#!/usr/bin/env bash
# tools/build-figures.sh
# Pre-build all figures (TikZ standalones + matplotlib scripts) before latexmk.
#   ./tools/build-figures.sh                         # rebuild everything
#   ./tools/build-figures.sh retention_curve         # rebuild one stem only
#   ./tools/build-figures.sh funnel-awareness-to-purchase
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FIGURES_DIR="$REPO_ROOT/figures"
PYTHON="$REPO_ROOT/.venv/bin/python"
filter="${1:-}"

cd "$REPO_ROOT"

# --- TikZ standalones (figures/*.tex -> figures/*.pdf) ---
shopt -s nullglob
for texfile in "$FIGURES_DIR"/*.tex; do
    stem="$(basename "$texfile" .tex)"
    [[ -n "$filter" && "$filter" != "$stem" ]] && continue
    echo "[figures] TikZ: $stem"
    lualatex -interaction=nonstopmode -halt-on-error \
        -output-directory="$FIGURES_DIR" "$texfile" >/dev/null
    rm -f "$FIGURES_DIR/$stem.aux" "$FIGURES_DIR/$stem.log" "$FIGURES_DIR/$stem.fls"
done

# --- matplotlib scripts (figures/src/*.py -> figures/*.pdf) ---
if [[ ! -x "$PYTHON" ]]; then
    echo "[figures] WARNING: .venv/bin/python missing — skipping Python figures."
    echo "          uv venv .venv && uv pip install -r tools/requirements.txt"
else
    for pyfile in "$FIGURES_DIR"/src/*.py; do
        stem="$(basename "$pyfile" .py)"
        [[ "$stem" == "booktheme" ]] && continue
        [[ -n "$filter" && "$filter" != "$stem" ]] && continue
        echo "[figures] matplotlib: $stem"
        "$PYTHON" "$pyfile"
    done
fi

echo "[figures] Done. Run 'latexmk' to rebuild the book."
