#!/usr/bin/env python3
"""
Google Deep Research CLI for deloryx-book-value-creation.

Uses the Gemini **Deep Research agent** via the experimental Interactions API
(client.interactions.*). The agent autonomously plans, searches (Google Search +
URL context + code execution are built in), reads sources, and synthesises a long,
citation-rich report -- often WITH generated chart images. We run it in the
background, poll to completion, assemble the full report from all steps, save any
embedded visualizations, and write everything to research/<chapter-slug>.md. The
human/Claude drafts the chapter FROM the brief -- this tool never writes book prose.

Usage
-----
    .venv/bin/python tools/research/deep_research.py \\
        --topic "Google Ads Smart Bidding: Target CPA vs Target ROAS" \\
        --chapter "paid-acquisition-platforms"

Re-assemble an already-completed run without paying for a new one:
    .venv/bin/python tools/research/deep_research.py \\
        --chapter "paid-acquisition-platforms" --from-interaction v1_XXXX

Optional:
    --agent {max,standard,pro}   default: max (most comprehensive)
    --timeout SECONDS            max wait before cancelling (default 1800)
    --poll SECONDS               poll interval (default 15)

Deep Research runs take MINUTES (max tier can exceed 10 min). Prefer running this
in the background. Requires GEMINI_API_KEY in the environment (read; never echoed).
"""
from __future__ import annotations

import argparse
import base64
import datetime
import os
import pathlib
import re
import sys
import time
import warnings

try:
    from google import genai
except ModuleNotFoundError:
    sys.exit(
        "Error: google-genai not installed.\n"
        "  uv venv .venv && uv pip install -r tools/requirements.txt\n"
        "Then run with .venv/bin/python."
    )

warnings.filterwarnings("ignore", message="Interactions usage is experimental.*")

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
AGENTS = {
    "max": "deep-research-max-preview-04-2026",       # most comprehensive (default)
    "standard": "deep-research-preview-04-2026",       # faster / lighter
    "pro": "deep-research-pro-preview-12-2025",         # Dec-2025 Pro preview
}
RESEARCH_DIR = pathlib.Path(__file__).resolve().parents[2] / "research"

DONE = {"completed", "succeeded", "done"}
DEAD = {"failed", "error", "errored", "cancelled", "canceled"}

# Source policy injected into the directive. Default 'academic' = books + peer-reviewed
# ONLY (verifiable via ISBN/DOI), no open-web blogs. 'official' allows first-party vendor
# docs (for the ad-platform chapters). 'mixed' is permissive.
SOURCE_POLICIES = {
    "academic": (
        "SOURCE POLICY -- STRICT. Cite ONLY: (a) published BOOKS (textbooks, monographs, and "
        "seminal works used in graduate business curricula) with author(s), full title, edition, "
        "publisher, year, and ISBN; and (b) PEER-REVIEWED journal articles with author(s), title, "
        "journal, year, volume/issue, pages, and DOI. You MAY search the web to DISCOVER which "
        "texts/papers are canonical or assigned, but you MUST cite the book or paper ITSELF -- "
        "NEVER cite a blog, syllabus page, bookstore, Wikipedia, Medium, Quora, news article, or "
        "marketing/agency post. Exclude ALL non-peer-reviewed web content from the citation list. "
        "If no verifiable book or peer-reviewed paper supports a claim, omit it or flag it under Gaps."
    ),
    "official": (
        "SOURCE POLICY -- STRICT. Cite ONLY: (a) OFFICIAL first-party vendor documentation under "
        "canonical domains (support.google.com, developers.google.com, developers.facebook.com, "
        "business.facebook.com/help, support.google.com/analytics and equivalent official help/"
        "developer sites), giving the CANONICAL url (never a redirect); and (b) PEER-REVIEWED "
        "journal articles with DOI. Do NOT cite blogs, agency posts, Medium, Quora, news, or "
        "third-party tutorials. Flag any claim supported only by non-official sources under Gaps."
    ),
    "mixed": (
        "SOURCE POLICY. Prefer official first-party documentation and peer-reviewed sources; you "
        "may use reputable secondary sources but mark them clearly as secondary."
    ),
}

