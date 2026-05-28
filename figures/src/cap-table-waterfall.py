"""
figures/src/cap-table-waterfall.py
Two-panel figure for ch.23 (Fundraising, Dilution & Runway).

Left panel  — Founder ownership across three rounds
              Pre-seed 100% -> Seed 75% -> Series A 62.5%

Right panel — Liquidation waterfall: investor vs. founder proceeds
              Series A: $5M invested, 25% ownership, 1x preference.
              Non-participating: max($5M, 25% * Exit)
              Participating:     $5M + 25% * (Exit - $5M)  [when Exit > $5M]
              Exit range: $5M to $30M.

Output: figures/cap-table-waterfall.pdf
Run:    .venv/bin/python figures/src/cap-table-waterfall.py
   or:  ./tools/build-figures.sh cap-table-waterfall
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np               # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# ── palette from booktheme ──────────────────────────────────────────────────
BLUE    = "#1A5276"   # decision blue
TEAL    = "#0E6655"   # intuition teal
VIOLET  = "#6C3483"   # derivation violet
RED     = "#7B241C"   # breaks red
ORANGE  = "#935116"   # trap orange
GRAY    = "#777777"   # deeper gray

# ═══════════════════════════════════════════════════════════════════════════
# LEFT PANEL: founder ownership across rounds
# ═══════════════════════════════════════════════════════════════════════════
rounds  = ["Pre-seed", "Seed", "Series A"]
founder = [100.0, 75.0, 62.5]

# Investor slices that make up the rest
# Pre-seed: no external investors
# Seed: seed investor 25%
# Series A: seed 20.8%, Series A 16.7%
seed_pct  = [0.0,  25.0,  20.8]
serA_pct  = [0.0,   0.0,  16.7]

x = np.arange(len(rounds))
bar_w = 0.5

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.09))

# stacked bar: founder (bottom), seed (middle), Series A (top)
b_founder = ax1.bar(x, founder, width=bar_w, color=BLUE,   label="Founder", alpha=0.88)
b_seed    = ax1.bar(x, seed_pct, width=bar_w, bottom=founder,
                    color=TEAL,   label="Seed investor", alpha=0.88)
b_serA    = ax1.bar(x, serA_pct, width=bar_w,
                    bottom=[f + s for f, s in zip(founder, seed_pct)],
                    color=VIOLET, label="Series A investor", alpha=0.88)

# percentage labels inside founder bars
for xi, pct in zip(x, founder):
    ax1.text(xi, pct / 2, f"{pct:.1f}%", ha="center", va="center",
             fontsize=8, color="white", fontweight="bold")

ax1.set_xticks(x)
ax1.set_xticklabels(rounds, fontsize=8)
ax1.set_ylabel("Ownership (%)")
ax1.set_ylim(0, 110)
ax1.set_title("Founder dilution across rounds", fontsize=10)
ax1.legend(fontsize=7, loc="upper right")

# ═══════════════════════════════════════════════════════════════════════════
# RIGHT PANEL: liquidation waterfall
# ═══════════════════════════════════════════════════════════════════════════
investment = 5_000_000
ownership  = 0.25       # 25%
pref       = investment  # 1x non-participating

exits = np.linspace(5_000_000, 30_000_000, 500)

# Non-participating: investor takes max(pref, p * Exit); founders get the rest
inv_nonpart  = np.maximum(pref, ownership * exits)
fnd_nonpart  = exits - inv_nonpart

# Participating: investor takes pref + p * (Exit - pref); founders get the rest
# Only meaningful when Exit >= pref (i.e. company can pay the preference)
inv_part = np.where(exits >= pref,
                    pref + ownership * (exits - pref),
                    exits)          # all proceeds go to investor if Exit < pref
fnd_part = exits - inv_part

exits_m = exits / 1e6   # convert to $M for axis

ax2.plot(exits_m, fnd_nonpart / 1e6,  color=BLUE,   linewidth=1.8,
         label="Founder (non-part.)")
ax2.plot(exits_m, fnd_part / 1e6,     color=BLUE,   linewidth=1.8,
         linestyle="--", label="Founder (participating)")
ax2.plot(exits_m, inv_nonpart / 1e6,  color=RED,    linewidth=1.8,
         label="Investor (non-part.)")
ax2.plot(exits_m, inv_part / 1e6,     color=RED,    linewidth=1.8,
         linestyle="--", label="Investor (participating)")

# Reference line at the $8M exit used in the worked example
ax2.axvline(8, color=GRAY, linewidth=0.8, linestyle=":")
ax2.text(8.1, 12, "$8M exit", fontsize=7, color=GRAY, va="top")

ax2.set_xlabel("Exit value ($M)")
ax2.set_ylabel("Proceeds ($M)")
ax2.set_title("Liquidation waterfall: 1x preference, 25% ownership", fontsize=10)
ax2.legend(fontsize=7, loc="upper left")
ax2.set_xlim(5, 30)
ax2.set_ylim(0, exits_m[-1])

fig.suptitle("Cap-table dilution & liquidation waterfall", fontsize=11, y=1.01)
fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "cap-table-waterfall.pdf"
fig.savefig(out, format="pdf", bbox_inches="tight")
print(f"[cap-table-waterfall] Written to {out}")
