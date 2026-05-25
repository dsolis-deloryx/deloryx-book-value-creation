"""
figures/src/retention_curve.py
Cohort retention curves for the customer-economics chapter.
Output: figures/retention_curve.pdf
Run:    .venv/bin/python figures/src/retention_curve.py
   or:  ./tools/build-figures.sh retention_curve
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")  # non-interactive; set before importing pyplot
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

months = np.arange(0, 13)


def retention(r0: float, decay: float) -> np.ndarray:
    """Exponential retention: r0 * exp(-decay * t)."""
    return r0 * np.exp(-decay * months)


saas = retention(1.0, 0.08)  # ~46% at month 12
ecom = retention(1.0, 0.22)  # ~9%  at month 12

fig, ax = plt.subplots()
ax.plot(months, saas * 100, label="SaaS / subscription", marker="o", markersize=3)
ax.plot(months, ecom * 100, label="E-commerce (repeat)", marker="s", markersize=3, linestyle="--")
ax.fill_between(months, saas * 100, alpha=0.08)  # area ~ cumulative margin (LTV integral)

ax.set_xlabel("Month since first purchase")
ax.set_ylabel("Retained customers (%)")
ax.set_xlim(0, 12)
ax.set_ylim(0, 105)
ax.set_xticks(months)
ax.legend()
fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "retention_curve.pdf"
fig.savefig(out, format="pdf")
print(f"[retention_curve] Written to {out}")
