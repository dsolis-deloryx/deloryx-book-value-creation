"""
figures-es/src/bullwhip.py
Efecto látigo: la varianza de la demanda se amplifica aguas arriba entre escalones (ch.17).
Salida: figures-es/bullwhip.pdf
Ejecutar: .venv/bin/python figures-es/src/bullwhip.py
      o:  ./tools/build-figures-es.sh bullwhip
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

# Demanda del cliente final: base 200/mes con ruido moderado (DE ~15)
demand_base = 200.0
demand = demand_base + rng.normal(0, 15, size=len(months))
# Inyectar el mes anómalo (mes 10 = índice 9): +50% de pico y vuelta
demand[9] = 300.0

# Media móvil de 3 meses de la demanda (señal suavizada)
def rolling_mean(x: np.ndarray, w: int) -> np.ndarray:
    out = np.full_like(x, np.nan)
    for i in range(w - 1, len(x)):
        out[i] = x[i - w + 1 : i + 1].mean()
    return out

smooth = rolling_mean(demand, 3)

# Pedidos aguas arriba: cada escalón amplifica — simular con política de orden hasta
# el nivel objetivo que agrega stock de seguridad de tiempo de entrega (amplificación ~2x).
# Pedidos[t] = max(0, demanda[t] + 0.8*(demanda[t]-demanda[t-1])) + ruido
orders = np.zeros_like(demand)
orders[0] = demand[0]
for t in range(1, len(months)):
    orders[t] = demand[t] + 1.6 * (demand[t] - demand[t - 1]) + rng.normal(0, 8)
orders = np.clip(orders, 80, None)

fig, axes = plt.subplots(2, 1, sharex=True, figsize=(5.0, 4.2))

# Panel superior: pedidos aguas arriba (alta varianza)
ax_top = axes[0]
ax_top.plot(months, orders, color="#1A5276", label="Pedidos aguas arriba", linewidth=1.5)
ax_top.axhline(demand_base, color="#777777", linewidth=0.8, linestyle=":")
ax_top.set_ylabel("Unidades pedidas")
ax_top.set_title("Efecto látigo: la varianza de la demanda se amplifica aguas arriba", fontsize=9)
ax_top.legend(loc="upper left")

# Panel inferior: demanda del cliente final (baja varianza) + señal suavizada
ax_bot = axes[1]
ax_bot.plot(months, demand, color="#0E6655", label="Demanda del cliente final", linewidth=1.5)
ax_bot.plot(months, smooth, color="#935116", linestyle="--",
            label="Media móvil 3 meses", linewidth=1.2)
ax_bot.axhline(demand_base, color="#777777", linewidth=0.8, linestyle=":")
ax_bot.set_xlabel("Mes")
ax_bot.set_ylabel("Unidades demandadas")
ax_bot.legend(loc="upper left")

# Anotar el mes del pico
ax_bot.annotate(
    "mes\nanómalo",
    xy=(10, demand[9]),
    xytext=(13, 270),
    fontsize=7,
    arrowprops=dict(arrowstyle="->", color="#7B241C", lw=0.8),
    color="#7B241C",
    fontfamily="serif",
)

fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "bullwhip.pdf"
fig.savefig(out, format="pdf")
print(f"[bullwhip] Escrito en {out}")
