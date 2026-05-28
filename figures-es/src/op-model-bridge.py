"""
figures-es/src/op-model-bridge.py
Gráfico de puente en cascada del modelo operativo: insumos de economía unitaria → ARR → EBITDA → FCF.
Refleja la estructura de dcf-bridge.py (mismo booktheme, mismas convenciones de estilo).

Lógica de cascada:
  Inicio (0) → +contribución ARR (pool de beneficio bruto)
             → −costo S&M
             → −costo R&D
             → −costo G&A
             = barra EBITDA
             → −Impuesto sobre EBITDA (solo si es positivo)
             = barra FCF (Año 1)

Valores fijos del fact sheet (SaaS en ejecución, base Año 1):
  ARR = $4,000,000  |  Margen bruto 70%  |  S&M 50% del ARR  |  R&D 25%  |  G&A 10%
  Margen EBITDA -15%  |  FCF ≈ NOPAT = $600,000 (ROIC 20% × CI $3,000,000)

Salida: figures-es/op-model-bridge.pdf
Ejecutar: .venv/bin/python figures-es/src/op-model-bridge.py
      o:  ./tools/build-figures-es.sh op-model-bridge
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.patches as mpatches  # noqa: E402

STYLE = pathlib.Path(__file__).parent / "booktheme.mplstyle"
plt.style.use(str(STYLE))

# ── Números del fact sheet ─────────────────────────────────────────────────────────
ARR        = 4_000_000
gm_rate    = 0.70          # margen bruto
sm_pct     = 0.50          # S&M como % del ARR
rd_pct     = 0.25          # R&D como % del ARR
ga_pct     = 0.10          # G&A como % del ARR  (85% opex total → -15% margen EBITDA)
tax_rate   = 0.30
fcf_target = 600_000       # NOPAT del fact sheet

gross_profit = ARR * gm_rate                    # 2,800,000
sm_cost      = ARR * sm_pct                     # 2,000,000
rd_cost      = ARR * rd_pct                     # 1,000,000
ga_cost      = ARR * ga_pct                     #   400,000
ebitda       = gross_profit - sm_cost - rd_cost - ga_cost   # -600,000

# Impuesto: sin escudo sobre pérdidas (conservador); el FCF del fact sheet anula el signo.
# El FCF del fact sheet = NOPAT = $600K asume que la empresa genera NOPAT sobre su base de
# capital invertido (ROIC 20% × CI $3M) — esto refleja el ARR base de INICIO de año que
# ya genera $600K de NOPAT, con opex invertido parcialmente para crecimiento. Mostramos la
# cascada de drivers y luego el FCF de $600K como una barra separada de «ancla del fact sheet».
# Para claridad del gráfico mostramos el EBITDA desde el desglose de drivers (-$600K al -15%)
# y luego el NOPAT/FCF de $600K por separado, enmarcado como ancla del fact sheet.

# ── Segmentos de la cascada ─────────────────────────────────────────────────────────
# Cada segmento: (etiqueta, delta_valor, es_positivo)
# Comenzando desde 0, subiendo hasta beneficio bruto, luego restando cada línea de opex,
# llegando al EBITDA, luego mostrando el FCF desde la identidad CI/ROIC.

segments = [
    ("Beneficio\nbruto",  gross_profit, True),   # +2.8M
    ("Costo\nS&M",       -sm_cost,     False),   # −2.0M
    ("Costo\nR&D",       -rd_cost,     False),   # −1.0M
    ("Costo\nG&A",       -ga_cost,     False),   # −0.4M
    # EBITDA es el total acumulado aquí = −0.6M (barra de resultado)
    ("FCF\n(NOPAT)",      fcf_target,  True),    # +0.6M mostrado como ancla separada del fact sheet
]

# Paleta: usar colores del booktheme
# Barras positivas: violeta de derivación #6C3483 (construcción operativa)
# Barras negativas: rojo de quiebra       #7B241C
# Barra FCF:        azul de decisión      #1A5276
COLOR_POS = "#6C3483"
COLOR_NEG = "#7B241C"
COLOR_FCF = "#1A5276"
COLOR_RES = "#4D4D4D"  # barra de resultado / referencia

labels = [s[0] for s in segments]
deltas = [s[1] for s in segments]

# Calcular totales acumulados para las bases de la cascada
bases   = []
running = 0.0
for i, (lbl, delta, is_pos) in enumerate(segments):
    if lbl.startswith("FCF"):
        # La barra FCF comienza desde cero para mostrarla como un output separado
        bases.append(0.0)
    else:
        if delta < 0:
            bases.append(running + delta)   # la barra comienza en la parte inferior del segmento negativo
        else:
            bases.append(running)
    running += delta if not lbl.startswith("FCF") else 0.0

# Dibujaremos EBITDA como barra de resultado entre las columnas de drivers y la columna FCF
# Insertar un espacio entre G&A y FCF, y agregar una barra de resultado EBITDA
all_labels = [s[0] for s in segments[:4]] + ["EBITDA\n(resultado)", "", "FCF\n(NOPAT)"]
all_bases  = []
all_heights= []
all_colors = []

run = 0.0
for lbl, delta, is_pos in segments[:4]:
    if delta < 0:
        all_bases.append(run + delta)
    else:
        all_bases.append(run)
    all_heights.append(abs(delta))
    all_colors.append(COLOR_POS if is_pos else COLOR_NEG)
    run += delta

# Barra de resultado EBITDA: de 0 a run (que es negativo)
ebitda_val = run  # = -600,000
all_bases.append(min(0.0, ebitda_val))
all_heights.append(abs(ebitda_val))
all_colors.append(COLOR_RES)

# Espaciador (invisible)
all_bases.append(0.0)
all_heights.append(0.0)
all_colors.append("none")

# Barra FCF/NOPAT: de 0 a fcf_target
all_bases.append(0.0)
all_heights.append(fcf_target)
all_colors.append(COLOR_FCF)

x_positions = range(len(all_labels))

fig, ax = plt.subplots()

for i, (base, height, color, lbl) in enumerate(zip(all_bases, all_heights, all_colors, all_labels)):
    if color == "none" or height == 0:
        continue
    ax.bar(i, height / 1e6, bottom=base / 1e6,
           color=color, alpha=0.88, edgecolor="white", linewidth=0.4, width=0.65)
    # Anotación de valor
    if lbl.startswith("EBITDA"):
        y_annot = (base + height / 2 if ebitda_val < 0 else base) / 1e6
        ax.text(i, (base / 1e6) - 0.12, f"−{abs(ebitda_val)/1e6:.1f}",
                ha="center", va="top", fontsize=7, color=COLOR_RES, fontweight="bold")
    elif lbl.startswith("FCF"):
        ax.text(i, (base + height) / 1e6 + 0.05,
                f"+{fcf_target/1e6:.1f}",
                ha="center", va="bottom", fontsize=7, color=COLOR_FCF, fontweight="bold")
    elif all_heights[i] > 0:
        sign = "+" if all_colors[i] == COLOR_POS else "−"
        ax.text(i,
                (base + height + 50_000) / 1e6 if base >= 0
                else (base - 50_000) / 1e6,
                f"{sign}{height/1e6:.1f}",
                ha="center",
                va="bottom" if base >= 0 else "top",
                fontsize=7)

# Línea de cero
ax.axhline(0, color="black", linewidth=0.6, alpha=0.5)

# Líneas de conector para el flujo de la cascada (entre barras de drivers)
run2 = 0.0
connector_stops = []
for i, (lbl, delta, _) in enumerate(segments[:4]):
    run2 += delta
    connector_stops.append((i, run2))

for i in range(len(connector_stops) - 1):
    x0, y0 = connector_stops[i]
    x1, y1 = connector_stops[i + 1]
    ax.plot([x0 + 0.33, x1 - 0.33], [y0 / 1e6, y0 / 1e6],
            color="black", linewidth=0.5, linestyle="--", alpha=0.4)

# Anotación: insumos de driver ARR (texto superior izquierdo)
arpu_label = "ARPU $600/año | 200 nuevos/mes | churn 0.65%/mes"
ax.text(0.02, 0.97, arpu_label, transform=ax.transAxes,
        fontsize=6.5, va="top", ha="left", color="#555555",
        fontstyle="italic")

# Leyenda
patch_pos = mpatches.Patch(color=COLOR_POS, alpha=0.88, label="Ingresos / beneficio bruto")
patch_neg = mpatches.Patch(color=COLOR_NEG, alpha=0.88, label="Gasto operativo")
patch_res = mpatches.Patch(color=COLOR_RES, alpha=0.88, label="Resultado EBITDA")
patch_fcf = mpatches.Patch(color=COLOR_FCF, alpha=0.88, label="FCF / NOPAT (CI×ROIC)")
ax.legend(handles=[patch_pos, patch_neg, patch_res, patch_fcf],
          loc="lower right", fontsize=6.5, frameon=False)

ax.set_xticks(list(x_positions))
ax.set_xticklabels(all_labels, fontsize=7.5)
ax.set_ylabel("Valor ($M)")
ax.set_title("Puente del modelo operativo: economía unitaria → ARR → EBITDA → FCF", fontsize=9.5)

# Límites del eje Y: dar espacio para etiquetas por encima y debajo de cero
ax.set_ylim(-0.95, 3.3)

fig.tight_layout(pad=0.5)
out = pathlib.Path(__file__).resolve().parents[2] / "figures-es" / "op-model-bridge.pdf"
fig.savefig(out, format="pdf")
print(f"[op-model-bridge] Escrito en {out}")
