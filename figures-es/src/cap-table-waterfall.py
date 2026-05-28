"""
figures-es/src/cap-table-waterfall.py
Figura de dos paneles para ch.23 (Financiamiento, Dilución y Runway).

Panel izquierdo  — Participación del fundador en tres rondas
                   Pre-semilla 100% -> Semilla 75% -> Serie A 62.5%

Panel derecho    — Cascada de liquidación: recursos del inversor vs el fundador
                   Serie A: $5M invertidos, 25% de participación, preferencia 1x.
                   No participante: max($5M, 25% * Salida)
                   Participante:    $5M + 25% * (Salida - $5M)  [cuando Salida > $5M]
                   Rango de salida: $5M a $30M.

Salida: figures-es/cap-table-waterfall.pdf
Ejecutar: .venv/bin/python figures-es/src/cap-table-waterfall.py
      o:  ./tools/build-figures-es.sh cap-table-waterfall
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np               # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# ── paleta del booktheme ──────────────────────────────────────────────────
BLUE    = "#1A5276"   # azul de decisión
TEAL    = "#0E6655"   # verde azulado de intuición
VIOLET  = "#6C3483"   # violeta de derivación
RED     = "#7B241C"   # rojo de quiebra
ORANGE  = "#935116"   # naranja de trampa
GRAY    = "#777777"   # gris profundo

# ═══════════════════════════════════════════════════════════════════════════
# PANEL IZQUIERDO: participación del fundador por ronda
# ═══════════════════════════════════════════════════════════════════════════
rounds  = ["Pre-semilla", "Semilla", "Serie A"]
founder = [100.0, 75.0, 62.5]

# Porciones del inversor que completan el resto
# Pre-semilla: sin inversores externos
# Semilla: inversor semilla 25%
# Serie A: semilla 20.8%, Serie A 16.7%
seed_pct  = [0.0,  25.0,  20.8]
serA_pct  = [0.0,   0.0,  16.7]

x = np.arange(len(rounds))
bar_w = 0.5

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.09))

# barra apilada: fundador (abajo), semilla (medio), Serie A (arriba)
b_founder = ax1.bar(x, founder, width=bar_w, color=BLUE,   label="Fundador", alpha=0.88)
b_seed    = ax1.bar(x, seed_pct, width=bar_w, bottom=founder,
                    color=TEAL,   label="Inversor semilla", alpha=0.88)
b_serA    = ax1.bar(x, serA_pct, width=bar_w,
                    bottom=[f + s for f, s in zip(founder, seed_pct)],
                    color=VIOLET, label="Inversor Serie A", alpha=0.88)

# etiquetas de porcentaje dentro de las barras del fundador
for xi, pct in zip(x, founder):
    ax1.text(xi, pct / 2, f"{pct:.1f}%", ha="center", va="center",
             fontsize=8, color="white", fontweight="bold")

ax1.set_xticks(x)
ax1.set_xticklabels(rounds, fontsize=8)
ax1.set_ylabel("Participación (%)")
ax1.set_ylim(0, 110)
ax1.set_title("Dilución del fundador por ronda", fontsize=10)
ax1.legend(fontsize=7, loc="upper right")

# ═══════════════════════════════════════════════════════════════════════════
# PANEL DERECHO: cascada de liquidación
# ═══════════════════════════════════════════════════════════════════════════
investment = 5_000_000
ownership  = 0.25       # 25%
pref       = investment  # preferencia 1x no participante

exits = np.linspace(5_000_000, 30_000_000, 500)

# No participante: inversor recibe max(pref, p * Salida); fundadores reciben el resto
inv_nonpart  = np.maximum(pref, ownership * exits)
fnd_nonpart  = exits - inv_nonpart

# Participante: inversor recibe pref + p * (Salida - pref); fundadores reciben el resto
# Solo es válido cuando Salida >= pref (la empresa puede pagar la preferencia)
inv_part = np.where(exits >= pref,
                    pref + ownership * (exits - pref),
                    exits)          # todos los recursos van al inversor si Salida < pref
fnd_part = exits - inv_part

exits_m = exits / 1e6   # convertir a $M para el eje

ax2.plot(exits_m, fnd_nonpart / 1e6,  color=BLUE,   linewidth=1.8,
         label="Fundador (no part.)")
ax2.plot(exits_m, fnd_part / 1e6,     color=BLUE,   linewidth=1.8,
         linestyle="--", label="Fundador (participante)")
ax2.plot(exits_m, inv_nonpart / 1e6,  color=RED,    linewidth=1.8,
         label="Inversor (no part.)")
ax2.plot(exits_m, inv_part / 1e6,     color=RED,    linewidth=1.8,
         linestyle="--", label="Inversor (participante)")

# Línea de referencia en la salida de $8M usada en el ejemplo
ax2.axvline(8, color=GRAY, linewidth=0.8, linestyle=":")
ax2.text(8.1, 12, "salida $8M", fontsize=7, color=GRAY, va="top")

ax2.set_xlabel("Valor de salida ($M)")
ax2.set_ylabel("Recursos ($M)")
ax2.set_title("Cascada de liquidación: preferencia 1x, 25% de participación", fontsize=10)
ax2.legend(fontsize=7, loc="upper left")
ax2.set_xlim(5, 30)
ax2.set_ylim(0, exits_m[-1])

fig.suptitle("Dilución en cap table y cascada de liquidación", fontsize=11, y=1.01)
fig.tight_layout(pad=0.4)

out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "cap-table-waterfall.pdf"
fig.savefig(out, format="pdf", bbox_inches="tight")
print(f"[cap-table-waterfall] Escrito en {out}")