DIRECTIVE = """\
Produce a rigorous, citation-rich research brief on the topic below for a graduate-level \
business book. Use exact terminology and describe current behaviour as of {date}; flag \
anything that changed recently.

{policy}

Topic: {topic}

Structure the final report with these sections:
1. Key Concepts -- core mechanics, vocabulary, and distinctions a practitioner needs.
2. Formulas & Quantitative Relationships -- every relevant formula in LaTeX inline math \
(e.g. $ROAS = Revenue / AdSpend$). Omit only if genuinely none apply.
3. References -- a numbered list of EVERY source with full bibliographic metadata (books: \
author, title, edition, publisher, year, ISBN; papers: author, title, journal, year, \
volume/issue, pages, DOI; official docs: title + canonical URL + access date {date}).
4. Ready-to-Paste BibLaTeX Entries -- one entry per reference, correct type: @book (with \
isbn), @article (with doi), or @online (with urldate). Key format <authorORorg><year><slug>.
5. Gaps & Caveats -- what could NOT be verified against a book, peer-reviewed paper, or \
official doc, and what the author must double-check before publication.

Embed inline citations to every source you rely on."""


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9-]", "", text.lower().strip().replace(" ", "-"))


def assemble_report(interaction) -> tuple[str, list[tuple[str, object]]]:
    """Concatenate text from EVERY model_output step and collect embedded images.

    interaction.output_text typically holds only the LAST step, so the report
    must be assembled from interaction.steps[*].content[*] in order.
    """
    chunks: list[str] = []
    images: list[tuple[str, object]] = []
    for s in getattr(interaction, "steps", None) or []:
        if getattr(s, "type", None) != "model_output":
            continue
        content = getattr(s, "content", None) or []
        parts = content if isinstance(content, list) else (getattr(content, "parts", None) or [])
        for p in parts:
            t = getattr(p, "text", None)
            if isinstance(t, str) and t.strip():
                chunks.append(t.strip())
            data = getattr(p, "data", None)
            mime = getattr(p, "mime_type", "") or ""
            if data and mime.startswith("image/"):
                images.append((mime, data))
    text = "\n\n".join(chunks).strip()
    if not text:  # fallback for shapes where steps are absent
        text = (getattr(interaction, "output_text", "") or "").strip()
    return text, images


def _save_image(data, mime: str, stem: pathlib.Path) -> pathlib.Path:
    ext = "." + (mime.split("/")[-1] or "png")
    raw = base64.b64decode(data) if isinstance(data, str) else data
    out = pathlib.Path(f"{stem}{ext}")
    out.write_bytes(raw)
    return out


def persist(interaction, chapter: str, agent: str, iid: str, today: str) -> pathlib.Path:
    text, images = assemble_report(interaction)
    if not text:
        sys.exit("[deep_research] Completed but no text content found in steps.")
    slug = slugify(chapter)
    RESEARCH_DIR.mkdir(exist_ok=True)

    img_paths: list[pathlib.Path] = []
    for n, (mime, data) in enumerate(images, 1):
        try:
            img_paths.append(_save_image(data, mime, RESEARCH_DIR / f"{slug}-fig{n}"))
        except Exception as e:  # noqa: BLE001
            print(f"[deep_research] WARN: could not save image {n}: {e}")

    n_steps = len(getattr(interaction, "steps", []) or [])
    header = (
        f"<!-- Deep Research: agent={agent}; interaction={iid}; "
        f"steps={n_steps}; generated={today} -->\n\n"
    )
    if img_paths:
        header += "<!-- Generated visualizations: " + ", ".join(p.name for p in img_paths) + " -->\n\n"

    out = RESEARCH_DIR / f"{slug}.md"
    out.write_text(header + text, encoding="utf-8")
    print(f"[deep_research] Brief written to {out} ({len(text)} chars, {n_steps} steps, {len(img_paths)} images).")
    print("[deep_research] NOTE: citations are Google grounding-redirect URLs and may point at")
    print("[deep_research]       secondary blogs. Resolve & verify the canonical official-doc")
    print("[deep_research]       URL before adding any @online entry to references.bib.")
    return out


