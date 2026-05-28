"""
figures-es/src/bass-diffusion.py
Modelo de Difusión de Bass: curvas S de adopción acumulada para el lanzamiento del nivel empresarial.
Parámetros: M=500 cuentas de mercado medio, p=0.02, q=0.3.
Salida: figures-es/bass-diffusion.pdf
Ejecutar: .venv/bin/python figures-es/src/bass-diffusion.py
      o:  ./tools/build-figures-es.sh bass-diffusion
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("pdf")  # no interactivo; establecer antes de importar pyplot
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# --- Parámetros del modelo (valores fijos del fact sheet) ---
M = 500          # mercado total direccionable (cuentas de mercado medio)
p = 0.02         # coeficiente de innovación (adopción saliente / intrínseca)
q = 0.3          # coeficiente de imitación (boca a boca / referencia entre pares)
T = 20           # meses a simular


def bass_cumulative(M: int, p: float, q: float, T: int) -> np.ndarray:
    """Simula el modelo Bass en tiempo discreto; devuelve array de adoptantes acumulados (longitud T+1)."""
    N = np.zeros(T + 1)
    for t in range(1, T + 1):
        new = (p + q * N[t - 1] / M) * (M - N[t - 1])
        N[t] = N[t - 1] + new
    return N


def innovator_only_cumulative(M: int, p: float, T: int) -> np.ndarray:
    """Difusión solo de innovadores (q=0): aproximación exponencial a M."""
    N = np.zeros(T + 1)
    for t in range(1, T + 1):
        new = p * (M - N[t - 1])
        N[t] = N[t - 1] + new
    return N


months = np.arange(0, T + 1)

cum_bass = bass_cumulative(M, p, q, T)
cum_inno = innovator_only_cumulative(M, p, T)

# Identificar el pico de nuevos adoptantes (primera diferencia del Bass acumulado)
new_adopters = np.diff(cum_bass)          # longitud T
peak_month = int(np.argmax(new_adopters)) + 1   # indexado desde 1

# --- Gráfico ---
fig, ax = plt.subplots()

ax.plot(months, cum_bass, label=f"Modelo Bass (p={p}, q={q})", marker="o", markersize=3)
ax.plot(months, cum_inno, label=f"Solo innovadores (p={p}, q=0)",
        linestyle="--", marker="", color="#0E6655")

ax.axvline(peak_month, color="#7B241C", linewidth=0.9, linestyle=":", alpha=0.8)
ax.text(peak_month + 0.3, cum_bass[peak_month] * 0.55,
        f"Pico de nuevos adoptantes\nmes {peak_month}",
        fontsize=7, color="#7B241C", va="center")

ax.axhline(M, color="#777777", linewidth=0.6, linestyle="--", alpha=0.6)
ax.text(T - 0.5, M + 8, f"M = {M}", fontsize=7, color="#777777", ha="right")

ax.set_xlabel("Mes desde el lanzamiento")
ax.set_ylabel("Adoptantes acumulados")
ax.set_xlim(0, T)
ax.set_ylim(0, M * 1.12)
ax.set_xticks(range(0, T + 1, 2))
ax.legend()
fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "bass-diffusion.pdf"
fig.savefig(out, format="pdf")
print(f"[bass-diffusion] Escrito en {out}")
