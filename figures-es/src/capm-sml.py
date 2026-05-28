"""
figures-es/src/capm-sml.py
Línea del mercado de valores (SML) para la sección CAPM (ch.16).
Muestra el retorno esperado vs beta; marca la SaaS en ejecución en beta=1.4, re=11%.
Salida: figures-es/capm-sml.pdf
Ejecutar: .venv/bin/python figures-es/src/capm-sml.py
      o:  ./tools/build-figures-es.sh capm-sml
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# --- Parámetros CAPM (fact sheet) ---
rf = 0.04          # tasa libre de riesgo
erp = 0.05         # prima de riesgo de capital E(Rm) - Rf
beta_saas = 1.4    # beta de la empresa en ejecución
re_saas = rf + beta_saas * erp  # = 0.11

betas = np.linspace(0, 2.2, 200)
returns = rf + betas * erp

fig, ax = plt.subplots()

# Línea SML
ax.plot(betas, returns * 100, color="#1A5276", linewidth=1.8, label="Línea del mercado de valores")

# Portafolio de mercado (beta=1)
ax.scatter([1.0], [(rf + erp) * 100], color="#0E6655", s=45, zorder=5)
ax.annotate(
    "Mercado (beta=1, re=9%)",
    xy=(1.0, (rf + erp) * 100),
    xytext=(0.5, 10.5),
    fontsize=7.5,
    arrowprops=dict(arrowstyle="-", color="#777777", lw=0.8),
    color="#0E6655",
)

# Activo libre de riesgo (beta=0)
ax.scatter([0], [rf * 100], color="#6C3483", s=45, zorder=5)
ax.annotate(
    f"Libre de riesgo (Rf={rf*100:.0f}%)",
    xy=(0, rf * 100),
    xytext=(0.12, 5.8),
    fontsize=7.5,
    color="#6C3483",
)

# SaaS en ejecución
ax.scatter([beta_saas], [re_saas * 100], color="#7B241C", s=60, zorder=6, marker="D")
ax.annotate(
    f"SaaS (beta={beta_saas}, re={re_saas*100:.0f}%)",
    xy=(beta_saas, re_saas * 100),
    xytext=(1.55, 10.2),
    fontsize=7.5,
    arrowprops=dict(arrowstyle="-", color="#777777", lw=0.8),
    color="#7B241C",
    fontweight="bold",
)

# Líneas de referencia punteadas hacia los ejes
ax.plot([beta_saas, beta_saas], [0, re_saas * 100], color="#7B241C", linewidth=0.7,
        linestyle=":", alpha=0.6)
ax.plot([0, beta_saas], [re_saas * 100, re_saas * 100], color="#7B241C", linewidth=0.7,
        linestyle=":", alpha=0.6)

ax.set_xlabel("Beta (riesgo sistemático)")
ax.set_ylabel("Retorno esperado (%)")
ax.set_title("Modelo de valoración de activos de capital: Línea del mercado de valores", fontsize=10)
ax.set_xlim(-0.05, 2.2)
ax.set_ylim(0, 16)
ax.legend(fontsize=8, loc="upper left")

fig.tight_layout(pad=0.4)
out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "capm-sml.pdf"
fig.savefig(out, format="pdf")
print(f"[capm-sml] Escrito en {out}")
