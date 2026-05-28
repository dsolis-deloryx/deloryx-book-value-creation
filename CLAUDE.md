# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-volume **LaTeX book** — *Value Creation: An Applied Distillation of MBA, Marketing & the Founder's Craft*. Not a software project. The deliverable is `main.pdf`, built from `.tex` sources. See `README.md` for the editorial concept (value-creation spine, layered depth, one template per concept).

## Build

```bash
latexmk        # LuaLaTeX + biber → main.pdf (driven by ./latexmkrc)
latexmk -c     # remove aux files, keep main.pdf
latexmk -C     # remove aux files AND main.pdf
```

Toolchain: TeX Live with `luatex`, `mathscience`, `bibtexextra`, `fontsrecommended`, `binextra`, `biber`.

The build **must** use LuaLaTeX (`$pdf_mode=4` in `latexmkrc`) — `fontspec` + `unicode-math` require it; pdfLaTeX will fail. There is no test suite; a clean `latexmk` run is the only correctness check — read `main.log` for errors.

Chapters are pulled in with `\input` (not `\include`), so `\includeonly` partial builds are **not** available. To iterate on one chapter, temporarily comment the other `\input` lines in `main.tex`.

Figures are **pre-built**, not part of the LaTeX run: `./tools/build-figures.sh` compiles standalone TikZ (`figures/*.tex`) and matplotlib scripts (`figures/src/*.py`) to `figures/*.pdf` before `latexmk`. Research/reference tooling (Gemini Deep Research → registry-verified BibLaTeX) lives in `tools/` — see `tools/README.md`. Python tools use a `uv` venv: `uv venv .venv && uv pip install -r tools/requirements.txt`.

## Architecture

Three files carry the system; the chapter files are thin.

- **`main.tex`** — master. `scrbook` class; **9 `\part`s spanning 32 chapters**; one `\input{chapters/NN-...}` per chapter, ordered along the *value-creation spine* (the sequence of business decisions), **not** by academic discipline. The Acquisition part (10 channels/GTM/sales, 11 digital funnel/CRM, 12 paid platforms, 13 attribution), the Founder part (27 persuasion/influence, 28 storytelling/communication, 29 founder-psychology, 30 leadership/charisma), and the Reference part (31 metrics catalog) sit on that spine. Bibliography printed at the end as "Source Library".
- **`preamble.sty`** — all packages plus the layout engine. Concepts are written as **flowing prose under `\section` headings** with two restrained monochrome set-offs — `example` (numbered worked examples) and `admonition{Label}` (Warning/Note callouts) — plus a compact `metriccard` reference-card environment with `\mcfield` (for the ch.31 metrics catalog). (Earlier drafts used a 9-box `tcolorbox` system; it was superseded by the prose + set-off style — do not reintroduce the boxes.) Package load order is load-bearing: `unicode-math` loads after `amsmath`/`mathtools` (it supersedes `amssymb`); `multicol`/`enumitem`/`graphicx` (`\graphicspath{{figures/}}`) load before `tikz`; `hyperref` then `cleveref` load **last**.
- **`references.bib`** — the source library: distilled books **plus** peer-reviewed papers (with `doi`) and official platform docs (`@online`, canonical Google/Meta URLs) **plus a Part-VII applied-science layer** (peer-reviewed meta-analyses & field experiments with Crossref-verified DOIs), ~185 entries. Most non-book entries were sourced and registry-verified via the `tools/` pipeline (see `tools/README.md`). Cite with `\textcite{key}` / `\parencite{key}` (biblatex, `authoryear` style, biber backend).

### The "unification" mechanism
The book's thesis is cross-linking the same idea across disciplines, implemented with labels + `cleveref`: chapters carry `\label{ch:slug}`, sections `\label{sec:slug}`, equations `\label{eq:slug}`, referenced via `\cref{...}`. Labels are **stable across renumbering** (e.g. `\label{ch:corporate-finance-core}` regardless of the file's number — chapters have been renumbered as the spine grew, but `\cref` targets the slug, so cross-refs never break). Example: the growing-perpetuity derivation in `chapters/19-corporate-finance-core.tex` is explicitly wired to its customer-lifetime-value twin in the customer-economics chapter. When adding content, **add a label and cross-reference rather than restating** the shared concept.

### Chapter status
All 32 chapters are drafted. `chapters/19-corporate-finance-core.tex` (the growing perpetuity) is the **canonical style exemplar** — copy its register: flowing prose under `\section` headings, with `example` for reasoning-first worked numbers and `admonition{Warning|Note}` for cautions. ch.31 (metrics catalog) uses `metriccard`/`\mcfield`, not the prose template. The Founder part (Part VII, ch.27–30) covers the entrepreneur's soft skills — persuasion, storytelling, psychology, leadership — grounded strictly in field-validated applied science (meta-analyses & field experiments with reported effect sizes; trade books demoted to signposts behind their peer-reviewed primary sources). Every skill ties to a hard metric (CAC, CLV, churn, ROIC). A single B2B-SaaS running company carries every worked example (fact sheet in the capstone, ch.32). Per-chapter research briefs live in `research/<slug>.md`.

## Conventions

- Currency: `\money{1250000}` → `$1,250,000` (helper in `preamble.sty`). Don't hand-format dollar amounts.
- Numbers/units: `siunitx` — `\num{}` for figures, `\qty{42}{\percent}` for units.
- Reusable equations: put them in `equation` with a `\label{eq:...}` so other chapters can `\cref` them instead of re-deriving.
- Keep the register of `chapters/19-corporate-finance-core.tex`: tight, practitioner-first, with worked examples carried through in real numbers (the one running SaaS company).
