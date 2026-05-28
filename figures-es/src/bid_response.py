"""
figures-es/src/bid_response.py
La relación volumen–eficiencia para una estrategia de puja CPA objetivo (ch.09).
Las conversiones crecen y se saturan a medida que el objetivo de costo se relaja; por debajo del
piso de la fase de aprendizaje (~50 eventos/semana) la entrega se desestabiliza; por encima del
techo LTV:CAC, la economía unitaria falla. La ventana utilizable se encuentra entre ambos.
Salida: figures-es/bid_response.pdf
Ejecutar: .venv/bin/python figures-es/src/bid_response.py  (o ./tools/build-figures-es.sh bid_response)
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

plt.style.use(str(pathlib.Path(__file__).parent / "booktheme.mplstyle"))

# conversiones semanales como función saturante de la restricción CPA objetivo
cpa = np.linspace(100, 1400, 400)
K, h = 150.0, 900.0
conv = K * cpa / (cpa + h)

LEARN = 50            # piso de fase de aprendizaje: ~50 eventos / 7 días
CEIL = 1050           # techo LTV:CAC = 3 (LTV 3150 / 3)
cpa_floor = h * LEARN / (K - LEARN)   # CPA donde conv == 50  -> 450

fig, ax = plt.subplots()
ax.plot(cpa, conv, color="#1A5276", label="Conversiones semanales")

# ventana utilizable
ax.axvspan(cpa_floor, CEIL, color="#0E6655", alpha=0.08)
ax.axhline(LEARN, color="#7B241C", lw=0.9, ls="--")
ax.axvline(CEIL, color="#935116", lw=0.9, ls=":")

# punto de operación (CPA objetivo = $600)
op_cpa = 600
op_conv = K * op_cpa / (op_cpa + h)
ax.plot([op_cpa], [op_conv], "o", color="#4D4D4D", ms=5, zorder=5)

ax.annotate("piso de aprendizaje (~50/sem)", xy=(180, LEARN), xytext=(180, LEARN + 8),
            color="#7B241C", fontsize=7)
ax.annotate("techo LTV:CAC = 3", xy=(CEIL, 18), xytext=(CEIL - 40, 18),
            color="#935116", fontsize=7, ha="right", rotation=90, va="bottom")
ax.annotate("punto de operación\nobjetivo $600", xy=(op_cpa, op_conv),
            xytext=(op_cpa + 90, op_conv - 22), fontsize=7, color="#4D4D4D",
            arrowprops=dict(arrowstyle="-", color="#4D4D4D", lw=0.6))
ax.annotate("muy ajustado:\naprendizaje limitado", xy=(300, K * 300 / (300 + h)),
            xytext=(150, 92), fontsize=7, color="#7B241C")

ax.set_xlabel("Restricción CPA objetivo (\\$)")
ax.set_ylabel("Conversiones por semana")
ax.set_xlim(100, 1400)
ax.set_ylim(0, 105)
fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "bid_response.pdf"
fig.savefig(out, format="pdf")
print(f"[bid_response] Escrito en {out}")
