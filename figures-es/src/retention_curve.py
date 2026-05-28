"""
figures-es/src/retention_curve.py
Curvas de retención de cohorte para el capítulo de economía del cliente.
Salida: figures-es/retention_curve.pdf
Ejecutar: .venv/bin/python figures-es/src/retention_curve.py
      o:  ./tools/build-figures-es.sh retention_curve
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")  # no interactivo; establecer antes de importar pyplot
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

months = np.arange(0, 13)


def retention(r0: float, decay: float) -> np.ndarray:
    """Retención exponencial: r0 * exp(-decay * t)."""
    return r0 * np.exp(-decay * months)


saas = retention(1.0, 0.08)  # ~46% al mes 12
ecom = retention(1.0, 0.22)  # ~9%  al mes 12

fig, ax = plt.subplots()
ax.plot(months, saas * 100, label="SaaS / suscripción", marker="o", markersize=3)
ax.plot(months, ecom * 100, label="E-commerce (recompra)", marker="s", markersize=3, linestyle="--")
ax.fill_between(months, saas * 100, alpha=0.08)  # área ~ margen acumulado (integral LTV)

ax.set_xlabel("Mes desde la primera compra")
ax.set_ylabel("Clientes retenidos (%)")
ax.set_xlim(0, 12)
ax.set_ylim(0, 105)
ax.set_xticks(months)
ax.legend()
fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "retention_curve.pdf"
fig.savefig(out, format="pdf")
print(f"[retention_curve] Escrito en {out}")
