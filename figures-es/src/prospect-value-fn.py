"""
figures-es/src/prospect-value-fn.py
Función de valor de la teoría prospectiva (Kahneman y Tversky 1979), lambda=2.25, alpha=beta=0.88.
Salida: figures-es/prospect-value-fn.pdf
Ejecutar: .venv/bin/python figures-es/src/prospect-value-fn.py
      o:  ./tools/build-figures-es.sh prospect-value-fn
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# Parámetros (estimaciones medianas de Tversky y Kahneman 1992)
alpha = 0.88   # curvatura de ganancias
beta = 0.88    # curvatura de pérdidas
lam = 2.25     # coeficiente de aversión a las pérdidas


def value(x: np.ndarray) -> np.ndarray:
    """Función de valor de la teoría prospectiva v(x)."""
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

# Graficar ganancias (azul) y pérdidas (rojo/oscuro) con distintos colores del ciclo del tema
colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
c_gain = colors[0]   # vcblue
c_loss = colors[3]   # vcred/oscuro

ax.plot(x_gains, value(x_gains), color=c_gain, linewidth=1.8, label="Ganancias")
ax.plot(x_losses, value(x_losses), color=c_loss, linewidth=1.8, label="Pérdidas")

# Líneas de referencia
ax.axhline(0, color="black", linewidth=0.6, linestyle="-")
ax.axvline(0, color="black", linewidth=0.6, linestyle="-")

# Anotar asimetría: ganancia vs pérdida de igual magnitud
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

# Líneas horizontales punteadas para mostrar que la pérdida pesa más
v_gain = value(np.array([gain_x]))[0]
v_loss = value(np.array([loss_x]))[0]
ax.plot([gain_x, gain_x], [0, v_gain], color=c_gain, linewidth=0.8, linestyle="--")
ax.plot([loss_x, loss_x], [0, v_loss], color=c_loss, linewidth=0.8, linestyle="--")
ax.plot([0, gain_x], [v_gain, v_gain], color=c_gain, linewidth=0.8, linestyle="--")
ax.plot([loss_x, 0], [v_loss, v_loss], color=c_loss, linewidth=0.8, linestyle="--")

# Etiquetas para las intersecciones punteadas
ax.text(
    gain_x + 10, v_gain + 4, f"v(+300) = {v_gain:.0f}",
    fontsize=7, color=c_gain, va="bottom",
)
ax.text(
    loss_x - 10, v_loss - 4, f"v(-300) = {v_loss:.0f}",
    fontsize=7, color=c_loss, ha="right", va="top",
)

ax.set_xlabel("Resultado relativo al punto de referencia ($)")
ax.set_ylabel("Valor psicológico  v(x)")
ax.set_title(f"Función de valor de la teoría prospectiva  (lambda = {lam}, alpha = {alpha})", fontsize=9)
ax.legend()

# Anotación: razón de aversión a las pérdidas
ax.text(
    -580, 20,
    f"|v(-300)| / v(+300) = {abs(v_loss)/v_gain:.1f}x",
    fontsize=7, color="black",
)

fig.tight_layout(pad=0.4)
out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "prospect-value-fn.pdf"
fig.savefig(out, format="pdf")
print(f"[prospect-value-fn] Escrito en {out}")
