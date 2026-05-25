# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-volume **LaTeX book** — *Value Creation: An Applied Distillation of MBA & Marketing*. Not a software project. The deliverable is `main.pdf`, built from `.tex` sources. See `README.md` for the editorial concept (value-creation spine, layered depth, one template per concept).

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

- **`main.tex`** — master. `scrbook` class; **8 `\part`s spanning 21 chapters**; one `\input{chapters/NN-...}` per chapter, ordered along the *value-creation spine* (the sequence of business decisions), **not** by academic discipline. The spine adds an **Acquisition** part (08 digital funnel/CRM, 09 paid platforms, 10 attribution) and a **Reference** part (20 metrics catalog). Bibliography printed at the end as "Source Library".
- **`preamble.sty`** — all packages plus the concept-template engine. Defines **9** `tcolorbox` environments — `decision`, `intuition`, `derivation`, `breaks`, `worked`, `trap`, `deeper`, `contested`, `platform` (how Meta/Google actually work) — plus a compact `metriccard` reference-card environment with `\mcfield` (for the ch.20 metrics catalog). Every concept is written *through* these boxes. Package load order is load-bearing: `unicode-math` loads after `amsmath`/`mathtools` (it supersedes `amssymb`); `multicol`/`enumitem`/`graphicx` (`\graphicspath{{figures/}}`) load before `tikz`; `hyperref` then `cleveref` load **last**.
- **`references.bib`** — the source library: distilled books **plus** peer-reviewed papers (with `doi`) and official platform docs (`@online`, canonical Google/Meta URLs), ~98 entries. Most non-book entries were sourced and registry-verified via the `tools/` pipeline (see `tools/README.md`). Cite with `\textcite{key}` / `\parencite{key}` (biblatex, `authoryear` style, biber backend).

### The "unification" mechanism
The book's thesis is cross-linking the same idea across disciplines, implemented with labels + `cleveref`: chapters carry `\label{ch:slug}`, sections `\label{sec:slug}`, equations `\label{eq:slug}`, referenced via `\cref{...}`. Labels are **stable across renumbering** (e.g. `\label{ch:corporate-finance-core}` regardless of the file's number). Example: the growing-perpetuity derivation in `chapters/14` is explicitly wired to its customer-lifetime-value twin in the customer-economics chapter. When adding content, **add a label and cross-reference rather than restating** the shared concept.

### Chapter status
`chapters/14-corporate-finance-core.tex` is the **only drafted chapter and the canonical reference implementation** of the template — copy its structure and prose register. Every other `chapters/*.tex` is a stub: `\chapter{...}\label{ch:...}` + a scope comment (with cross-link notes) + a `TODO`. "Drafting a chapter" means filling a stub using the template boxes; for ch.20 it means `\metriccard` entries, not the 8-box template. Several chapters have a sourced research brief in `research/<slug>.md` to draft from.

## Conventions

- Currency: `\money{1250000}` → `$1,250,000` (helper in `preamble.sty`). Don't hand-format dollar amounts.
- Numbers/units: `siunitx` — `\num{}` for figures, `\qty{42}{\percent}` for units.
- Reusable equations: put them in `equation` with a `\label{eq:...}` so other chapters can `\cref` them instead of re-deriving.
- Keep the register of `chapters/11`: tight, practitioner-first, with one worked example carried through in real numbers.
