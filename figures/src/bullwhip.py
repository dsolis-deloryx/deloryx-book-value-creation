"""
figures/src/bullwhip.py
Bullwhip effect: demand variance amplifies upstream across echelons (ch.17).
Output: figures/bullwhip.pdf
Run:    .venv/bin/python figures/src/bullwhip.py
   or:  ./tools/build-figures.sh bullwhip
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

rng = np.random.default_rng(42)

months = np.arange(1, 25)

# End-customer demand: baseline 200/month with modest noise (SD ~15)
demand_base = 200.0
demand = demand_base + rng.normal(0, 15, size=len(months))
# Inject the anomalous month (month 10 = index 9): +50% spike then back
demand[9] = 300.0

# Rolling 3-month average of demand (smoothed signal)
def rolling_mean(x: np.ndarray, w: int) -> np.ndarray:
    out = np.full_like(x, np.nan)
    for i in range(w - 1, len(x)):
        out[i] = x[i - w + 1 : i + 1].mean()
    return out

smooth = rolling_mean(demand, 3)

# Upstream orders: each echelon amplifies — simulate by convolving demand with a
# simple order-up-to policy that adds a lead-time safety stock (amplification ~2x).
# Orders[t] = max(0, demand[t] + 0.8*(demand[t]-demand[t-1])) + noise
orders = np.zeros_like(demand)
orders[0] = demand[0]
for t in range(1, len(months)):
    orders[t] = demand[t] + 1.6 * (demand[t] - demand[t - 1]) + rng.normal(0, 8)
orders = np.clip(orders, 80, None)

fig, axes = plt.subplots(2, 1, sharex=True, figsize=(5.0, 4.2))

# Top panel: upstream orders (high variance)
ax_top = axes[0]
ax_top.plot(months, orders, color="#1A5276", label="Upstream orders", linewidth=1.5)
ax_top.axhline(demand_base, color="#777777", linewidth=0.8, linestyle=":")
ax_top.set_ylabel("Units ordered")
ax_top.set_title("Bullwhip Effect: demand variance amplifies upstream", fontsize=9)
ax_top.legend(loc="upper left")

# Bottom panel: end-customer demand (low variance) + smoothed signal
ax_bot = axes[1]
ax_bot.plot(months, demand, color="#0E6655", label="End-customer demand", linewidth=1.5)
ax_bot.plot(months, smooth, color="#935116", linestyle="--",
            label="3-month rolling avg", linewidth=1.2)
ax_bot.axhline(demand_base, color="#777777", linewidth=0.8, linestyle=":")
ax_bot.set_xlabel("Month")
ax_bot.set_ylabel("Units demanded")
ax_bot.legend(loc="upper left")

# Annotate the spike month
ax_bot.annotate(
    "anomalous\nmonth",
    xy=(10, demand[9]),
    xytext=(13, 270),
    fontsize=7,
    arrowprops=dict(arrowstyle="->", color="#7B241C", lw=0.8),
    color="#7B241C",
    fontfamily="serif",
)

fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures" / "bullwhip.pdf"
fig.savefig(out, format="pdf")
print(f"[bullwhip] Written to {out}")
