# Guía de estilo — edición en español

Reglas operativas para los agentes traductores. Léase junto con `es-glossary.md`.

## Reglas inviolables (rompen el *build* si se incumplen)

1. **Etiquetas (`\label{}`) son slugs en inglés — NO TRADUCIR.** Las claves `ch:corporate-finance-core`, `sec:growing-perpetuity`, `eq:gordon`, etc. son estables entre ediciones y son la columna vertebral del sistema de referencias cruzadas. Si una etiqueta se traduce, todos los `\cref{}` del libro se rompen.
2. **Claves de citas (`\textcite{}`, `\parencite{}`, `\cite{}`) — NO TRADUCIR.** `bandura1997self`, `goldstein2008field`, etc. son claves de la bibliografía compartida `references.bib`. La bibliografía es trilingüe automáticamente: biblatex+babel-spanish traduce los strings genéricos («et al.», «vol.», «pp.», etc.).
3. **`\input{}` paths — NO TRADUCIR.** Los archivos en `chapters-es/` tienen el MISMO nombre que en `chapters/` (`19-corporate-finance-core.tex`).
4. **Macros y contenido matemático — NO TRADUCIR:** `\money{}`, `\num{}`, `\qty{}{}`, `\includegraphics{}`, todo lo que esté entre `$ ... $`, `\[ ... \]`, `\begin{equation} ... \end{equation}`, `\begin{align} ... \end{align}`, etc.
5. **Números bloqueados de la SaaS** (ARPU \$50, CAC \$600, CLV \$3150, ARR \$4M, etc.) — **idénticos** a la edición en inglés. Cualquier divergencia rompe la consistencia interna del libro.

## Qué SÍ se traduce

- **Prosa:** texto narrativo, explicativo, expositivo. La razón principal de existir de esta edición.
- **Títulos de capítulo y sección:** `\chapter{Foundations of Value}` → `\chapter{Fundamentos del valor}`. `\section{The Architecture of Influence}` → `\section{La arquitectura de la influencia}`. (Las etiquetas `\label{...}` justo después siguen en inglés.)
- **Subtítulos:** `\subsection{CAC --- Customer Acquisition Cost}` → `\subsection{CAC --- Costo de adquisición de clientes}`.
- **Etiquetas de `admonition`:** `\begin{admonition}{Warning}` → `\begin{admonition}{Advertencia}`.
- **Encabezados negrita en línea (ch.31):** `\textbf{Formula.}` → `\textbf{Fórmula.}` (ver glosario §5).
- **Captions opcionales de `example`:** `\begin{example}[CAC for the running SaaS]` → `\begin{example}[CAC para la SaaS de referencia]`.
- **Items de `\begin{description} \item[Label] ...`:** las etiquetas en negrita se traducen.
- **Contenido de listas** (`itemize`, `enumerate`).
- **Comentarios de LaTeX** que aporten contexto al lector futuro (líneas que empiezan con `%`).

## Convenciones tipográficas

- **Comillas:** «...» externas, "..." internas. Escribir los caracteres Unicode directamente.
  - **NO** usar las ligaduras TeX `` ``... '' `` (renderizan comillas inglesas).
- **Em-dashes:** `---` se conserva (renderiza «—»). Usar para incisos como en la edición en inglés.
- **Cursiva (`\emph{}`):** para préstamos del inglés en su primera aparición por capítulo (ver glosario §2). Para énfasis semántico se mantiene como en el original.
- **Negrita (`\textbf{}`):** sólo donde el original la usa (no añadir negrita decorativa).
- **Acrónimos:** sin cursiva, mayúsculas como en el glosario (`CAC`, `LTV`, `KPI`).

## Voz y registro

- **Persona:** tercera del plural neutra. *"el fundador hace X"*, *"se observa Y"*. Para instrucciones directas al lector usar *"considere"* (formal) o construcción impersonal *"conviene considerar"*. **Nunca** *vosotros*.
- **Tono:** técnico-práctico, *graduate-level*. Misma densidad y rigor del original. No simplificar; no dramatizar.
- **Conectores:** preferir frases cortas con conectores explícitos («por lo tanto», «en consecuencia», «no obstante»). Evitar oraciones de varios párrafos.
- **Anglicismos naturalizados** (no cursivar nunca): *internet*, *email*, *web*, *online*, *software*, *hardware*, *Excel*, *SaaS* (acrónimo).

## Errores frecuentes a evitar

- Traducir «marketing» a «mercadotecnia»: **NO**. Decisión confirmada: mantener *marketing* (cursiva en primera aparición).
- Cambiar separadores de miles/decimales: **NO**. Mantener `\$1,250` con coma como miles, punto como decimal.
- Traducir «churn» a «abandono»: **NO**. Mantener *churn* (cursiva en primera aparición). La métrica formal en ch.31 sigue siendo «Logo Churn» con esa grafía.
- Traducir el slug de una etiqueta: **NO**. `\label{ch:value-creation}` siempre — no `\label{cap:creacion-de-valor}`.
- Reordenar ecuaciones o cambiar variables matemáticas: **NO**. La prosa que rodea la ecuación se traduce; la ecuación misma es idéntica.
- Cambiar cifras de los ejemplos trabajados (CAC \$600, etc.): **NO**. Los números están bloqueados por la *fact sheet* de la empresa.

## Verificación rápida tras traducir un capítulo

Antes de entregar, el agente verifica con `grep`:

1. `grep -c '\\label{' chapters-es/XX-...tex` — debe coincidir con el conteo de la versión en inglés.
2. `grep -c 'parencite\|textcite' chapters-es/XX-...tex` — debe coincidir.
3. `grep "admonition\}{Warning\\|Note\\|Contested" chapters-es/XX-...tex` — debe devolver **0** líneas (todas traducidas).
4. `grep -E '\\money\{[0-9]+\}' chapters-es/XX-...tex` — los valores en `\money{}` deben ser idénticos a los del inglés.
5. `grep "ref\{\\|eqref\{" chapters-es/XX-...tex` (sin `\c` adelante) — debe devolver **0** líneas. Usar `\cref` siempre, nunca `\ref` ni `\eqref`.