def run_research(topic, chapter, agent_key, timeout, poll, from_interaction=None, sources="academic") -> pathlib.Path:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("Error: GEMINI_API_KEY not set. Run `direnv allow` or export it.")
    client = genai.Client(api_key=api_key)
    today = datetime.date.today().isoformat()

    if from_interaction:
        print(f"[deep_research] Re-assembling existing interaction {from_interaction} (no new run)...", flush=True)
        interaction = client.interactions.get(from_interaction)
        st = (getattr(interaction, "status", "") or "").lower()
        if st not in DONE:
            sys.exit(f"[deep_research] interaction status is '{st}', not completed.")
        agent = getattr(interaction, "agent", AGENTS.get(agent_key, "?"))
        return persist(interaction, chapter, agent, from_interaction, today)

    if not topic:
        sys.exit("Error: --topic is required unless --from-interaction is given.")
    agent = AGENTS[agent_key]
    prompt = DIRECTIVE.format(topic=topic, date=today, policy=SOURCE_POLICIES[sources])

    print(f"[deep_research] Starting Deep Research agent '{agent}' (sources={sources}, background)...", flush=True)
    interaction = client.interactions.create(input=prompt, agent=agent, background=True)
    iid = interaction.id
    print(f"[deep_research] interaction id: {iid}", flush=True)
    print(f"[deep_research] polling every {poll}s (timeout {timeout}s). Runs take minutes.", flush=True)
    print(f"[deep_research] recover later with:  --chapter {slugify(chapter)} --from-interaction {iid}", flush=True)

    start = time.monotonic()
    status = getattr(interaction, "status", "in_progress")
    while True:
        elapsed = int(time.monotonic() - start)
        norm = (status or "").lower()
        if norm in DONE:
            break
        if norm in DEAD:
            sys.exit(f"[deep_research] FAILED after {elapsed}s (status={status}): {getattr(interaction,'error',None)}")
        if elapsed > timeout:
            try:
                client.interactions.cancel(iid)
            except Exception:  # noqa: BLE001
                pass
            sys.exit(f"[deep_research] TIMEOUT after {elapsed}s — cancelled {iid}.")
        time.sleep(poll)
        interaction = client.interactions.get(iid)
        status = getattr(interaction, "status", status)
        print(f"[deep_research]   {elapsed:>4}s  status={status}", flush=True)

    return persist(interaction, chapter, agent, iid, today)


def main() -> None:
    p = argparse.ArgumentParser(description="Google Deep Research brief generator (Interactions API)")
    p.add_argument("--topic", help="Specific research topic (use exact platform terms)")
    p.add_argument("--chapter", required=True, help="Target chapter slug, e.g. paid-acquisition-platforms")
    p.add_argument("--agent", choices=sorted(AGENTS), default="max", help="Deep Research tier (default: max)")
    p.add_argument("--timeout", type=int, default=1800, help="Max seconds before cancelling (default 1800)")
    p.add_argument("--poll", type=int, default=15, help="Poll interval seconds (default 15)")
    p.add_argument("--sources", choices=sorted(SOURCE_POLICIES), default="academic",
                   help="Source policy: academic=books+peer-reviewed ONLY (default); official=vendor docs+peer-reviewed; mixed=permissive")
    p.add_argument("--from-interaction", dest="from_interaction", help="Re-assemble an existing completed interaction id (no new run)")
    args = p.parse_args()
    run_research(args.topic, args.chapter, args.agent, args.timeout, args.poll, args.from_interaction, sources=args.sources)


if __name__ == "__main__":
    main()
