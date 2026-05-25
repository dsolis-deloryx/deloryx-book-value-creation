"""
figures/src/adstock_saturation.py
The media-mix saturation response (ch.10): cumulative conversions rise with spend but
saturate (Hill curve), so incremental return per dollar falls. Output: figures/adstock_saturation.pdf
Run: .venv/bin/python figures/src/adstock_saturation.py  (or ./tools/build-figures.sh adstock_saturation)
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

plt.style.use(str(pathlib.Path(__file__).parent / "booktheme.mplstyle"))

spend = np.linspace(0, 100, 400)          # weekly spend ($000s)
k, theta, scale = 1.6, 35.0, 1000.0
resp = scale * spend**k / (spend**k + theta**k)          # cumulative conversions (Hill)
marg = np.gradient(resp, spend)                           # marginal conversions per $000

fig, ax = plt.subplots()
ax.plot(spend, resp, color="#1A5276", label="Cumulative conversions")
ax.fill_between(spend, resp, where=(spend <= theta), color="#0E6655", alpha=0.08)
ax.axvline(theta, color="#935116", ls=":", lw=0.9)
ax.annotate("efficient region\n(before saturation)", xy=(theta, scale * 0.3),
            xytext=(theta - 4, scale * 0.62), fontsize=7, color="#935116", ha="right")

ax2 = ax.twinx()
ax2.plot(spend, marg, color="#7B241C", ls="--", lw=1.2, label="Marginal conv. / \\$")
ax2.set_ylabel("Marginal conversions per \\$000", color="#7B241C")
ax2.tick_params(axis="y", labelcolor="#7B241C")
ax2.set_ylim(0, marg.max() * 1.1)

ax.set_xlabel("Weekly media spend (\\$000s)")
ax.set_ylabel("Cumulative conversions")
ax.set_xlim(0, 100)
ax.set_ylim(0, scale * 1.02)

lines = [l for l in ax.get_lines() + ax2.get_lines() if not l.get_label().startswith("_")]
ax.legend(lines, [l.get_label() for l in lines], loc="center right", fontsize=7)
fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "adstock_saturation.pdf"
fig.savefig(out, format="pdf")
print(f"[adstock_saturation] Written to {out}")
