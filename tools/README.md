# Tooling — research & diagram pipelines

Supporting tools for *Value Creation*. None are part of the LaTeX build; they
generate **research briefs**, **verified references**, and **figures** that feed
the book. The book itself still builds with plain `latexmk`.

## Setup (one-time)

`pip` is absent / externally-managed on this machine; use **`uv`**:

```bash
uv venv .venv
uv pip install -r tools/requirements.txt   # google-genai, matplotlib, numpy, pandas
```

Secrets: scripts read **only** `GEMINI_API_KEY` from the environment (loaded by
direnv from the git-ignored `.envrc`). Nothing else is read; the env is never echoed.

## Reference pipeline — discover → format → resolve → merge

Deep Research *discovers* canonical works but won't emit clean BibLaTeX, and its
citations are opaque grounding-redirect URLs. The chain fixes both; **identifiers
are never invented** — DOIs/ISBNs come from registries, URLs from following redirects.

| Step | Script | Does |
|------|--------|------|
| 1. Discover | `research/deep_research.py` | Google **Deep Research** agent (Interactions API, async + poll). `--sources academic\|official\|mixed` enforces a source policy. Writes `research/<slug>.md` + any generated chart PNGs. |
| 2. Format | `research/extract_bib.py` | `gemini-2.5-flash` (no grounding) turns the brief's named works into `@book`/`@article` stubs. Missing fields flagged `% TODO`, never fabricated. → `references-<slug>.bib` |
| 3a. Resolve papers/books | `research/resolve_bib.py` | Crossref → OpenAlex fill **DOIs** (title-gated to avoid wrong-paper matches); books pass through as-authored (work-level ISBNs are edition-unreliable). → `references-<slug>.resolved.bib` |
| 3b. Resolve doc URLs | `research/resolve_urls.py` | Follows grounding redirects to **canonical** Google/Meta URLs, drops non-official domains, fetches page titles. → `references-<slug>.bib` (`@online`) |
| 4. Merge | manual / small script | Dedupe against `references.bib`, append, `latexmk` to confirm biber is clean. |

### Examples

```bash
# Discover (long: Deep Research Max runs ~12 min — prefer a background runner)
.venv/bin/python tools/research/deep_research.py \
    --sources official --chapter "paid-acquisition-platforms" \
    --topic "Meta & Google ad auction, bidding strategies, learning phase, PMax"

# Recover a finished run without paying again
.venv/bin/python tools/research/deep_research.py \
    --chapter "paid-acquisition-platforms" --from-interaction v1_XXXX

# Format + resolve
.venv/bin/python tools/research/extract_bib.py  --infile research/<slug>.md
.venv/bin/python tools/research/resolve_bib.py  --bib   references-<slug>.bib       # papers/books → DOIs
.venv/bin/python tools/research/resolve_urls.py --infile research/<slug>.md          # docs → canonical @online
```

**Source policies:** `academic` = books + peer-reviewed only (ISBN/DOI; no web).
`official` = first-party vendor docs (canonical Google/Meta domains) + peer-reviewed.
`mixed` = permissive. Theory-heavy chapters often need an `academic` pass for papers
*and* an `official` pass for platform docs (e.g. ch.10).

**Audit trail:** `research/*.md` briefs are committed. `references-*.bib` /
`*.resolved.bib` are intermediate staging (git-ignored) — only `references.bib` is canonical.

## Diagram pipeline (TikZ + matplotlib)

```bash
./tools/build-figures.sh                 # rebuild all figures
./tools/build-figures.sh retention_curve # one stem only
```

- Conceptual diagrams: standalone TikZ in `figures/*.tex` → `figures/*.pdf`.
- Data plots: matplotlib in `figures/src/*.py` (shared `figures/src/booktheme.mplstyle`,
  serif + tcolorbox palette) → `figures/*.pdf`.
- Embed with `\includegraphics{<stem>}` (preamble sets `\graphicspath{{figures/}}`).
- Run `build-figures.sh` **before** `latexmk`; `figures/*.pdf` are git-ignored (regenerated).

## Optional / local

Ollama (`nomic-embed-text`, `qwen3-vl`) can later dedupe briefs or read ad-dashboard
screenshots — not wired in. Deep Research Max can emit chart PNGs into `research/`;
treat them as reference, then re-author in TikZ/matplotlib to match the book's style.
