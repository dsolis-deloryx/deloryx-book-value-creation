# Value Creation — An Applied Distillation of MBA & Marketing

A single-volume distillation of the core MBA and marketing canon: advanced applied
knowledge, the formulas, and — crucially — *the reasoning behind each formula and why
it works*. Not a summary of textbooks; a unification of them.

## Design

- **Value-creation spine.** Organized around the sequence of decisions a business
  makes, not by academic discipline. Disciplines hang off the spine so cross-links
  (e.g. strategy → the `g` in a DCF, brand equity → the inputs to CLV) are explicit.
- **Layered depth.** Each concept reads at three levels: intuition (practitioner),
  a boxed derivation (the math), and a *Going Deeper* note (the advanced frontier).
- **One method per concept.** Every concept uses the same template, implemented as
  `tcolorbox` environments in `preamble.sty`:

  | Box | Purpose |
  |---|---|
  | `decision`   | The real question this answers |
  | `intuition`  | Plain-language version |
  | `derivation` | Build the formula from first principles |
  | `breaks`     | Assumptions and when the model fails |
  | `worked`     | Real numbers, one running company throughout |
  | `trap`       | The classic misuse |
  | `deeper`     | Advanced extension |
  | `contested`  | Where the field genuinely disagrees |
  | `platform`   | How Meta/Google actually work (grounded in official docs) |

  The metrics catalog (Reference part) uses a compact `metriccard` environment
  instead — formula, what it tells you, the trap/vanity flag, and a benchmark.

## Build

Requires TeX Live with `luatex`, `mathscience`, `bibtexextra`, `fontsrecommended`,
`binextra`, and `biber`. Then:

```bash
latexmk          # LuaLaTeX + biber, driven by ./latexmkrc -> main.pdf
latexmk -c       # clean aux files
```

## Structure

```
main.tex           # master: \part + \input chapter files
preamble.sty       # packages, template boxes (incl. platform + metriccard), cross-ref setup
references.bib     # source library: books + peer-reviewed papers (DOIs) + official docs (~98 entries)
latexmkrc          # build config (LuaLaTeX, biber)
chapters/          # one file per chapter, grouped into 8 parts (21 chapters)
figures/           # TikZ (*.tex) + matplotlib (src/*.py) -> *.pdf via tools/build-figures.sh
research/          # Deep-Research briefs per chapter (the drafting source)
tools/             # research + diagram pipelines (see tools/README.md)
```

## Chapter arc

1. **Foundations of Value** — what business is for, decisions under uncertainty, microeconomics
2. **Customer Understanding** — STP, brand growth, customer economics, pricing
3. **Acquisition: Classical & Digital** — digital funnel & CRM, paid platforms (Meta/Google), attribution & measurement
4. **Strategy** — competitive analysis, advantage & disruption, growth & moats
5. **Finance & Valuation** — corporate finance core, valuation, risk & capital structure
6. **Execution** — operations & constraints, organizational behavior, business models & unit economics
7. **Reference** — business metrics catalog
8. **Capstone** — one company analyzed through every lens
