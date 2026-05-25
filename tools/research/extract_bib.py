#!/usr/bin/env python3
"""
Extract paste-ready BibLaTeX from a Deep Research brief.

The Deep Research agent reliably NAMES canonical books and peer-reviewed papers
(with editions/years/authors) but will not emit clean biblatex. This companion
runs a fast model (gemini-2.5-flash, NO web grounding — pure text->biblatex) over
a research/*.md brief and emits @book / @article / @online entries built ONLY from
metadata present in the text. It never invents ISBNs/DOIs; missing identifiers are
flagged with a TODO comment for the author to verify.

Usage
-----
    .venv/bin/python tools/research/extract_bib.py --infile research/curriculum-canon.md
    # -> references-curriculum-canon.bib  (staging; review + dedupe before merging into references.bib)

Requires GEMINI_API_KEY (read; never echoed).
"""
from __future__ import annotations

import argparse
import os
import pathlib
import sys

try:
    from google import genai
    from google.genai import types
except ModuleNotFoundError:
    sys.exit("Error: google-genai not installed. uv pip install -r tools/requirements.txt")

MODEL = "gemini-2.5-flash"  # plain generate_content, no tools — deterministic-ish formatting

INSTRUCTION = """\
You convert a research brief into BibLaTeX. Be EXHAUSTIVE: the brief may name 20-40 \
distinct works across many discipline sections. Walk the brief top to bottom and emit \
an entry for EVERY distinct book and peer-reviewed paper it names — do NOT stop early, \
do NOT summarise, do NOT skip a discipline. For each, emit one entry:

- Books -> @book{key, author={...}, title={...}, edition={N}, year={YYYY}, publisher={...}, isbn={...}}
- Papers -> @article{key, author={...}, title={...}, journaltitle={...}, year={YYYY}, volume={...}, number={...}, pages={...}, doi={...}}
- Official vendor docs (only if present) -> @online{key, author={{Org}}, title={...}, year={YYYY}, url={...}, urldate={...}, organization={...}}

HARD RULES:
- Use ONLY metadata explicitly present in the brief text. NEVER invent an ISBN, DOI,
  URL, page range, volume, or publisher. If a field is not in the text, OMIT the field
  and add, on the line immediately AFTER the entry, a comment:  % TODO verify <key>: missing <fields>
- Multiple authors joined with " and ". Key format: <firstauthorlastname><year><short-slug>, lowercase.
- De-duplicate: one entry per work even if cited several times.
- Output ONLY BibLaTeX (entries + the TODO comments). No prose, no code fences, no headings.

BRIEF:
---
{brief}
---
"""


def main() -> None:
    ap = argparse.ArgumentParser(description="Extract BibLaTeX from a research brief (gemini-2.5-flash)")
    ap.add_argument("--infile", required=True, help="Path to research/<slug>.md")
    ap.add_argument("--out", help="Output .bib (default: references-<slug>.bib in repo root)")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("Error: GEMINI_API_KEY not set.")

    infile = pathlib.Path(args.infile)
    if not infile.is_file():
        sys.exit(f"Error: {infile} not found.")
    brief = infile.read_text(encoding="utf-8")

    repo_root = pathlib.Path(__file__).resolve().parents[2]
    out = pathlib.Path(args.out) if args.out else repo_root / f"references-{infile.stem}.bib"

    client = genai.Client(api_key=api_key)
    print(f"[extract_bib] {MODEL}: extracting biblatex from {infile} ...", flush=True)
    resp = client.models.generate_content(
        model=MODEL,
        contents=INSTRUCTION.replace("{brief}", brief),
        config=types.GenerateContentConfig(temperature=0.0, max_output_tokens=16384),
    )
    fr = None
    for cand in (resp.candidates or []):
        fr = getattr(cand, "finish_reason", None)
    print(f"[extract_bib] finish_reason={fr}")
    text = (resp.text or "").strip()
    # strip accidental code fences
    if text.startswith("```"):
        text = text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
    if not text:
        sys.exit("[extract_bib] Model returned no text.")

    header = (
        f"% Extracted from {infile.name} by tools/research/extract_bib.py ({MODEL}).\n"
        f"% STAGING FILE — review every entry, verify/fill ISBN & DOI, dedupe against\n"
        f"% references.bib (keys may collide), then merge. Identifiers are NOT invented:\n"
        f"% any missing field is flagged with a TODO comment.\n\n"
    )
    out.write_text(header + text + "\n", encoding="utf-8")
    n_book = text.count("@book")
    n_art = text.count("@article")
    n_onl = text.count("@online")
    n_todo = text.count("% TODO")
    print(f"[extract_bib] wrote {out}  (@book={n_book} @article={n_art} @online={n_onl}; {n_todo} TODO).")
    print("[extract_bib] Verify ISBN/DOI before merging into references.bib.")


if __name__ == "__main__":
    main()
