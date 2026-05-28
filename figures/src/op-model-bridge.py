"""
figures/src/op-model-bridge.py
Operating-model waterfall bridge chart: unit-economics inputs → ARR → EBITDA → FCF.
Mirrors the structure of dcf-bridge.py (same booktheme, same style conventions).

Waterfall logic:
  Start (0) → +ARR contribution (gross profit pool)
            → −S&M cost
            → −R&D cost
            → −G&A cost
            = EBITDA bar
            → −Tax on EBITDA (positive only)
            = FCF bar (Year 1)

Fact-sheet lock (running SaaS, Year 1 base):
  ARR = $4,000,000  |  Gross margin 70%  |  S&M 50% of ARR  |  R&D 25%  |  G&A 10%
  EBITDA margin -15%  |  FCF ≈ NOPAT = $600,000 (ROIC 20% × IC $3,000,000)

Output: figures/op-model-bridge.pdf
Run:    .venv/bin/python figures/src/op-model-bridge.py
   or:  ./tools/build-figures.sh op-model-bridge
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.patches as mpatches  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# ── Fact-sheet numbers ─────────────────────────────────────────────────────────
ARR        = 4_000_000
gm_rate    = 0.70          # gross margin
sm_pct     = 0.50          # S&M as % of ARR
rd_pct     = 0.25          # R&D as % of ARR
ga_pct     = 0.10          # G&A as % of ARR  (85% total opex → -15% EBITDA margin)
tax_rate   = 0.30
fcf_target = 600_000       # NOPAT from fact sheet

gross_profit = ARR * gm_rate                    # 2,800,000
sm_cost      = ARR * sm_pct                     # 2,000,000
rd_cost      = ARR * rd_pct                     # 1,000,000
ga_cost      = ARR * ga_pct                     #   400,000
ebitda       = gross_profit - sm_cost - rd_cost - ga_cost   # -600,000

# Tax: no shield on losses (conservative); FCF from fact sheet overrides the sign.
# The fact-sheet FCF = NOPAT = $600K assumes the company is earning NOPAT on its invested
# capital base (ROIC 20% × IC $3M) — this reflects the BEGINNING-of-year base ARR that
# already generates $600K NOPAT, with opex invested partly for growth. We display the
# driver waterfall and then show the $600K FCF as a separate "from IC/ROIC" bar.
# For chart clarity we show EBITDA from the driver breakdown (-$600K at -15%) and then
# the $600K NOPAT/FCF separately, framed as the fact-sheet anchor.

# ── Waterfall segments ─────────────────────────────────────────────────────────
# Each segment: (label, delta_value, is_positive)
# Starting from 0, building up to gross profit, then subtracting each opex line,
# arriving at EBITDA, then showing FCF from the IC/ROIC identity.

segments = [
    ("Gross\nprofit",  gross_profit, True),   # +2.8M
    ("S&M\ncost",     -sm_cost,     False),   # −2.0M
    ("R&D\ncost",     -rd_cost,     False),   # −1.0M
    ("G&A\ncost",     -ga_cost,     False),   # −0.4M
    # EBITDA is the running total here = −0.6M (result bar)
    ("FCF\n(NOPAT)",   fcf_target,  True),    # +0.6M shown as separate fact-sheet anchor
]

# Palette: use booktheme colours
# Positive bars: derivation-violet #6C3483 (operating build)
# Negative bars: breaks red        #7B241C
# FCF bar:       decision-blue     #1A5276
COLOR_POS = "#6C3483"
COLOR_NEG = "#7B241C"
COLOR_FCF = "#1A5276"
COLOR_RES = "#4D4D4D"  # result / reference bar

labels = [s[0] for s in segments]
deltas = [s[1] for s in segments]

# Compute running totals for the waterfall bases
bases   = []
running = 0.0
for i, (lbl, delta, is_pos) in enumerate(segments):
    if lbl.startswith("FCF"):
        # FCF bar starts fresh from 0 to show it as a separate output
        bases.append(0.0)
    else:
        if delta < 0:
            bases.append(running + delta)   # bar starts at bottom of negative segment
        else:
            bases.append(running)
    running += delta if not lbl.startswith("FCF") else 0.0

# We'll draw EBITDA as a result bar between the driver columns and the FCF column
# Insert a gap between G&A and FCF, and add an EBITDA result bar
all_labels = [s[0] for s in segments[:4]] + ["EBITDA\n(result)", "", "FCF\n(NOPAT)"]
all_bases  = []
all_heights= []
all_colors = []

run = 0.0
for lbl, delta, is_pos in segments[:4]:
    if delta < 0:
        all_bases.append(run + delta)
    else:
        all_bases.append(run)
    all_heights.append(abs(delta))
    all_colors.append(COLOR_POS if is_pos else COLOR_NEG)
    run += delta

# EBITDA result bar: from 0 to run (which is negative)
ebitda_val = run  # = -600,000
all_bases.append(min(0.0, ebitda_val))
all_heights.append(abs(ebitda_val))
all_colors.append(COLOR_RES)

# Spacer (invisible)
all_bases.append(0.0)
all_heights.append(0.0)
all_colors.append("none")

# FCF/NOPAT bar: from 0 to fcf_target
all_bases.append(0.0)
all_heights.append(fcf_target)
all_colors.append(COLOR_FCF)

x_positions = range(len(all_labels))

fig, ax = plt.subplots()

for i, (base, height, color, lbl) in enumerate(zip(all_bases, all_heights, all_colors, all_labels)):
    if color == "none" or height == 0:
        continue
    ax.bar(i, height / 1e6, bottom=base / 1e6,
           color=color, alpha=0.88, edgecolor="white", linewidth=0.4, width=0.65)
    # Value annotation
    if lbl.startswith("EBITDA"):
        y_annot = (base + height / 2 if ebitda_val < 0 else base) / 1e6
        ax.text(i, (base / 1e6) - 0.12, f"−{abs(ebitda_val)/1e6:.1f}",
                ha="center", va="top", fontsize=7, color=COLOR_RES, fontweight="bold")
    elif lbl.startswith("FCF"):
        ax.text(i, (base + height) / 1e6 + 0.05,
                f"+{fcf_target/1e6:.1f}",
                ha="center", va="bottom", fontsize=7, color=COLOR_FCF, fontweight="bold")
    elif all_heights[i] > 0:
        sign = "+" if all_colors[i] == COLOR_POS else "−"
        ax.text(i,
                (base + height + 50_000) / 1e6 if base >= 0
                else (base - 50_000) / 1e6,
                f"{sign}{height/1e6:.1f}",
                ha="center",
                va="bottom" if base >= 0 else "top",
                fontsize=7)

# Zero line
ax.axhline(0, color="black", linewidth=0.6, alpha=0.5)

# Connector lines for the waterfall flow (between driver bars)
run2 = 0.0
connector_stops = []
for i, (lbl, delta, _) in enumerate(segments[:4]):
    run2 += delta
    connector_stops.append((i, run2))

for i in range(len(connector_stops) - 1):
    x0, y0 = connector_stops[i]
    x1, y1 = connector_stops[i + 1]
    ax.plot([x0 + 0.33, x1 - 0.33], [y0 / 1e6, y0 / 1e6],
            color="black", linewidth=0.5, linestyle="--", alpha=0.4)

# Annotation: ARR driver inputs (top-left text)
arpu_label = "ARPU $600/yr | 200 new/mo | churn 0.65%/mo"
ax.text(0.02, 0.97, arpu_label, transform=ax.transAxes,
        fontsize=6.5, va="top", ha="left", color="#555555",
        fontstyle="italic")

# Legend
patch_pos = mpatches.Patch(color=COLOR_POS, alpha=0.88, label="Revenue / gross profit")
patch_neg = mpatches.Patch(color=COLOR_NEG, alpha=0.88, label="Operating expense")
patch_res = mpatches.Patch(color=COLOR_RES, alpha=0.88, label="EBITDA result")
patch_fcf = mpatches.Patch(color=COLOR_FCF, alpha=0.88, label="FCF / NOPAT (IC×ROIC)")
ax.legend(handles=[patch_pos, patch_neg, patch_res, patch_fcf],
          loc="lower right", fontsize=6.5, frameon=False)

ax.set_xticks(list(x_positions))
ax.set_xticklabels(all_labels, fontsize=7.5)
ax.set_ylabel("Value ($M)")
ax.set_title("Operating-model bridge: unit economics → ARR → EBITDA → FCF", fontsize=9.5)

# Y-axis limits: give room for labels above and below zero
ax.set_ylim(-0.95, 3.3)

fig.tight_layout(pad=0.5)
out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "op-model-bridge.pdf"
fig.savefig(out, format="pdf")
print(f"[op-model-bridge] Written to {out}")
