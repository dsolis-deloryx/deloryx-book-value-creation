"""
figures/src/mrr-waterfall.py
MRR waterfall chart: starting MRR -> +new -> +expansion -> -contraction -> -churn -> ending MRR.
Numbers match the running SaaS fact sheet (ch.13 growth accounting).
Output: figures/mrr-waterfall.pdf
Run:    .venv/bin/python figures/src/mrr-waterfall.py
   or:  ./tools/build-figures.sh mrr-waterfall
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.patches as mpatches  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# ---- Data (all values in $000s for axis readability) ----
start_mrr   = 340   # $340,000
new_mrr     =  30   # +$30,000
expansion   =  20   # +$20,000
contraction =   5   # -$5,000
churn       =  22   # -$22,000
end_mrr     = start_mrr + new_mrr + expansion - contraction - churn  # 363

labels  = ["Start\nMRR", "New", "Expansion", "Contraction", "Churn", "End\nMRR"]
values  = [start_mrr, new_mrr, expansion, -contraction, -churn, end_mrr]

# Compute running bottoms for the floating bars (connectors)
# Start and End are absolute bars; intermediate bars float.
bottoms = [0, start_mrr, start_mrr + new_mrr, start_mrr + new_mrr + expansion,
           start_mrr + new_mrr + expansion - contraction, 0]

# Palette: book theme blues/teals/reds
COLOR_BASE   = "#1A5276"   # vcblue  — start/end bars
COLOR_POS    = "#0E6655"   # vcteal  — positive movements
COLOR_NEG    = "#7B241C"   # breaks red — negative movements

colors = [COLOR_BASE, COLOR_POS, COLOR_POS, COLOR_NEG, COLOR_NEG, COLOR_BASE]
heights = [start_mrr, new_mrr, expansion, contraction, churn, end_mrr]
# For negative bars, bottom is the running total, height is positive (matplotlib handles direction)
plot_bottoms = [0,
                start_mrr,
                start_mrr + new_mrr,
                start_mrr + new_mrr + expansion - contraction,  # bottom of contraction bar
                start_mrr + new_mrr + expansion - contraction - churn,  # bottom of churn bar
                0]
plot_heights = [start_mrr, new_mrr, expansion, contraction, churn, end_mrr]

fig, ax = plt.subplots()

x = np.arange(len(labels))
bars = ax.bar(x, plot_heights, bottom=plot_bottoms, color=colors,
              width=0.55, linewidth=0.7, edgecolor="white")

# Connector lines between bars
running = start_mrr
connector_pairs = [
    (0, running),
    (running, running + new_mrr),
    (running + new_mrr, running + new_mrr + expansion),
    (running + new_mrr + expansion, running + new_mrr + expansion - contraction),
    (running + new_mrr + expansion - contraction,
     running + new_mrr + expansion - contraction - churn),
]
for i, (y_from, y_to) in enumerate(connector_pairs):
    ax.plot([x[i] + 0.275, x[i + 1] - 0.275], [y_from, y_from],
            color="#AAAAAA", linewidth=0.7, linestyle="--", zorder=0)

# Value labels on each bar
label_vals = [f"+{start_mrr}", f"+{new_mrr}", f"+{expansion}",
              f"-{contraction}", f"-{churn}", f"+{end_mrr}"]
label_vals[0] = f"{start_mrr}"
label_vals[-1] = f"{end_mrr}"
for bar, lv, pb, ph in zip(bars, label_vals, plot_bottoms, plot_heights):
    mid = pb + ph / 2
    ax.text(bar.get_x() + bar.get_width() / 2, mid,
            f"${lv}k", ha="center", va="center",
            fontsize=7.5, color="white", fontweight="bold", fontfamily="serif")

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=8)
ax.set_ylabel("MRR ($000s)")
ax.set_ylim(0, end_mrr * 1.12)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${int(v)}k"))

# Legend
pos_patch = mpatches.Patch(color=COLOR_POS, label="Positive movements")
neg_patch = mpatches.Patch(color=COLOR_NEG, label="Negative movements")
base_patch = mpatches.Patch(color=COLOR_BASE, label="Total MRR")
ax.legend(handles=[pos_patch, neg_patch, base_patch], fontsize=7)

fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "mrr-waterfall.pdf"
fig.savefig(out, format="pdf")
print(f"[mrr-waterfall] Written to {out}")
