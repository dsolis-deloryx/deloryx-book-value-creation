"""
figures/src/bid_response.py
The volume--efficiency trade-off for a Target-CPA bid strategy (ch.09).
Conversions rise and saturate as the cost target loosens; below the learning-phase
floor (~50 events/week) delivery destabilises; above the LTV:CAC ceiling, unit
economics break. The usable window sits between.
Output: figures/bid_response.pdf
Run:    .venv/bin/python figures/src/bid_response.py  (or ./tools/build-figures.sh bid_response)
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

plt.style.use(str(pathlib.Path(__file__).parent / "booktheme.mplstyle"))

# weekly conversions as a saturating function of the Target CPA constraint
cpa = np.linspace(100, 1400, 400)
K, h = 150.0, 900.0
conv = K * cpa / (cpa + h)

LEARN = 50            # learning-phase floor: ~50 events / 7 days
CEIL = 1050           # LTV:CAC = 3 ceiling (LTV 3150 / 3)
cpa_floor = h * LEARN / (K - LEARN)   # CPA where conv == 50  -> 450

fig, ax = plt.subplots()
ax.plot(cpa, conv, color="#1A5276", label="Weekly conversions")

# usable window
ax.axvspan(cpa_floor, CEIL, color="#0E6655", alpha=0.08)
ax.axhline(LEARN, color="#7B241C", lw=0.9, ls="--")
ax.axvline(CEIL, color="#935116", lw=0.9, ls=":")

# operating point (Target CPA = $600)
op_cpa = 600
op_conv = K * op_cpa / (op_cpa + h)
ax.plot([op_cpa], [op_conv], "o", color="#4D4D4D", ms=5, zorder=5)

ax.annotate("learning floor (~50/wk)", xy=(180, LEARN), xytext=(180, LEARN + 8),
            color="#7B241C", fontsize=7)
ax.annotate("LTV:CAC = 3 ceiling", xy=(CEIL, 18), xytext=(CEIL - 40, 18),
            color="#935116", fontsize=7, ha="right", rotation=90, va="bottom")
ax.annotate("operating point\n$600 target", xy=(op_cpa, op_conv),
            xytext=(op_cpa + 90, op_conv - 22), fontsize=7, color="#4D4D4D",
            arrowprops=dict(arrowstyle="-", color="#4D4D4D", lw=0.6))
ax.annotate("too tight:\nLearning Limited", xy=(300, K * 300 / (300 + h)),
            xytext=(150, 92), fontsize=7, color="#7B241C")

ax.set_xlabel("Target CPA constraint (\\$)")
ax.set_ylabel("Conversions per week")
ax.set_xlim(100, 1400)
ax.set_ylim(0, 105)
fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "bid_response.pdf"
fig.savefig(out, format="pdf")
print(f"[bid_response] Written to {out}")
