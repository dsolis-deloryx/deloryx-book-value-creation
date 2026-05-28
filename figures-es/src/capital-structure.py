"""
figures-es/src/capital-structure.py
Teoría del equilibrio: valor de la empresa vs apalancamiento (D/V).
Muestra la línea base sin apalancamiento, VA(escudo fiscal), VA(costos de insolvencia) y el óptimo neto.
Salida: figures-es/capital-structure.pdf
Ejecutar: .venv/bin/python figures-es/src/capital-structure.py
      o:  ./tools/build-figures-es.sh capital-structure
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# --- Parámetros del modelo ---
dv = np.linspace(0, 0.95, 300)   # razón D/V

vu = 18.0                         # valor de la empresa sin apalancamiento ($M)  -- EV del fact sheet

# VA(escudo fiscal): lineal en D/V con tasa corporativa del 25%
tc = 0.25
pv_tax_shield = tc * dv * vu

# VA(costos de insolvencia): convexo en D/V; calibrado para que los costos dominen por encima de ~60% de apalancamiento
# Usar exponencial desplazada: c*(exp(k*(dv-d0)) - 1) para dv > d0, de lo contrario 0
k = 8.0
d0 = 0.25
pv_distress = np.where(
    dv > d0,
    0.6 * (np.exp(k * (dv - d0)) - 1),
    0.0,
)
# Limitar a vu para coherencia visual
pv_distress = np.minimum(pv_distress, vu)

# Valor de la empresa con apalancamiento (neto)
vl = vu + pv_tax_shield - pv_distress

# D/V óptimo: donde vl es máximo
i_opt = np.argmax(vl)
dv_opt = dv[i_opt]
vl_opt = vl[i_opt]

fig, ax = plt.subplots()

ax.axhline(vu, color="#777777", linewidth=1.0, linestyle="--", label=f"Valor sin apalancamiento $V_U$ = ${vu:.0f}M")
ax.plot(dv * 100, vl, color="#1A5276", linewidth=2.0, label="Valor de la empresa con apalancamiento $V_L$")
ax.fill_between(dv * 100, vu, vl, where=(vl >= vu), alpha=0.12, color="#0E6655",
                label="VA(escudo fiscal) neto de insolvencia")
ax.fill_between(dv * 100, vl, vu, where=(vl < vu), alpha=0.12, color="#7B241C")

# Marcar el óptimo
ax.scatter([dv_opt * 100], [vl_opt], color="#7B241C", s=60, zorder=6, marker="D")
ax.annotate(
    f"D/V óptimo = {dv_opt*100:.0f}%\n$V_L^*$ = ${vl_opt:.1f}M",
    xy=(dv_opt * 100, vl_opt),
    xytext=(dv_opt * 100 + 8, vl_opt + 0.4),
    fontsize=7.5,
    arrowprops=dict(arrowstyle="-", color="#777777", lw=0.8),
    color="#7B241C",
    fontweight="bold",
)

# Anotar posición SaaS (D/V ~ 0)
ax.annotate(
    "SaaS en etapa de growth\n(D/V cercano a 0)",
    xy=(2, vu + 0.05),
    xytext=(10, vu + 1.2),
    fontsize=7.5,
    arrowprops=dict(arrowstyle="-", color="#777777", lw=0.8),
    color="#4D4D4D",
)

ax.set_xlabel("Apalancamiento D/V (%)")
ax.set_ylabel("Valor de la empresa ($M)")
ax.set_title("Teoría del equilibrio: estructura de capital óptima", fontsize=10)
ax.set_xlim(0, 95)
ax.legend(fontsize=7.5, loc="lower left")

fig.tight_layout(pad=0.4)
out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "capital-structure.pdf"
fig.savefig(out, format="pdf")
print(f"[capital-structure] Escrito en {out}")
