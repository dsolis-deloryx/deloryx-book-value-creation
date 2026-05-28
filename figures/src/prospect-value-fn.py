"""
figures/src/prospect-value-fn.py
Prospect theory value function (Kahneman & Tversky 1979), lambda=2.25, alpha=beta=0.88.
Output: figures/prospect-value-fn.pdf
Run:    .venv/bin/python figures/src/prospect-value-fn.py
   or:  ./tools/build-figures.sh prospect-value-fn
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# Parameters (Tversky & Kahneman 1992 median estimates)
alpha = 0.88   # gain curvature
beta = 0.88    # loss curvature
lam = 2.25     # loss aversion coefficient


def value(x: np.ndarray) -> np.ndarray:
    """Prospect theory value function v(x)."""
    out = np.empty_like(x, dtype=float)
    gains = x >= 0
    out[gains] = x[gains] ** alpha
    out[~gains] = -lam * ((-x[~gains]) ** beta)
    return out


x_gains = np.linspace(0, 600, 400)
x_losses = np.linspace(-600, 0, 400)
x_all = np.concatenate([x_losses, x_gains])
v_all = value(x_all)

fig, ax = plt.subplots()

# Plot gains (blue) and losses (red/dark) with different colours from the theme cycle
colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
c_gain = colors[0]   # vcblue
c_loss = colors[3]   # vcred/dark

ax.plot(x_gains, value(x_gains), color=c_gain, linewidth=1.8, label="Gains")
ax.plot(x_losses, value(x_losses), color=c_loss, linewidth=1.8, label="Losses")

# Reference lines
ax.axhline(0, color="black", linewidth=0.6, linestyle="-")
ax.axvline(0, color="black", linewidth=0.6, linestyle="-")

# Annotate asymmetry: equal magnitude gain vs loss
gain_x = 300
loss_x = -300
ax.annotate(
    "",
    xy=(gain_x, value(np.array([gain_x]))[0]),
    xytext=(0, 0),
    arrowprops=dict(arrowstyle="->", color=c_gain, lw=1.0),
)
ax.annotate(
    "",
    xy=(loss_x, value(np.array([loss_x]))[0]),
    xytext=(0, 0),
    arrowprops=dict(arrowstyle="->", color=c_loss, lw=1.0),
)

# Dashed horizontal lines to show loss looms larger
v_gain = value(np.array([gain_x]))[0]
v_loss = value(np.array([loss_x]))[0]
ax.plot([gain_x, gain_x], [0, v_gain], color=c_gain, linewidth=0.8, linestyle="--")
ax.plot([loss_x, loss_x], [0, v_loss], color=c_loss, linewidth=0.8, linestyle="--")
ax.plot([0, gain_x], [v_gain, v_gain], color=c_gain, linewidth=0.8, linestyle="--")
ax.plot([loss_x, 0], [v_loss, v_loss], color=c_loss, linewidth=0.8, linestyle="--")

# Labels for the dashed intercepts
ax.text(
    gain_x + 10, v_gain + 4, f"v(+300) = {v_gain:.0f}",
    fontsize=7, color=c_gain, va="bottom",
)
ax.text(
    loss_x - 10, v_loss - 4, f"v(-300) = {v_loss:.0f}",
    fontsize=7, color=c_loss, ha="right", va="top",
)

ax.set_xlabel("Outcome relative to reference point ($)")
ax.set_ylabel("Psychological value  v(x)")
ax.set_title(f"Prospect theory value function  (lambda = {lam}, alpha = {alpha})", fontsize=9)
ax.legend()

# Annotation: loss aversion ratio
ax.text(
    -580, 20,
    f"|v(-300)| / v(+300) = {abs(v_loss)/v_gain:.1f}x",
    fontsize=7, color="black",
)

fig.tight_layout(pad=0.4)
out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "prospect-value-fn.pdf"
fig.savefig(out, format="pdf")
print(f"[prospect-value-fn] Written to {out}")
