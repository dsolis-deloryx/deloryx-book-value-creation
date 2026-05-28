"""
figures-es/src/disruption-scurve.py
Trayectorias de doble curva S: el dominante que se excede vs el disruptivo que cruza la demanda principal.
Salida: figures-es/disruption-scurve.pdf
Ejecutar: .venv/bin/python figures-es/src/disruption-scurve.py
      o:  ./tools/build-figures-es.sh disruption-scurve
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
    """Curva S logística: L / (1 + exp(-k*(t - t0)))."""
    return L / (1.0 + np.exp(-k * (t - t0)))


t = np.linspace(0, 10, 300)

# Dominante: ventaja inicial, meseta que supera el techo de demanda principal
incumbent = scurve(t, L=1.0, k=0.9, t0=3.0)

# Disruptivo: entra después y desde abajo, L más pequeño inicialmente pero mismo potencial de techo
disruptor = scurve(t, L=1.0, k=1.1, t0=7.0) * 0.95 + 0.02

# Techo de demanda principal (banda horizontal plana)
demand_ceiling = 0.70  # fracción del máximo eventual del dominante

fig, ax = plt.subplots()

ax.plot(t, incumbent, label="Trayectoria del dominante", linewidth=1.8)
ax.plot(t, disruptor, label="Trayectoria del disruptivo", linewidth=1.8, linestyle="--")
ax.axhline(demand_ceiling, color="#777777", linewidth=1.0, linestyle=":",
           label="Umbral de demanda principal")

# Anotar punto de cruce
crossing_idx = np.argmin(np.abs(disruptor - demand_ceiling))
crossing_t = t[crossing_idx]
ax.annotate(
    "Cruce de disrupción",
    xy=(crossing_t, demand_ceiling),
    xytext=(crossing_t + 0.6, demand_ceiling - 0.18),
    arrowprops=dict(arrowstyle="-|>", color="#7B241C", lw=0.9),
    fontsize=7,
    color="#7B241C",
    fontfamily="serif",
)

# Anotar exceso del dominante
ax.annotate(
    "El dominante se excede",
    xy=(5.5, incumbent[np.argmin(np.abs(t - 5.5))]),
    xytext=(5.7, 0.88),
    arrowprops=dict(arrowstyle="-|>", color="#1A5276", lw=0.8),
    fontsize=7,
    color="#1A5276",
    fontfamily="serif",
)

ax.set_xlabel("Tiempo")
ax.set_ylabel("Desempeño en la dimensión principal")
ax.set_xlim(0, 10)
ax.set_ylim(0, 1.05)
ax.set_xticks([])   # el tiempo es ordinal; sin valores de marca significativos
ax.set_yticks([0, demand_ceiling, 1.0])
ax.set_yticklabels(["0", "Umbral\nprincipal", "Máx"])
ax.legend(loc="upper left")

fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "disruption-scurve.pdf"
fig.savefig(out, format="pdf")
print(f"[disruption-scurve] Escrito en {out}")
