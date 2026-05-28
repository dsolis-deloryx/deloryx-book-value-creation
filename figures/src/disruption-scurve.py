"""
figures/src/disruption-scurve.py
Dual S-curve trajectories: incumbent overshooting vs disruptor crossing mainstream demand.
Output: figures/disruption-scurve.pdf
Run:    .venv/bin/python figures/src/disruption-scurve.py
   or:  ./tools/build-figures.sh disruption-scurve
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))


def scurve(t: np.ndarray, L: float, k: float, t0: float) -> np.ndarray:
    """Logistic S-curve: L / (1 + exp(-k*(t - t0)))."""
    return L / (1.0 + np.exp(-k * (t - t0)))


t = np.linspace(0, 10, 300)

# Incumbent: early lead, plateau overshoots mainstream demand ceiling
incumbent = scurve(t, L=1.0, k=0.9, t0=3.0)

# Disruptor: enters later and from below, smaller L initially but same ceiling potential
disruptor = scurve(t, L=1.0, k=1.1, t0=7.0) * 0.95 + 0.02

# Mainstream demand ceiling (flat horizontal band)
demand_ceiling = 0.70  # fraction of incumbent's eventual max

fig, ax = plt.subplots()

ax.plot(t, incumbent, label="Incumbent trajectory", linewidth=1.8)
ax.plot(t, disruptor, label="Disruptor trajectory", linewidth=1.8, linestyle="--")
ax.axhline(demand_ceiling, color="#777777", linewidth=1.0, linestyle=":",
           label="Mainstream demand threshold")

# Annotate crossing point
crossing_idx = np.argmin(np.abs(disruptor - demand_ceiling))
crossing_t = t[crossing_idx]
ax.annotate(
    "Disruption crossing",
    xy=(crossing_t, demand_ceiling),
    xytext=(crossing_t + 0.6, demand_ceiling - 0.18),
    arrowprops=dict(arrowstyle="-|>", color="#7B241C", lw=0.9),
    fontsize=7,
    color="#7B241C",
    fontfamily="serif",
)

# Annotate overshoot
ax.annotate(
    "Incumbent overshoots",
    xy=(5.5, incumbent[np.argmin(np.abs(t - 5.5))]),
    xytext=(5.7, 0.88),
    arrowprops=dict(arrowstyle="-|>", color="#1A5276", lw=0.8),
    fontsize=7,
    color="#1A5276",
    fontfamily="serif",
)

ax.set_xlabel("Time")
ax.set_ylabel("Performance on mainstream dimension")
ax.set_xlim(0, 10)
ax.set_ylim(0, 1.05)
ax.set_xticks([])   # time is ordinal; no meaningful tick values
ax.set_yticks([0, demand_ceiling, 1.0])
ax.set_yticklabels(["0", "Mainstream\nthreshold", "Max"])
ax.legend(loc="upper left")

fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "disruption-scurve.pdf"
fig.savefig(out, format="pdf")
print(f"[disruption-scurve] Written to {out}")
