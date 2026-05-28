# Glosario español — *Creación de Valor*

> **Audiencia:** lectores hispanohablantes de negocios — México, Colombia, Argentina, Chile, España. Español neutro (sin regionalismos; sin *vosotros*; sin "ordenador").
> **Política maestra:** mantener acrónimos del ecosistema *startup* en inglés; cursivar (\emph{}) los préstamos en su primera aparición por capítulo; nunca traducir claves de citas, etiquetas, ni referencias cruzadas.

---

## 1) Acrónimos que **permanecen en inglés** (sin cursiva)

Acrónimos técnicos universalmente usados en inglés en empresas y *startups* hispanohablantes. **NO traducir, NO cursivar.**

`CAC` · `LTV` · `MRR` · `ARR` · `NRR` · `CLV` · `KPI` · `OKR` · `ROAS` · `iROAS` · `CPA` · `CPL` · `CPC` · `CPM` · `eCPM` · `CTR` · `CVR` · `ROI` · `ROIC` · `WACC` · `NPV` · `IRR` · `DCF` · `FCF` · `EV` · `COGS` · `EBITDA` · `EBIT` · `GTM` · `SLA` · `NPS` · `DAU` · `MAU` · `BATNA` · `ZOPA` · `ELM` · `A/B` · `B2B` · `B2C` · `PLG` · `SaaS` · `ESG` · `GMA` · `NVT` · `RCT` · `OBHDP` · `JAP` · `JPSP` · `AMR` · `SOC 2`.

## 2) Préstamos del inglés que **permanecen en inglés** (cursiva en primera aparición por capítulo)

Palabras del léxico del ecosistema *startup*. La primera vez que aparezcan en un capítulo, ir en cursiva: `\emph{startup}`. Apariciones posteriores: sin cursiva.

`marketing` · `startup` · `churn` · `funnel` · `growth` · `pipeline` · `dashboard` · `cash flow` · `runway` · `burn` · `moat` · `hedge` · `spread` · `equity` · `insight` · `lead` (cliente potencial) · `coach` · `framework` · `pitch` · `deal` · `upsell` · `cross-sell` · `landing page` · `onboarding` · `retention` (cuando se refiere al concepto SaaS, no a la idea genérica) · `payback` · `breakpoint` · `tier` · `seed` · `Series A/B/C` · `cap table`.

## 3) Términos canónicos en español (traducir consistentemente)

| Inglés | Español canónico |
|---|---|
| rate | tasa |
| ratio | razón |
| revenue | ingreso |
| margin | margen |
| profit | beneficio o utilidad (según contexto) |
| investment | inversión |
| capital | capital |
| present value | valor presente |
| net present value | valor presente neto (en prosa) / `NPV` (en fórmulas y nombres) |
| discount rate | tasa de descuento |
| break-even | umbral de rentabilidad |
| entry barrier | barrera de entrada |
| supply | oferta |
| demand | demanda |
| leverage | apalancamiento |
| competitive advantage | ventaja competitiva |
| market share | cuota de mercado / participación de mercado |
| stakeholder | parte interesada |
| benchmark | referencia (en prosa); el *benchmark* (en términos técnicos en cursiva si conviene) |
| forecast | pronóstico |
| revenue stream | flujo de ingresos |
| willingness to pay | disposición a pagar |
| segment | segmento |
| targeting | segmentación / definición del público objetivo |
| positioning | posicionamiento |
| growth rate | tasa de crecimiento |
| switching cost | costo de cambio |
| network effect | efecto de red |
| meta-analysis | metaanálisis |
| field experiment | experimento de campo |
| effect size | tamaño del efecto |
| sample size | tamaño de muestra |
| odds ratio | razón de momios / odds ratio (mantener en inglés si la cita lo requiere) |
| trial-to-paid | conversión de prueba a pago |

## 4) Etiquetas de `admonition` (traducir literal en cada llamada)

`\begin{admonition}{Warning}` → `\begin{admonition}{Advertencia}`
`\begin{admonition}{Note}` → `\begin{admonition}{Nota}`
`\begin{admonition}{Contested}` → `\begin{admonition}{Controvertido}`

## 5) Encabezados en negrita del Capítulo 31 (catálogo de métricas)

| Inglés | Español |
|---|---|
| `\textbf{Formula.}` | `\textbf{Fórmula.}` |
| `\textbf{What each term means.}` | `\textbf{Qué significa cada término.}` |
| `\textbf{What it tracks.}` | `\textbf{Qué mide.}` |
| `\textbf{Why it matters.}` | `\textbf{Por qué importa.}` |
| `\textbf{Why it misleads.}` | `\textbf{Por qué engaña.}` (sólo métricas vanidad) |
| `\textbf{Benchmark.}` | `\textbf{Referencia.}` |
| `\textbf{Trap.}` | `\textbf{Trampa.}` |

## 6) Comillas, guiones, números

- **Comillas:** «...» como comillas externas; "..." para citas internas. Usar los caracteres Unicode directamente (LuaLaTeX + Pagella los renderiza nativamente).
- **Em-dashes:** mantener `---` (em-dash) en LaTeX; renderiza «—». Aceptable en español para incisos.
- **Números, decimales y moneda:** **idénticos a la edición en inglés** (separador de miles: coma; decimal: punto; moneda: `$1,250`). No cambiar a coma decimal.
- **Fechas:** `\today` se renderiza automáticamente en español («28 de mayo de 2026») gracias a babel-spanish — no escribir fechas a mano.

## 7) Cosas que **NUNCA se traducen**

- Cualquier clave de `\label{}` (todas son slugs estables en inglés: `ch:value-creation`, `eq:gordon`, `sec:influence-principles`).
- Cualquier clave de `\cref{}`, `\Cref{}`, `\textcite{}`, `\parencite{}`, `\cite{}`.
- Cualquier clave de `\input{}` (rutas y nombres de archivo).
- Macros: `\money{}`, `\num{}`, `\qty{}{}`, `\textcite{}`, `\parencite{}`, `\includegraphics{}`.
- Matemáticas: el contenido entre `\[` `\]`, `$ ... $`, `\begin{equation}...\end{equation}`, `\begin{align*}...\end{align*}`.
- Números bloqueados de la empresa de ejemplo (la SaaS B2B): ARPU \$50/mes (\$600/año), CM 42% = \$21/mes, CAC \$600, CLV \$3150, ARR \$4M, ~6700 clientes, *churn* mensual 0.65%, funnel 10000 → 800 → 200, WACC 11%, *g* 3%, NOPAT \$600k, IC \$3M, ROIC 20%, β 1.4.

## 8) Voz y registro

- Tercera persona del plural neutra para el lector ("ustedes" cuando se direccionan, o impersonal con "se"): *"el fundador puede hacer X"*, *"se observa que Y"*. **Nunca** *vosotros*.
- Registro: técnico-práctico, mismo nivel de formalidad que la edición en inglés (graduate-level practitioner). Frases cortas; cláusulas independientes preferidas.
- Anglicismos sin cursiva ya naturalizados: *email*, *internet*, *online*, *web*, *software*, *hardware*, *startup* (cursivar sólo en primera aparición por capítulo).
