"""
figures/src/capm-sml.py
Security Market Line (SML) for the CAPM section (ch.16).
Shows expected return vs beta; marks the running SaaS at beta=1.4, re=11%.
Output: figures/capm-sml.pdf
Run:    .venv/bin/python figures/src/capm-sml.py
   or:  ./tools/build-figures.sh capm-sml
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# --- CAPM parameters (fact sheet) ---
rf = 0.04          # risk-free rate
erp = 0.05         # equity risk premium E(Rm) - Rf
beta_saas = 1.4    # running company beta
re_saas = rf + beta_saas * erp  # = 0.11

betas = np.linspace(0, 2.2, 200)
returns = rf + betas * erp

fig, ax = plt.subplots()

# SML line
ax.plot(betas, returns * 100, color="#1A5276", linewidth=1.8, label="Security Market Line")

# Market portfolio (beta=1)
ax.scatter([1.0], [(rf + erp) * 100], color="#0E6655", s=45, zorder=5)
ax.annotate(
    "Market (beta=1, re=9%)",
    xy=(1.0, (rf + erp) * 100),
    xytext=(0.5, 10.5),
    fontsize=7.5,
    arrowprops=dict(arrowstyle="-", color="#777777", lw=0.8),
    color="#0E6655",
)

# Risk-free asset (beta=0)
ax.scatter([0], [rf * 100], color="#6C3483", s=45, zorder=5)
ax.annotate(
    f"Risk-free (Rf={rf*100:.0f}%)",
    xy=(0, rf * 100),
    xytext=(0.12, 5.8),
    fontsize=7.5,
    color="#6C3483",
)

# Running SaaS
ax.scatter([beta_saas], [re_saas * 100], color="#7B241C", s=60, zorder=6, marker="D")
ax.annotate(
    f"SaaS (beta={beta_saas}, re={re_saas*100:.0f}%)",
    xy=(beta_saas, re_saas * 100),
    xytext=(1.55, 10.2),
    fontsize=7.5,
    arrowprops=dict(arrowstyle="-", color="#777777", lw=0.8),
    color="#7B241C",
    fontweight="bold",
)

# Dashed reference lines to axes
ax.plot([beta_saas, beta_saas], [0, re_saas * 100], color="#7B241C", linewidth=0.7,
        linestyle=":", alpha=0.6)
ax.plot([0, beta_saas], [re_saas * 100, re_saas * 100], color="#7B241C", linewidth=0.7,
        linestyle=":", alpha=0.6)

ax.set_xlabel("Beta (systematic risk)")
ax.set_ylabel("Expected return (%)")
ax.set_title("Capital Asset Pricing Model: Security Market Line", fontsize=10)
ax.set_xlim(-0.05, 2.2)
ax.set_ylim(0, 16)
ax.legend(fontsize=8, loc="upper left")

fig.tight_layout(pad=0.4)
out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "capm-sml.pdf"
fig.savefig(out, format="pdf")
print(f"[capm-sml] Written to {out}")
