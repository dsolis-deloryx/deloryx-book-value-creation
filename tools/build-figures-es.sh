#!/usr/bin/env bash
# tools/build-figures-es.sh
# Pre-build all SPANISH figures (TikZ standalones + matplotlib scripts) before `latexmk main-es.tex`.
#   ./tools/build-figures-es.sh                         # rebuild everything
#   ./tools/build-figures-es.sh value-spine             # rebuild one stem only
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FIGURES_DIR="$REPO_ROOT/figures-es"
PYTHON="$REPO_ROOT/.venv/bin/python"
filter="${1:-}"

cd "$REPO_ROOT"

# --- TikZ standalones (figures-es/*.tex -> figures-es/*.pdf) ---
shopt -s nullglob
for texfile in "$FIGURES_DIR"/*.tex; do
    stem="$(basename "$texfile" .tex)"
    [[ -n "$filter" && "$filter" != "$stem" ]] && continue
    echo "[figures-es] TikZ: $stem"
    lualatex -interaction=nonstopmode -halt-on-error \
        -output-directory="$FIGURES_DIR" "$texfile" >/dev/null
    rm -f "$FIGURES_DIR/$stem.aux" "$FIGURES_DIR/$stem.log" "$FIGURES_DIR/$stem.fls"
done

# --- matplotlib scripts (figures-es/src/*.py -> figures-es/*.pdf) ---
if [[ ! -x "$PYTHON" ]]; then
    echo "[figures-es] WARNING: .venv/bin/python missing — skipping Python figures."
    echo "             uv venv .venv && uv pip install -r tools/requirements.txt"
else
    for pyfile in "$FIGURES_DIR"/src/*.py; do
        stem="$(basename "$pyfile" .py)"
        [[ "$stem" == "booktheme" ]] && continue
        [[ -n "$filter" && "$filter" != "$stem" ]] && continue
        echo "[figures-es] matplotlib: $stem"
        "$PYTHON" "$pyfile"
    done
fi

echo "[figures-es] Done. Run 'latexmk main-es.tex' to rebuild the Spanish edition."
