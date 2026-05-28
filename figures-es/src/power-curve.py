"""
figures-es/src/power-curve.py
Potencia estadística vs tamaño del efecto (incremento en tasa de conversión) para distintos tamaños de muestra.
Muestra curvas para n=100/200/550 por brazo; marca el punto n=550 requerido en delta=0.06.
Salida: figures-es/power-curve.pdf
Ejecutar: .venv/bin/python figures-es/src/power-curve.py
      o:  ./tools/build-figures-es.sh power-curve
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from scipy import stats  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# --- Parámetros ---
alpha = 0.05
z_a2 = stats.norm.ppf(1 - alpha / 2)   # 1.96
p_base = 0.25                            # tasa de conversión base (control)
sample_sizes = [100, 200, 550]           # brazos por grupo
labels = ["n = 100 por brazo", "n = 200 por brazo", "n = 550 por brazo"]
# posiciones de paleta: azul de decisión, teal, rojo
colors = ["#1A5276", "#0E6655", "#7B241C"]

# Tamaños de efecto: incremento absoluto sobre la base (delta = p_tratamiento - p_control)
deltas = np.linspace(0.005, 0.15, 300)

fig, ax = plt.subplots()

for n, label, color in zip(sample_sizes, labels, colors):
    power_vals = []
    for d in deltas:
        p_t = p_base + d
        # SE bajo H_a usando ambas proporciones
        se_ha = np.sqrt(p_base * (1 - p_base) / n + p_t * (1 - p_t) / n)
        # SE bajo H_0 usando proporción combinada
        p_pool = (p_base + p_t) / 2
        se_h0 = np.sqrt(2 * p_pool * (1 - p_pool) / n)
        # Efecto crítico bajo H_0
        critical_effect = z_a2 * se_h0
        # Potencia: P(rechazar H_0 | verdadero delta existe)
        z_power = (d - critical_effect) / se_ha
        power = stats.norm.cdf(z_power)
        power_vals.append(power)
    lw = 2.2 if n == 550 else 1.5
    ax.plot(deltas * 100, power_vals, color=color, linewidth=lw, label=label)

# Marcar el objetivo: delta=6pp, n=550
delta_target = 0.06
p_t_target = p_base + delta_target
n_target = 550
se_ha_t = np.sqrt(p_base * (1 - p_base) / n_target + p_t_target * (1 - p_t_target) / n_target)
p_pool_t = (p_base + p_t_target) / 2
se_h0_t = np.sqrt(2 * p_pool_t * (1 - p_pool_t) / n_target)
critical_effect_t = z_a2 * se_h0_t
z_power_t = (delta_target - critical_effect_t) / se_ha_t
power_at_target = stats.norm.cdf(z_power_t)

ax.scatter([delta_target * 100], [power_at_target],
           color="#7B241C", s=55, zorder=6, marker="D")
ax.annotate(
    f"n=550, delta=6pp\npotencia={power_at_target:.0%}",
    xy=(delta_target * 100, power_at_target),
    xytext=(8.5, 0.55),
    fontsize=7.5,
    arrowprops=dict(arrowstyle="-", color="#777777", lw=0.8),
    color="#7B241C",
    fontweight="bold",
)

# Línea de referencia de potencia 80%
ax.axhline(0.80, color="#4D4D4D", linewidth=0.8, linestyle="--", alpha=0.7,
           label="Objetivo de potencia 80%")

# Línea de referencia MDE 6pp
ax.axvline(delta_target * 100, color="#4D4D4D", linewidth=0.8, linestyle=":",
           alpha=0.7)

ax.set_xlabel("Tamaño del efecto: incremento absoluto sobre base del 25% (pp)")
ax.set_ylabel("Potencia estadística (1 - beta)")
ax.set_title("Potencia vs tamaño del efecto para pruebas A/B (alpha = 0.05, dos colas)", fontsize=10)
ax.set_xlim(0, 15)
ax.set_ylim(0, 1.02)
ax.yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(xmax=1, decimals=0))
ax.legend(fontsize=8, loc="lower right")

fig.tight_layout(pad=0.4)
out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "power-curve.pdf"
fig.savefig(out, format="pdf")
print(f"[power-curve] Escrito en {out}")
