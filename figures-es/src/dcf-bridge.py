"""
figures-es/src/dcf-bridge.py
Gráfico de cascada / puente DCF: VA de cada FCF del año explícito más VA del valor terminal
sumando al valor de la empresa. Ilustra que el valor terminal domina (~80% del EV).
Salida: figures-es/dcf-bridge.pdf
Ejecutar: .venv/bin/python figures-es/src/dcf-bridge.py
      o:  ./tools/build-figures-es.sh dcf-bridge
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# --- Números del fact sheet (SaaS B2B en ejecución) ---
wacc = 0.11
fcf_y1 = 600_000
growth_rates = [0.30, 0.30, 0.30, 0.10, 0.10]  # años 1-5

fcfs = [fcf_y1]
for g in growth_rates[1:]:
    fcfs.append(fcfs[-1] * (1 + g))

# VA de cada FCF del año explícito
pv_explicit = [fcf / (1 + wacc) ** (t + 1) for t, fcf in enumerate(fcfs)]

# Valor terminal: FCF año 5 * (1+g_estable) / (wacc - g_estable), descontado 5 años
g_steady = 0.03
tv = fcfs[-1] * (1 + g_steady) / (wacc - g_steady)
pv_tv = tv / (1 + wacc) ** 5

labels = ["FCF A1", "FCF A2", "FCF A3", "FCF A4", "FCF A5", "Valor\nterminal"]
values = pv_explicit + [pv_tv]

# Color: años explícitos usan violeta de derivación, terminal usa azul de decisión
colors = ["#6C3483"] * 5 + ["#1A5276"]

fig, ax = plt.subplots()

# Base acumulada para cascada apilada
bottoms = np.zeros(len(values))
for i, (val, color, label) in enumerate(zip(values, colors, labels)):
    ax.bar(i, val / 1e6, color=color, alpha=0.88, edgecolor="white", linewidth=0.4)
    ax.text(
        i,
        val / 1e6 + 0.15,
        f"{val/1e6:.1f}",
        ha="center",
        va="bottom",
        fontsize=7,
    )

# Línea horizontal en el EV total
total_ev = sum(values)
ax.axhline(total_ev / 1e6, color="#7B241C", linewidth=1.0, linestyle="--", alpha=0.7)
ax.text(
    len(values) - 0.5,
    total_ev / 1e6 + 0.3,
    f"EV = ${total_ev/1e6:.1f}M",
    ha="right",
    fontsize=8,
    color="#7B241C",
)

ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=8)
ax.set_ylabel("Valor presente ($M)")
ax.set_title("Puente DCF: FCF explícitos + valor terminal", fontsize=10)
ax.set_ylim(0, pv_tv / 1e6 * 1.18)

# Anotación de porcentaje en la barra de valor terminal
tv_pct = pv_tv / total_ev * 100
ax.text(
    5,
    pv_tv / 1e6 / 2,
    f"{tv_pct:.0f}% del EV",
    ha="center",
    va="center",
    fontsize=8,
    color="white",
    fontweight="bold",
)

fig.tight_layout(pad=0.4)
out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "dcf-bridge.pdf"
fig.savefig(out, format="pdf")
print(f"[dcf-bridge] Escrito en {out}")
