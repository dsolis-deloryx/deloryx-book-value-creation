"""
figures/src/dcf-bridge.py
DCF waterfall / bridge chart: PV of each explicit-year FCF plus PV of terminal value
summing to enterprise value. Illustrates that terminal value dominates (~80% of EV).
Output: figures/dcf-bridge.pdf
Run:    .venv/bin/python figures/src/dcf-bridge.py
   or:  ./tools/build-figures.sh dcf-bridge
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# --- Fact-sheet numbers (running B2B SaaS) ---
wacc = 0.11
fcf_y1 = 600_000
growth_rates = [0.30, 0.30, 0.30, 0.10, 0.10]  # years 1-5

fcfs = [fcf_y1]
for g in growth_rates[1:]:
    fcfs.append(fcfs[-1] * (1 + g))

# PV of each explicit-year FCF
pv_explicit = [fcf / (1 + wacc) ** (t + 1) for t, fcf in enumerate(fcfs)]

# Terminal value: year-5 FCF * (1+g_steady) / (wacc - g_steady), then discount back 5 yrs
g_steady = 0.03
tv = fcfs[-1] * (1 + g_steady) / (wacc - g_steady)
pv_tv = tv / (1 + wacc) ** 5

labels = ["Y1 FCF", "Y2 FCF", "Y3 FCF", "Y4 FCF", "Y5 FCF", "Terminal\nValue"]
values = pv_explicit + [pv_tv]

# Colour: explicit years use derivation-violet, terminal uses decision-blue
colors = ["#6C3483"] * 5 + ["#1A5276"]

fig, ax = plt.subplots()

# Running bottom for stacked waterfall
bottoms = np.zeros(len(values))
for i, (val, color, label) in enumerate(zip(values, colors, labels)):
    ax.bar(i, val / 1e6, color=color, alpha=0.88, edgecolor="white", linewidth=0.4)
    ax.text(
        i,
        val / 1e6 + 0.15,
        f"{val/1e6:.1f}",
        ha="center",
        va="bottom",
        fontsize=7,
    )

# Horizontal line at total EV
total_ev = sum(values)
ax.axhline(total_ev / 1e6, color="#7B241C", linewidth=1.0, linestyle="--", alpha=0.7)
ax.text(
    len(values) - 0.5,
    total_ev / 1e6 + 0.3,
    f"EV = ${total_ev/1e6:.1f}M",
    ha="right",
    fontsize=8,
    color="#7B241C",
)

ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=8)
ax.set_ylabel("Present value ($M)")
ax.set_title("DCF bridge: explicit FCFs + terminal value", fontsize=10)
ax.set_ylim(0, pv_tv / 1e6 * 1.18)

# Percentage annotation on TV bar
tv_pct = pv_tv / total_ev * 100
ax.text(
    5,
    pv_tv / 1e6 / 2,
    f"{tv_pct:.0f}% of EV",
    ha="center",
    va="center",
    fontsize=8,
    color="white",
    fontweight="bold",
)

fig.tight_layout(pad=0.4)
out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "dcf-bridge.pdf"
fig.savefig(out, format="pdf")
print(f"[dcf-bridge] Written to {out}")
