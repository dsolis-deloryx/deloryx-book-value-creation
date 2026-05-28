"""
figures/src/capital-structure.py
Trade-off theory: firm value vs leverage (D/V).
Shows unlevered baseline, PV(tax shield), PV(distress costs), and net optimal.
Output: figures/capital-structure.pdf
Run:    .venv/bin/python figures/src/capital-structure.py
   or:  ./tools/build-figures.sh capital-structure
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# --- Model parameters ---
dv = np.linspace(0, 0.95, 300)   # D/V ratio

vu = 18.0                         # unlevered firm value ($M)  -- fact sheet EV

# PV(tax shield): linear in D/V with corporate tax rate 25%
tc = 0.25
pv_tax_shield = tc * dv * vu

# PV(distress costs): convex in D/V; calibrated so costs dominate above ~60% leverage
# Use a shifted exponential: c*(exp(k*(dv-d0)) - 1) for dv > d0, else 0
k = 8.0
d0 = 0.25
pv_distress = np.where(
    dv > d0,
    0.6 * (np.exp(k * (dv - d0)) - 1),
    0.0,
)
# Cap at vu for visual coherence
pv_distress = np.minimum(pv_distress, vu)

# Net levered firm value
vl = vu + pv_tax_shield - pv_distress

# Optimal D/V: where vl is maximised
i_opt = np.argmax(vl)
dv_opt = dv[i_opt]
vl_opt = vl[i_opt]

fig, ax = plt.subplots()

ax.axhline(vu, color="#777777", linewidth=1.0, linestyle="--", label=f"Unlevered value $V_U$ = ${vu:.0f}M")
ax.plot(dv * 100, vl, color="#1A5276", linewidth=2.0, label="Levered firm value $V_L$")
ax.fill_between(dv * 100, vu, vl, where=(vl >= vu), alpha=0.12, color="#0E6655",
                label="PV(tax shield) net of distress")
ax.fill_between(dv * 100, vl, vu, where=(vl < vu), alpha=0.12, color="#7B241C")

# Mark optimum
ax.scatter([dv_opt * 100], [vl_opt], color="#7B241C", s=60, zorder=6, marker="D")
ax.annotate(
    f"Optimal D/V = {dv_opt*100:.0f}%\n$V_L^*$ = ${vl_opt:.1f}M",
    xy=(dv_opt * 100, vl_opt),
    xytext=(dv_opt * 100 + 8, vl_opt + 0.4),
    fontsize=7.5,
    arrowprops=dict(arrowstyle="-", color="#777777", lw=0.8),
    color="#7B241C",
    fontweight="bold",
)

# Annotate SaaS position (D/V ~ 0)
ax.annotate(
    "Growth-stage SaaS\n(D/V near 0)",
    xy=(2, vu + 0.05),
    xytext=(10, vu + 1.2),
    fontsize=7.5,
    arrowprops=dict(arrowstyle="-", color="#777777", lw=0.8),
    color="#4D4D4D",
)

ax.set_xlabel("Leverage D/V (%)")
ax.set_ylabel("Firm value ($M)")
ax.set_title("Trade-off theory: optimal capital structure", fontsize=10)
ax.set_xlim(0, 95)
ax.legend(fontsize=7.5, loc="lower left")

fig.tight_layout(pad=0.4)
out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "capital-structure.pdf"
fig.savefig(out, format="pdf")
print(f"[capital-structure] Written to {out}")
