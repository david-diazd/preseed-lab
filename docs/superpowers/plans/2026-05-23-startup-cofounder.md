# Startup-Cofounder Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear 26 agentes markdown en `Startup-Cofounder/agents/` que leen los documentos del founder desde `inputs/` y producen versiones mejoradas en `outputs/`.

**Architecture:** Cada agente es un archivo `.md` con frontmatter estructurado, un workflow de 3 fases (leer inputs/, diagnosticar, producir output) y frameworks del dominio. 25 agentes se adaptan de `shawnpang/startup-founder-skills` (MIT); 1 (`financial-model`) se crea desde cero. La adaptación clave: reemplazar el workflow "entrevistar al founder desde cero" por "leer y mejorar sus documentos existentes".

**Tech Stack:** Markdown, Claude Code @-references, gh CLI para fetchear fuentes

---

## Patrón de adaptación (referencia para todos los agentes)

Todos los agentes adaptados siguen este transform desde la fuente:

**Frontmatter nuevo:**
```yaml
---
name: <nombre>
description: <trigger phrases en español>
domain: <fundraising|product|marketing|legal-ops>
reads: [inputs/]
outputs: [outputs/<nombre>.md]
---
```

**Sección añadida después de "Cuándo usar":**
```markdown
## Qué leer en inputs/
[Lista específica de tipos de archivos relevantes para este agente]
Si no hay nada disponible, pregunta: "[pregunta específica al founder]"
```

**Step 1 del workflow siempre es:**
```markdown
1. **Leer inputs/** — Escanea todos los archivos en inputs/. Extrae [lista específica]. Si falta algo crítico, pregunta antes de continuar.
```

**Los frameworks y best practices se copian verbatim de la fuente.** El output se escribe siempre en `outputs/<nombre>.md`.

---

## Fase 0 — Scaffolding

### Task 0: Crear estructura de directorios y README

**Files:**
- Create: `Startup-Cofounder/inputs/.gitkeep`
- Create: `Startup-Cofounder/outputs/.gitkeep`
- Create: `Startup-Cofounder/agents/fundraising/.gitkeep`
- Create: `Startup-Cofounder/agents/product/.gitkeep`
- Create: `Startup-Cofounder/agents/marketing/.gitkeep`
- Create: `Startup-Cofounder/agents/legal-ops/.gitkeep`
- Create: `Startup-Cofounder/README.md`

- [ ] **Step 1: Crear directorios**

```bash
mkdir -p Startup-Cofounder/inputs
mkdir -p Startup-Cofounder/outputs
mkdir -p Startup-Cofounder/agents/fundraising
mkdir -p Startup-Cofounder/agents/product
mkdir -p Startup-Cofounder/agents/marketing
mkdir -p Startup-Cofounder/agents/legal-ops
touch Startup-Cofounder/inputs/.gitkeep
touch Startup-Cofounder/outputs/.gitkeep
touch Startup-Cofounder/agents/fundraising/.gitkeep
touch Startup-Cofounder/agents/product/.gitkeep
touch Startup-Cofounder/agents/marketing/.gitkeep
touch Startup-Cofounder/agents/legal-ops/.gitkeep
```

- [ ] **Step 2: Escribir README.md**

Escribir `Startup-Cofounder/README.md` con este contenido exacto:

```markdown
# Startup-Cofounder

Suite de 26 agentes especializados para ayudar a founders a mejorar su documentación de startup usando Claude Code.

## Cómo funciona

1. Pon tus documentos en `inputs/` — Excel, Word, PDF, PPT, CSV, lo que tengas
2. Invoca el agente con `@agents/<dominio>/<nombre>.md`
3. El agente lee tus docs, los diagnostica y produce la versión mejorada en `outputs/`

No necesitas rellenar ningún formulario previo. El agente extrae el contexto directamente de tus documentos.

## Agentes disponibles

### Fundraising
| Agente | Cuándo usarlo |
|---|---|
| `@agents/fundraising/pitch-deck.md` | Crear o mejorar tu pitch deck slide a slide |
| `@agents/fundraising/financial-model.md` | Revisar P&L, unit economics y proyecciones |
| `@agents/fundraising/data-room.md` | Preparar data room para due diligence |
| `@agents/fundraising/investor-research.md` | Construir lista de inversores tiered |
| `@agents/fundraising/fundraising-email.md` | Cold outreach, follow-ups e investor updates |
| `@agents/fundraising/accelerator-application.md` | Essays para YC, Techstars y otros programas |
| `@agents/fundraising/board-update.md` | Updates mensuales/trimestrales a inversores |
| `@agents/fundraising/market-research.md` | TAM/SAM/SOM con metodología rigurosa |
| `@agents/fundraising/competitive-analysis.md` | Landscape competitivo y posicionamiento |

### Producto & Estrategia
| Agente | Cuándo usarlo |
|---|---|
| `@agents/product/prd-writing.md` | PRD estructurado de features |
| `@agents/product/mvp-scoping.md` | Definir scope v1 vs defer |
| `@agents/product/roadmap-planning.md` | Roadmap priorizado con dependencias |
| `@agents/product/user-research-synthesis.md` | Sintetizar entrevistas en insights |
| `@agents/product/feedback-synthesis.md` | Patrones de feedback en acciones |

### Marketing & Crecimiento
| Agente | Cuándo usarlo |
|---|---|
| `@agents/marketing/content-strategy.md` | Estrategia de contenido con calendario |
| `@agents/marketing/launch-strategy.md` | Plan de lanzamiento con canales y timing |
| `@agents/marketing/landing-page.md` | Copy de landing page optimizado |
| `@agents/marketing/cold-outreach.md` | Secuencias de outreach B2B |
| `@agents/marketing/sales-script.md` | Script de demo y manejo de objeciones |
| `@agents/marketing/social-content.md` | Posts para LinkedIn/Twitter del founder |
| `@agents/marketing/seo-technical.md` | Auditoría SEO y plan de keywords |

### Legal & Operaciones
| Agente | Cuándo usarlo |
|---|---|
| `@agents/legal-ops/contract-review.md` | Revisar contratos con red flags |
| `@agents/legal-ops/terms-of-service.md` | ToS completo para SaaS/app |
| `@agents/legal-ops/privacy-policy.md` | Política de privacidad GDPR-ready |
| `@agents/legal-ops/process-docs.md` | SOPs y documentación de procesos |
| `@agents/legal-ops/proposal-generation.md` | Propuestas comerciales y SOWs |

## Flujo recomendado para fundraising

1. `@agents/fundraising/pitch-deck.md` — mejora el deck
2. `@agents/fundraising/financial-model.md` — valida los números
3. `@agents/fundraising/market-research.md` — refuerza el slide de mercado
4. `@agents/fundraising/competitive-analysis.md` — refuerza el slide de competencia
5. `@agents/fundraising/data-room.md` — prepara el data room
6. `@agents/fundraising/investor-research.md` — construye la lista de targets
7. `@agents/fundraising/fundraising-email.md` — escribe los emails de outreach

## inputs/ — qué puedes poner

Cualquier documento que tengas: PDF de tu deck, Excel con P&L, Word con descripción del producto, CSV de métricas, notas de entrevistas de usuarios, contratos, etc. Cuanto más pongas, mejor el output.
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/
git commit -m "feat: scaffold Startup-Cofounder structure and README"
```

---

## Fase 1 — Fundraising (9 agentes)

### Task 1: pitch-deck.md

**Files:**
- Create: `Startup-Cofounder/agents/fundraising/pitch-deck.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/pitch-deck/SKILL.md \
  --jq '.content' | base64 -d > /tmp/pitch-deck-source.md
cat /tmp/pitch-deck-source.md
```

Lee la fuente para extraer: los 10-12 slides del framework, las narrative arc rules y los tips de investor lens. Los usarás en el paso siguiente.

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/fundraising/pitch-deck.md`:

```markdown
---
name: pitch-deck
description: Cuando el founder quiere crear, revisar o reestructurar su pitch deck. Activa con "deck", "pitch", "presentación inversores", "slides", "narrativa de la empresa".
domain: fundraising
reads: [inputs/]
outputs: [outputs/pitch-deck.md]
---

# Pitch Deck Agent

## Cuándo usar
- El founder tiene un deck existente y quiere mejorarlo slide a slide
- El founder quiere crear un deck desde cero para su ronda
- El founder quiere estructurar mejor la narrativa para inversores

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Presentaciones existentes (.pptx, .pdf, .key, .ppt)
- Documentos con descripción de la empresa o one-pager
- Datos de tracción (Excel, CSV con métricas)
- Modelo financiero o proyecciones
- Análisis de mercado o competencia

Si no hay nada en inputs/, pregunta: "¿Tienes algún borrador de deck, one-pager o descripción de tu startup que pueda revisar?"

## Workflow

1. **Leer inputs/** — Escanea todos los archivos en inputs/. Extrae:
   - One-liner de la empresa
   - Problema que resuelve y a quién
   - Solución y producto actual
   - Mercado objetivo y tamaño si está disponible
   - Modelo de negocio y pricing
   - Métricas de tracción actuales (MRR, usuarios, clientes)
   - Información del equipo fundador
   - Ronda de fundraising objetivo (importe y uso de fondos)
   Si falta algún dato crítico para un slide clave, pregunta antes de continuar.

2. **Diagnosticar** — Evalúa el material existente contra el framework de 10-12 slides:
   - ¿Qué slides faltan o están incompletos?
   - ¿La narrativa conecta problema → solución → mercado → tracción?
   - ¿Hay métricas de vanidad en vez de métricas que importan a inversores?
   - ¿El ask es específico con milestones concretos?

3. **Producir output** — Escribe `outputs/pitch-deck.md` con el deck completo reescrito, slide a slide. Cada slide incluye título, mensaje clave, contenido, sugerencia visual y la pregunta del inversor que responde.

## Output Format

`outputs/pitch-deck.md` — un H3 por slide:

```
### Slide N: [Título]
**Mensaje clave:** [Lo que el inversor debe recordar]
**Contenido:**
- ...
**Sugerencia visual:** [Qué gráfico, imagen o screenshot va aquí]
**Pregunta del inversor que responde:** [La pregunta implícita en la mente del VC]
```

## Frameworks & Best Practices

[COPIAR VERBATIM las secciones "The 10-12 Slide Framework", "Narrative Arc Rules" y cualquier otra sección de frameworks de /tmp/pitch-deck-source.md]
```

- [ ] **Step 3: Verificar estructura**

```bash
head -20 Startup-Cofounder/agents/fundraising/pitch-deck.md
```

Confirma que el archivo empieza con frontmatter `---`, tiene sección "Qué leer en inputs/", y el workflow tiene 3 pasos numerados.

- [ ] **Step 4: Commit**

```bash
git add Startup-Cofounder/agents/fundraising/pitch-deck.md
git commit -m "feat: add pitch-deck agent (fundraising)"
```

---

### Task 2: financial-model.md (agente custom, no existe en el repo fuente)

**Files:**
- Create: `Startup-Cofounder/agents/fundraising/financial-model.md`

- [ ] **Step 1: Escribir archivo desde cero**

Escribir `Startup-Cofounder/agents/fundraising/financial-model.md`:

```markdown
---
name: financial-model
description: Cuando el founder quiere revisar o crear su modelo financiero. Activa con "P&L", "modelo financiero", "proyecciones", "unit economics", "burn rate", "runway", "CAC", "LTV", "gross margin".
domain: fundraising
reads: [inputs/]
outputs: [outputs/financial-model.md]
---

# Financial Model Agent

## Cuándo usar
- El founder tiene un Excel con P&L y quiere que lo revise un experto
- El founder necesita calcular sus unit economics correctamente
- El founder necesita proyecciones a 18-36 meses para presentar a inversores
- El founder no sabe cuánto runway le queda

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Modelo financiero o P&L en Excel (.xlsx, .csv)
- Datos de facturación o ingresos por período
- Información de clientes (número, contratos, precios)
- Datos de costes (equipo, infraestructura, marketing, otros)
- Extractos bancarios o saldo actual
- Slides con información financiera del deck

Si no hay nada financiero en inputs/, pregunta: "¿Tienes algún Excel con ingresos, costes o datos de clientes? Con el saldo del banco y el gasto mensual también puedo empezar."

## Workflow

1. **Leer inputs/** — Extrae todos los datos financieros disponibles:
   - Ingresos actuales (MRR/ARR o ingresos por proyecto si no es recurrente)
   - Costes fijos y variables (equipo, infraestructura, marketing, otros)
   - Número de clientes activos y precio medio
   - Churn mensual si está disponible
   - Saldo en banco y burn rate mensual actual
   Si faltan datos clave, especifica exactamente qué necesitas y por qué es necesario para el modelo.

2. **Diagnosticar** — Evalúa la salud financiera y la calidad del modelo existente:
   - ¿Los unit economics son sostenibles? (LTV debe ser >3x CAC)
   - ¿El gross margin es adecuado para el tipo de negocio?
   - ¿Las proyecciones tienen supuestos explícitos o son "hockey stick" sin base?
   - ¿Cuánto runway hay con el burn actual?
   - ¿Qué métricas faltan o están mal calculadas?

3. **Producir output** — Escribe `outputs/financial-model.md` con el modelo completo incluyendo snapshot actual, unit economics calculados, proyecciones 18-36 meses con supuestos explícitos, y tres escenarios.

## Output Format

`outputs/financial-model.md`:

```
## Snapshot financiero actual
- MRR/ARR: $X
- Clientes activos: N
- Precio medio: $X/mes
- Gross Margin: X%
- Burn rate mensual: $X
- Saldo en banco: $X
- Runway: X meses

## Unit Economics
| Métrica | Valor actual | Benchmark saludable |
|---|---|---|
| CAC | $X | Depende del canal |
| LTV | $X | >3x CAC |
| LTV/CAC ratio | X | >3x |
| Payback Period | X meses | <12 meses (SaaS B2B) |
| Gross Margin | X% | >60% (SaaS) |
| Churn mensual | X% | <2% (SaaS B2B) |
| NRR | X% | >100% ideal |

## Proyecciones 18-36 meses
| Mes | MRR | Clientes | Burn mensual | Runway restante |
|---|---|---|---|---|
| M+1 | ... | ... | ... | ... |
[continuar hasta M+36]

## Supuestos del modelo
- Crecimiento de clientes: X% mensual — basado en: [histórico / benchmark sector]
- CAC: $X — basado en: [gasto marketing / nuevos clientes]
- Churn: X% — basado en: [histórico / benchmark]
- Headcount plan: [descripción contrataciones previstas]
- Inversión prevista: $X en [fecha] — impacto en burn: [descripción]

## Escenarios
- **Base:** [supuestos] → runway de X meses, break-even en mes Y
- **Optimista (+30% crecimiento):** [supuestos] → runway de X meses
- **Pesimista (-30% crecimiento):** [supuestos] → runway de X meses, acción requerida en mes Z

## Diagnóstico y mejoras recomendadas
[Lista de problemas encontrados en el modelo actual]
[Métricas que faltan o están mal calculadas]
[Recomendaciones específicas con ejemplos]
```

## Frameworks & Best Practices

### Fórmulas de unit economics

**CAC (Customer Acquisition Cost):**
`CAC = Gasto total en ventas y marketing del período / Nuevos clientes adquiridos en el período`

**LTV para SaaS recurrente:**
`LTV = (MRR por cliente × Gross Margin%) / Churn mensual`

**LTV/CAC:** El ratio más importante para inversores. <2x es señal de alerta. >3x es saludable. >5x puede indicar que no estás invirtiendo suficiente en crecimiento.

**Payback Period:**
`Payback = CAC / (MRR por cliente × Gross Margin%)`
<12 meses es saludable para SaaS B2B. <6 meses es excelente.

**NRR (Net Revenue Retention):**
`NRR = (MRR inicio + Expansión - Contracción - Churned MRR) / MRR inicio × 100`
>100% significa que creces aunque no adquieras ningún cliente nuevo. Es el indicador más poderoso de product-market fit en SaaS.

### Gross Margin por modelo de negocio
- SaaS puro (sin soporte intensivo): 70-85%
- SaaS con servicios profesionales: 50-65%
- Marketplace: 40-60%
- D2C / e-commerce: 30-50%
- Hardware + software: 20-40%

### Supuestos que siempre deben ser explícitos
Para cada línea de proyección documenta:
1. En qué dato histórico se basa (o qué benchmark del sector si no hay histórico)
2. Qué tiene que ocurrir para que sea verdad
3. Qué pasa si ese supuesto falla (escenario pesimista)

### Red flags en modelos financieros para inversores
- **Hockey stick sin driver:** Si las proyecciones se disparan, debe haber un evento concreto (campaña, contratación de ventas, nuevo canal)
- **CAC omitido o mezclado:** El sueldo de los fundadores no es CAC a menos que dediquen el 100% a adquisición
- **Gross margin que asume escala futura:** Las proyecciones deben mostrar el margen actual, no el marginal futuro
- **Runway calculado con burn fijo:** El burn aumenta a medida que creces — el modelo debe reflejarlo
- **Precisión falsa:** Proyecciones a 3 años con 2 decimales. Los inversores saben que es ficción, pero los supuestos sí importan
```

- [ ] **Step 2: Verificar estructura**

```bash
head -15 Startup-Cofounder/agents/fundraising/financial-model.md
grep -n "## " Startup-Cofounder/agents/fundraising/financial-model.md
```

Confirma: frontmatter correcto, 6 secciones principales presentes (Cuándo usar, Qué leer, Workflow, Output Format, Frameworks).

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/fundraising/financial-model.md
git commit -m "feat: add financial-model agent (custom, fundraising)"
```

---

### Task 3: data-room.md

**Files:**
- Create: `Startup-Cofounder/agents/fundraising/data-room.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/data-room/SKILL.md \
  --jq '.content' | base64 -d > /tmp/data-room-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/fundraising/data-room.md` con este contenido (copiar frameworks verbatim de la fuente):

```markdown
---
name: data-room
description: Cuando el founder quiere preparar el data room para due diligence. Activa con "data room", "due diligence", "DD", "documentos para inversores", "qué documentos necesito".
domain: fundraising
reads: [inputs/]
outputs: [outputs/data-room.md]
---

# Data Room Agent

## Cuándo usar
- Un inversor ha pedido materiales adicionales tras el pitch
- El founder quiere preparar el data room de forma proactiva antes de iniciar outreach
- El founder ha recibido un term sheet y necesita preparar due diligence confirmatorio

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Documentos corporativos (estatutos, actas de junta, pactos de socios)
- Cap table (Carta, Excel, o cualquier documento de equity)
- Documentos financieros (P&L, balance, cash flow, extractos bancarios)
- Contratos con clientes o proveedores clave
- Documentos legales (SAFEs, convertibles, contratos de empleados)
- Pitch deck o one-pager

Si inputs/ está vacío, pregunta: "¿En qué fase de due diligence estás — preparación previa, post-primera reunión, o post-term sheet?"

## Workflow

1. **Leer inputs/** — Escanea todos los archivos en inputs/. Identifica qué documentos corporativos, financieros y legales ya existen. Detecta cuáles están desactualizados (financieros >1 mes, 409A >12 meses) o incompletos.

2. **Diagnosticar** — Evalúa el estado de cada categoría del master DD checklist. Clasifica cada ítem como: Existe ✓ / Necesita actualización ⚠️ / Falta ✗ / No aplica —.

3. **Producir output** — Escribe `outputs/data-room.md` con el checklist completo por categoría, estado de cada documento, estructura de carpetas recomendada y drafts o templates para los documentos que faltan.

## Output Format

`outputs/data-room.md`:

```
## Data Room Checklist — [Nombre empresa] — [Ronda]

### 1. Documentos corporativos
- [✓/⚠️/✗/—] Escritura de constitución — [estado]
- [✓/⚠️/✗/—] Estatutos sociales — [estado]
...

### 2. Cap table & equity
...

[Una sección por cada categoría del master checklist]

## Estructura de carpetas recomendada
[Árbol de carpetas para organizar el data room]

## Documentos que faltan — drafts/templates
[Para cada documento marcado como ✗, incluir un template o borrador]
```

## Frameworks & Best Practices

[COPIAR VERBATIM el "Master Due Diligence Checklist" y cualquier otra sección de frameworks de /tmp/data-room-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/fundraising/data-room.md
git commit -m "feat: add data-room agent (fundraising)"
```

---

### Task 4: investor-research.md

**Files:**
- Create: `Startup-Cofounder/agents/fundraising/investor-research.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/investor-research/SKILL.md \
  --jq '.content' | base64 -d > /tmp/investor-research-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/fundraising/investor-research.md`:

```markdown
---
name: investor-research
description: Cuando el founder quiere identificar y priorizar inversores para su ronda. Activa con "lista de inversores", "a quién pitchar", "buscar VCs", "inversores para mi startup", "angel investors".
domain: fundraising
reads: [inputs/]
outputs: [outputs/investor-research.md]
---

# Investor Research Agent

## Cuándo usar
- El founder va a empezar a fundraisear y necesita una lista de targets
- El founder tiene una lista de inversores y quiere cualificarlos o priorizarlos
- El founder quiere entender si un fondo específico encaja con su startup

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (para extraer stage, sector, modelo de negocio, geografía)
- Modelo financiero (para extraer el importe de la ronda y runway)
- Descripción de la empresa o one-pager
- Lista previa de inversores (si el founder ya tiene una)

Si inputs/ está vacío, pregunta: "¿Cuál es el stage de tu startup, en qué sector estás y cuánto estás buscando levantar?"

## Workflow

1. **Leer inputs/** — Extrae de los documentos disponibles: stage, sector/vertical, modelo de negocio, geografía, importe de la ronda objetivo, inversores actuales y cualquier inversor ya en conversación.

2. **Diagnosticar** — Define los criterios de filtrado: stage match, sector focus, tamaño de cheque, geografía y conflictos de portfolio. Identifica cualquier inversor de la lista existente del founder que no cumpla los criterios.

3. **Producir output** — Escribe `outputs/investor-research.md` con la lista tiered de inversores (T1/T2/T3), warm paths para los T1, y sección de conflictos excluidos.

## Output Format

`outputs/investor-research.md`:

```
## Lista de inversores — [Nombre empresa] — [Ronda]

### Tier 1 — Alta prioridad
| Firma | Partner | Stage | Sector | Cheque típico | Fondo reciente | Conflicto | Warm path |
|---|---|---|---|---|---|---|---|

### Tier 2 — Buena adecuación
[misma tabla]

### Tier 3 — Backfill
[misma tabla]

## Conflictos excluidos
[Firma — razón del conflicto]

## Gaps de investigación
[Lo que no se ha podido verificar y necesita input del founder]
```

## Frameworks & Best Practices

[COPIAR VERBATIM "The 7-Point Filter", "Tiering Framework" y cualquier otra sección de frameworks de /tmp/investor-research-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/fundraising/investor-research.md
git commit -m "feat: add investor-research agent (fundraising)"
```

---

### Task 5: fundraising-email.md

**Files:**
- Create: `Startup-Cofounder/agents/fundraising/fundraising-email.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/fundraising-email/SKILL.md \
  --jq '.content' | base64 -d > /tmp/fundraising-email-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/fundraising/fundraising-email.md`:

```markdown
---
name: fundraising-email
description: Cuando el founder necesita escribir un email a un inversor. Activa con "email a inversor", "cold outreach", "intro email", "follow up con VC", "investor update", "forwardable email".
domain: fundraising
reads: [inputs/]
outputs: [outputs/fundraising-email.md]
---

# Fundraising Email Agent

## Cuándo usar
- El founder necesita escribir un cold outreach a un inversor
- El founder quiere redactar un "forwardable email" para que alguien le haga una intro
- El founder necesita un follow-up después de una reunión con un inversor
- El founder quiere escribir su investor update mensual

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (para extraer one-liner, métricas clave, round details)
- Modelo financiero (para la métrica de tracción más impactante)
- Lista de inversores (para personalizar el outreach)
- Emails anteriores o notas de reuniones con el inversor en cuestión

Si inputs/ está vacío, pregunta: "¿Qué tipo de email necesitas — cold outreach, intro request, follow-up o investor update? ¿Y a quién va dirigido?"

## Workflow

1. **Leer inputs/** — Extrae: one-liner de la empresa, la métrica de tracción más fuerte (la que hace lean-in), el round details (importe, uso de fondos), y cualquier contexto específico del inversor destinatario.

2. **Diagnosticar** — Determina el tipo de email (cold, warm intro, follow-up, update). Evalúa si hay personalización suficiente para el inversor específico — un email genérico no funciona.

3. **Producir output** — Escribe `outputs/fundraising-email.md` con el asunto y el cuerpo del email, listo para copiar y pegar.

## Output Format

`outputs/fundraising-email.md`:

```
**Para:** [Nombre del inversor]
**Asunto:** [Subject line]

[Cuerpo del email]

---
**Notas de personalización:**
- [Por qué este inversor específicamente]
- [Qué cambiar si se envía a otros]
```

## Frameworks & Best Practices

[COPIAR VERBATIM "The Five Email Types" (Cold Outreach, Warm Intro Request, Post-Meeting Follow-Up, Monthly Investor Update, Round Closing) y cualquier otra sección de frameworks de /tmp/fundraising-email-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/fundraising/fundraising-email.md
git commit -m "feat: add fundraising-email agent (fundraising)"
```

---

### Task 6: accelerator-application.md

**Files:**
- Create: `Startup-Cofounder/agents/fundraising/accelerator-application.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/accelerator-application/SKILL.md \
  --jq '.content' | base64 -d > /tmp/accelerator-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/fundraising/accelerator-application.md`:

```markdown
---
name: accelerator-application
description: Cuando el founder quiere aplicar a aceleradoras o programas de incubación. Activa con "YC", "Y Combinator", "Techstars", "aceleradora", "aplicar a programa", "application essays".
domain: fundraising
reads: [inputs/]
outputs: [outputs/accelerator-application.md]
---

# Accelerator Application Agent

## Cuándo usar
- El founder quiere aplicar a Y Combinator, Techstars u otras aceleradoras
- El founder quiere identificar qué aceleradoras encajan mejor con su startup
- El founder necesita ayuda con los essays y respuestas de la aplicación
- El founder se prepara para una entrevista de aceleradora

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (narrativa, problema, solución, tracción, equipo)
- Modelo financiero o métricas de tracción
- Aplicaciones anteriores (para mejorar respuestas ya usadas)
- CVs o bios del equipo fundador
- Descripción del producto o one-pager

Si inputs/ está vacío, pregunta: "¿A qué aceleradora estás aplicando y en qué stage estás?"

## Workflow

1. **Leer inputs/** — Extrae: stage, sector, traction metrics, team backgrounds, product description, y por qué este equipo es el adecuado para este mercado (founder-market fit).

2. **Diagnosticar** — Identifica la aceleradora objetivo y sus preferencias específicas (YC valora velocidad de crecimiento y founders técnicos; Techstars valora coachability; etc.). Evalúa el material existente contra lo que esa aceleradora busca.

3. **Producir output** — Escribe `outputs/accelerator-application.md` con respuestas completas a las preguntas estándar de la aplicación, adaptadas al programa específico.

## Output Format

`outputs/accelerator-application.md`:

```
## Aplicación a [Nombre programa] — [Empresa]

### Preguntas y respuestas

**¿Qué hace tu empresa en una frase?**
[Respuesta ≤15 palabras]

**¿Qué problema resuelve y para quién?**
[Respuesta 2-3 párrafos]

**¿Qué tracción tienes?**
[Métricas específicas con contexto]

**¿Por qué ahora?**
[Respuesta sobre timing del mercado]

**¿Por qué es este el equipo adecuado?**
[Founder-market fit específico]

[... resto de preguntas específicas del programa]

## Script para el video de aplicación (si requerido)
[Guión de 60-90 segundos: problema → solución → tracción → equipo → ask]

## Preparación para entrevista
[Preguntas más frecuentes con respuestas preparadas]
```

## Frameworks & Best Practices

[COPIAR VERBATIM el directorio de aceleradoras y los frameworks de respuesta de /tmp/accelerator-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/fundraising/accelerator-application.md
git commit -m "feat: add accelerator-application agent (fundraising)"
```

---

### Task 7: board-update.md

**Files:**
- Create: `Startup-Cofounder/agents/fundraising/board-update.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/board-update/SKILL.md \
  --jq '.content' | base64 -d > /tmp/board-update-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/fundraising/board-update.md`:

```markdown
---
name: board-update
description: Cuando el founder necesita escribir un update a inversores o preparar una reunión de board. Activa con "investor update", "board update", "actualización mensual", "update trimestral", "reunión de consejo".
domain: fundraising
reads: [inputs/]
outputs: [outputs/board-update.md]
---

# Board Update Agent

## Cuándo usar
- El founder necesita escribir su update mensual o trimestral a inversores
- El founder se prepara para una reunión de board
- El founder necesita comunicar malas noticias a inversores de forma efectiva

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Modelo financiero o datos de métricas del período (MRR, burn, runway)
- Actualizaciones anteriores (para mantener formato consistente)
- Notas sobre hitos del período (lanzamientos, contrataciones, eventos)
- Pipeline de ventas o datos de crecimiento

Si inputs/ está vacío, pregunta: "¿Es un update mensual por email o un deck para reunión de board? ¿Qué período cubre?"

## Workflow

1. **Leer inputs/** — Extrae métricas clave del período: MRR/ARR, burn rate, runway, headcount, hitos alcanzados, problemas relevantes y pipeline. Identifica si hay noticias negativas que comunicar.

2. **Diagnosticar** — Determina el formato (email mensual <800 palabras o deck para board). Evalúa si el material existente tiene el balance correcto entre buenas y malas noticias — los inversores valoran la transparencia.

3. **Producir output** — Escribe `outputs/board-update.md` con el update completo estructurado en las 11 secciones del framework, listo para enviar o presentar.

## Output Format

`outputs/board-update.md`:

```
## Investor Update — [Empresa] — [Período]

### Resumen ejecutivo
[3 frases: estado actual, evento principal, próxima dirección]

### Dashboard de métricas
| KPI | Actual | Objetivo | Status |
|---|---|---|---|

### Update financiero
[P&L resumen, runway, burn múltiple, variaciones vs plan]

[... resto de las 11 secciones del framework]

### Asks específicos
- [Nombre si es posible]: [Request concreto y accionable]
```

## Frameworks & Best Practices

[COPIAR VERBATIM "The 11-Section Framework", "The Four-Act Narrative Structure", el protocolo de bad news y cualquier otra sección de frameworks de /tmp/board-update-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/fundraising/board-update.md
git commit -m "feat: add board-update agent (fundraising)"
```

---

### Task 8: market-research.md

**Files:**
- Create: `Startup-Cofounder/agents/fundraising/market-research.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/market-research/SKILL.md \
  --jq '.content' | base64 -d > /tmp/market-research-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/fundraising/market-research.md`:

```markdown
---
name: market-research
description: Cuando el founder necesita calcular el tamaño de mercado o validar sus claims de mercado. Activa con "TAM", "SAM", "SOM", "tamaño de mercado", "market size", "oportunidad de mercado", "slide de mercado".
domain: fundraising
reads: [inputs/]
outputs: [outputs/market-research.md]
---

# Market Research Agent

## Cuándo usar
- El founder necesita calcular TAM/SAM/SOM para su deck
- El founder quiere validar con rigor los claims de mercado que ya tiene
- El founder se prepara para preguntas de inversores sobre el mercado

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (para extraer el mercado objetivo y claims existentes)
- Descripción del producto o one-pager
- Datos de pricing y modelo de negocio
- Cualquier análisis de mercado previo o informes del sector

Si inputs/ está vacío, pregunta: "¿Qué producto vendes, a quién se lo vendes y a qué precio? Con eso puedo construir el TAM/SAM/SOM."

## Workflow

1. **Leer inputs/** — Extrae: descripción del producto, cliente objetivo (ICP), precio por cliente, modelo de ingresos, geografía objetivo, y cualquier claim de mercado existente que necesite validación.

2. **Diagnosticar** — Evalúa si los claims de mercado existentes son creíbles (¿solo top-down? ¿sin fuentes? ¿mercado demasiado amplio?). Identifica qué falta para hacer el análisis defendible ante un inversor.

3. **Producir output** — Escribe `outputs/market-research.md` con TAM/SAM/SOM calculado con metodología top-down + bottom-up, drivers de crecimiento y supuestos explícitos.

## Output Format

`outputs/market-research.md`:

```
## Definición del mercado
[Párrafo definiendo el problema, cliente, geografía y scoping decisions]

## TAM / SAM / SOM
| Métrica | Estimación actual | Proyección 2-3 años | Método | Confianza |
|---|---|---|---|---|
| TAM | $X | $Y | Top-down + Bottom-up | Alta/Media/Baja |
| SAM | $X | $Y | Filtrado de TAM | Alta/Media/Baja |
| SOM | $X | $Y | Modelo de penetración | Alta/Media/Baja |

## Metodología de cálculo
**Top-Down:** [pasos del cálculo desde el total del sector]
**Bottom-Up:** [pasos desde unit economics: N clientes × precio × frecuencia]
**Reconciliación:** [por qué convergen o dónde difieren]

## Drivers de crecimiento
[Factores que expanden o contraen el mercado]

## Supuestos clave y riesgos
| Supuesto | Impacto si falla | Confianza | Cómo validar |
|---|---|---|---|

## Implicaciones estratégicas
[Qué significa para producto, pricing y go-to-market]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/market-research-source.md incluyendo "Always do both top-down and bottom-up", "Beware vanity TAMs" y "The who writes the check test"]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/fundraising/market-research.md
git commit -m "feat: add market-research agent (fundraising)"
```

---

### Task 9: competitive-analysis.md

**Files:**
- Create: `Startup-Cofounder/agents/fundraising/competitive-analysis.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/competitive-analysis/SKILL.md \
  --jq '.content' | base64 -d > /tmp/competitive-analysis-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/fundraising/competitive-analysis.md`:

```markdown
---
name: competitive-analysis
description: Cuando el founder necesita analizar su competencia o posicionar su producto. Activa con "competidores", "landscape competitivo", "cómo nos diferenciamos", "moat", "comparación con X", "posicionamiento".
domain: fundraising
reads: [inputs/]
outputs: [outputs/competitive-analysis.md]
---

# Competitive Analysis Agent

## Cuándo usar
- El founder necesita preparar el slide de competencia del deck
- El founder quiere entender cómo diferenciarse de los players existentes
- El founder se prepara para preguntas de inversores sobre competencia

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (especialmente el slide de competencia existente)
- Descripción del producto y propuesta de valor
- Análisis de competencia previo
- Datos de clientes o feedback que mencione alternativas

Si inputs/ está vacío, pregunta: "¿Cuál es tu producto y quiénes son tus 3-5 competidores más directos?"

## Workflow

1. **Leer inputs/** — Extrae: descripción del producto, cliente objetivo, propuesta de valor diferencial, competidores ya identificados por el founder, y cualquier feedback de clientes sobre alternativas.

2. **Diagnosticar** — Evalúa el análisis existente: ¿dice "no tenemos competidores"? (red flag), ¿usa una 2x2 donde mágicamente dominas? (no convincente), ¿ignora al status quo ("no hacer nada") como competidor? Identifica gaps en el análisis.

3. **Producir output** — Escribe `outputs/competitive-analysis.md` con perfiles de 5 competidores, mapa de diferenciación y recomendación de posicionamiento.

## Output Format

`outputs/competitive-analysis.md`:

```
## Vista general del mercado
[Párrafo sobre estructura, número de players, fragmentación]

## Perfiles de competidores (x5)
### [Nombre competidor]
| Dimensión | Detalle |
|---|---|
| Perfil | Funding, tamaño, fundación |
| Fortalezas del producto | ... |
| Gaps del producto | ... |
| Modelo y pricing | ... |
| Por qué son peligrosos | ... |

## Oportunidades de diferenciación
- [Pain points sin resolver por ningún competidor]
- [Segmentos desatendidos]
- [Cambios de mercado que crean oportunidad]

## Recomendación de posicionamiento
- Posicionamiento sugerido y framing de categoría
- Diferenciadores clave a enfatizar (con evidencia)
- Segmentos donde ganar es más fácil
- Competidores a monitorizar y por qué
- Riesgos competitivos a 12-18 meses
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/competitive-analysis-source.md incluyendo "Primary sources over secondhand", "Status quo is your biggest competitor", "Compete on a different axis", "Track momentum, not just position"]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/fundraising/competitive-analysis.md
git commit -m "feat: add competitive-analysis agent (fundraising)"
```

---

## Fase 2 — Producto & Estrategia (5 agentes)

### Task 10: prd-writing.md

**Files:**
- Create: `Startup-Cofounder/agents/product/prd-writing.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/prd-writing/SKILL.md \
  --jq '.content' | base64 -d > /tmp/prd-writing-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/product/prd-writing.md`:

```markdown
---
name: prd-writing
description: Cuando el founder necesita documentar un feature o iniciativa de producto. Activa con "PRD", "product requirements", "spec de feature", "documentar lo que vamos a construir", "requisitos del producto".
domain: product
reads: [inputs/]
outputs: [outputs/prd.md]
---

# PRD Writing Agent

## Cuándo usar
- El founder quiere convertir una idea de feature en un spec estructurado para el equipo de ingeniería
- El founder necesita alinear a distintos stakeholders sobre qué se va a construir y por qué
- El founder quiere documentar el scope de v1 vs futuras versiones

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Notas o descripción del feature/iniciativa
- Feedback de usuarios o entrevistas que motivan el feature
- Roadmap o contexto estratégico
- Wireframes o mockups si existen
- PRDs anteriores (para mantener el formato del equipo)

Si inputs/ está vacío, pregunta: "¿Qué feature o iniciativa quieres documentar? Descríbelo en 2-3 frases."

## Workflow

1. **Leer inputs/** — Extrae: descripción del feature, problema de usuario que resuelve, segmento de usuarios objetivo, métricas de éxito si se han definido, y cualquier constraint técnico conocido.

2. **Diagnosticar** — Determina si necesitas un PRD ligero (exploración early-stage, 2-3 páginas) o un PRD completo (iniciativa comprometida, 5-8 páginas). Identifica qué información falta para las 8 secciones del framework.

3. **Producir output** — Escribe `outputs/prd.md` con el PRD completo de 8 secciones. Cada sección incluye los supuestos clave explícitos.

## Output Format

`outputs/prd.md` — 8 secciones:

```
# PRD: [Nombre del feature] — v1.0 — [Fecha]

## 1. Resumen
[2-3 frases sobre qué se construye y por qué importa]

## 2. Contactos
[Stakeholders con roles]

## 3. Contexto
[Por qué ahora, qué ha cambiado, contexto competitivo]

## 4. Objetivo
[Metas con métricas SMART: "Permitir a [usuario] hacer [acción] resultando en [outcome medible]"]

## 5. Segmento(s) de mercado
[Usuarios objetivo definidos por problemas, no por demografía]

## 6. Propuesta de valor
[Jobs to be done, gains, pain points eliminados]

## 7. Solución
[Features, flujos de usuario, edge cases (mínimo 5), out-of-scope explícito]

## 8. Release
[Plan por fases: MVP vs iteraciones futuras, criterios de rollback]

## Supuestos clave
| Supuesto | Evidencia | Qué lo invalidaría |
|---|---|---|
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/prd-writing-source.md incluyendo "Problem before solution", "One objective not five", "Market segments defined by needs", "Data-driven specificity", "Scope creep guard"]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/product/prd-writing.md
git commit -m "feat: add prd-writing agent (product)"
```

---

### Task 11: mvp-scoping.md

**Files:**
- Create: `Startup-Cofounder/agents/product/mvp-scoping.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/mvp-scoping/SKILL.md \
  --jq '.content' | base64 -d > /tmp/mvp-scoping-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/product/mvp-scoping.md`:

```markdown
---
name: mvp-scoping
description: Cuando el founder necesita definir qué incluir en la primera versión del producto. Activa con "MVP", "qué construir primero", "scope v1", "qué dejar para después", "lanzamiento mínimo".
domain: product
reads: [inputs/]
outputs: [outputs/mvp-scope.md]
---

# MVP Scoping Agent

## Cuándo usar
- El founder tiene una lista de features y necesita priorizar qué va en v1
- El founder está añadiendo scope y necesita alguien que le frene
- El founder quiere definir los criterios de lanzamiento mínimo viable

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Lista de features o backlog del producto
- PRD o descripción del producto
- Feedback de usuarios o early adopters
- Roadmap o notas de planificación

Si inputs/ está vacío, pregunta: "¿Cuál es el problema central que resuelve tu producto y quién es el usuario más importante que necesita esa solución hoy?"

## Workflow

1. **Leer inputs/** — Extrae: lista de features o funcionalidades planteadas, usuario objetivo, hipótesis principal del negocio, y cualquier constraint (tiempo, equipo, funding).

2. **Diagnosticar** — Evalúa cada feature contra el criterio central: ¿es imprescindible para que el usuario core consiga su job-to-be-done? Si no, es candidato a defer. Identifica scope creep y features "nice to have".

3. **Producir output** — Escribe `outputs/mvp-scope.md` con la clasificación IN/OUT de cada feature, los criterios de lanzamiento, y el "definition of done" del MVP.

## Output Format

`outputs/mvp-scope.md`:

```
## Hipótesis del MVP
[La hipótesis principal que el MVP necesita validar, en una frase]

## Usuario core del MVP
[Perfil específico: quién, con qué problema, en qué contexto]

## Features: IN vs OUT

### IN — v1
| Feature | Por qué es esencial | Esfuerzo estimado |
|---|---|---|

### OUT — v2+
| Feature | Por qué se difiere | Cuándo reconsiderar |
|---|---|---|

## Criterios de lanzamiento
- [ ] [Criterio 1 — lo mínimo para que el usuario core lo use]
- [ ] [Criterio 2]
...

## Definition of done del MVP
[Descripción de qué tiene que ser verdad para considerar el MVP "lanzado"]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/mvp-scoping-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/product/mvp-scoping.md
git commit -m "feat: add mvp-scoping agent (product)"
```

---

### Task 12: roadmap-planning.md

**Files:**
- Create: `Startup-Cofounder/agents/product/roadmap-planning.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/roadmap-planning/SKILL.md \
  --jq '.content' | base64 -d > /tmp/roadmap-planning-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/product/roadmap-planning.md`:

```markdown
---
name: roadmap-planning
description: Cuando el founder necesita organizar y priorizar el trabajo de producto en el tiempo. Activa con "roadmap", "planificación de producto", "qué construir cuándo", "priorización", "quarterly planning".
domain: product
reads: [inputs/]
outputs: [outputs/roadmap.md]
---

# Roadmap Planning Agent

## Cuándo usar
- El founder necesita ordenar el backlog en un roadmap por fases
- El founder quiere comunicar la dirección del producto a inversores o equipo
- El founder necesita priorizar con constraintde recursos limitados

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Backlog de features o lista de iniciativas
- PRDs existentes
- Feedback de usuarios o datos de uso
- OKRs o prioridades estratégicas del período

Si inputs/ está vacío, pregunta: "¿Cuáles son las 3-5 cosas más importantes que necesita tu producto en los próximos 3-6 meses y por qué?"

## Workflow

1. **Leer inputs/** — Extrae todas las iniciativas y features identificadas. Agrupa las relacionadas. Identifica dependencias (qué necesita estar listo antes que qué).

2. **Diagnosticar** — Evalúa cada iniciativa en dos ejes: impacto en el objetivo estratégico principal y esfuerzo/complejidad. Identifica iniciativas de alto impacto / bajo esfuerzo como candidatas a Now, y bajo impacto / alto esfuerzo como candidatas a descarte o defer.

3. **Producir output** — Escribe `outputs/roadmap.md` con el roadmap por fases temporales relativas (Now/Next/Later), dependencias explícitas y criterios de éxito por fase.

## Output Format

`outputs/roadmap.md`:

```
## Objetivo estratégico del período
[Qué debe ser verdad al final del período para considerar el roadmap exitoso]

## Roadmap por fases

### Now (0-6 semanas)
| Iniciativa | Impacto | Por qué ahora | Owner | Criterio de éxito |
|---|---|---|---|---|

### Next (6-16 semanas)
[misma tabla — dependencias de "Now" explícitas]

### Later (>16 semanas)
[misma tabla — condiciones que activarían el trabajo]

## Dependencias críticas
[Qué tiene que estar listo antes de poder empezar cada bloque]

## Iniciativas descartadas (y por qué)
[Lista de lo que se decidió NO hacer en este período]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/roadmap-planning-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/product/roadmap-planning.md
git commit -m "feat: add roadmap-planning agent (product)"
```

---

### Task 13: user-research-synthesis.md

**Files:**
- Create: `Startup-Cofounder/agents/product/user-research-synthesis.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/user-research-synthesis/SKILL.md \
  --jq '.content' | base64 -d > /tmp/user-research-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/product/user-research-synthesis.md`:

```markdown
---
name: user-research-synthesis
description: Cuando el founder tiene notas de entrevistas de usuarios y quiere extraer insights accionables. Activa con "entrevistas de usuarios", "customer discovery", "sintetizar feedback", "qué nos dicen los usuarios".
domain: product
reads: [inputs/]
outputs: [outputs/user-research-synthesis.md]
---

# User Research Synthesis Agent

## Cuándo usar
- El founder tiene notas de entrevistas de usuarios y no sabe qué hacer con ellas
- El founder quiere identificar patrones en el feedback recibido
- El founder necesita traducir observaciones en decisiones de producto

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Notas de entrevistas de usuarios (Word, PDF, TXT)
- Transcripciones de llamadas de discovery
- Respuestas a encuestas (CSV, Excel)
- Emails o mensajes de usuarios con feedback

Si inputs/ está vacío, pregunta: "¿Tienes notas de entrevistas de usuarios o feedback de clientes que pueda analizar?"

## Workflow

1. **Leer inputs/** — Lee todas las notas e identificar las citas textuales más reveladoras. Agrupa por temas emergentes sin forzar categorías previas.

2. **Diagnosticar** — Encuentra patrones: ¿qué problemas mencionan >50% de los usuarios? ¿Qué workarounds están usando? ¿Qué outcomes buscan que el producto no da? ¿Qué sorpresas hay vs. las hipótesis previas?

3. **Producir output** — Escribe `outputs/user-research-synthesis.md` con insights priorizados por frecuencia e impacto, citas textuales de soporte, y acciones de producto recomendadas.

## Output Format

`outputs/user-research-synthesis.md`:

```
## Resumen ejecutivo
[3-5 bullets con los hallazgos más importantes]

## Insights por tema

### [Tema 1] — mencionado por X/Y entrevistados
**Insight:** [Qué quieren o necesitan realmente]
**Evidencia:** "[Cita textual 1]" — [perfil de usuario]
           "[Cita textual 2]" — [perfil de usuario]
**Implicación para producto:** [Qué sugiere hacer]

[repetir por cada tema]

## Sorpresas vs. hipótesis previas
[Lo que era diferente a lo esperado]

## Acciones recomendadas (priorizadas)
1. [Acción] — basada en [insight], impacto esperado: [descripción]
2. ...

## Perfiles de usuario emergentes
[Si hay segmentos distintos que aparecen en los datos]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/user-research-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/product/user-research-synthesis.md
git commit -m "feat: add user-research-synthesis agent (product)"
```

---

### Task 14: feedback-synthesis.md

**Files:**
- Create: `Startup-Cofounder/agents/product/feedback-synthesis.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/feedback-synthesis/SKILL.md \
  --jq '.content' | base64 -d > /tmp/feedback-synthesis-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/product/feedback-synthesis.md`:

```markdown
---
name: feedback-synthesis
description: Cuando el founder tiene feedback acumulado de usuarios o clientes y quiere convertirlo en acciones. Activa con "feedback de usuarios", "reviews", "NPS comments", "tickets de soporte", "quejas de clientes".
domain: product
reads: [inputs/]
outputs: [outputs/feedback-synthesis.md]
---

# Feedback Synthesis Agent

## Cuándo usar
- El founder tiene feedback acumulado (reviews, tickets, NPS, emails) y no sabe por dónde empezar
- El founder quiere identificar los problemas más frecuentes para priorizarlos
- El founder necesita transformar quejas en decisiones de producto accionables

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Exports de reviews (G2, App Store, Play Store — CSV o Excel)
- Tickets de soporte o Zendesk exports
- Respuestas de NPS con comentarios
- Emails de clientes con feedback
- Churn surveys o exit interviews

Si inputs/ está vacío, pregunta: "¿De dónde viene el feedback — reviews, soporte, emails de clientes? ¿Tienes algún archivo que pueda analizar?"

## Workflow

1. **Leer inputs/** — Lee todo el feedback disponible. Clasifica cada ítem como positivo, negativo o solicitud de feature. Identifica las categorías de problemas más frecuentes.

2. **Diagnosticar** — Prioriza por frecuencia × impacto percibido. Separa bugs de peticiones de feature de problemas de UX. Identifica si hay patrones en qué tipo de usuario da el feedback negativo.

3. **Producir output** — Escribe `outputs/feedback-synthesis.md` con los problemas priorizados, evidencia de soporte, y acciones concretas de producto o soporte.

## Output Format

`outputs/feedback-synthesis.md`:

```
## Resumen de feedback analizado
- Total ítems: N
- Positivo: N (X%)
- Negativo/Problemas: N (X%)
- Feature requests: N (X%)

## Top problemas (por frecuencia)

### Problema 1: [Descripción] — mencionado N veces (X%)
**Tipo:** Bug / UX / Feature gap / Expectativa no cumplida
**Muestra de feedback:**
- "[cita]" — [fuente, fecha]
**Acción recomendada:** [Qué hacer — fix, cambio de UX, cambio de expectativas en onboarding]
**Prioridad:** Alta / Media / Baja

[repetir para cada problema significativo]

## Feature requests más solicitadas
| Feature | Menciones | Segmento que lo pide | Esfuerzo estimado |
|---|---|---|---|

## Patrones positivos (qué está funcionando)
[Lo que los usuarios elogian — para no romperlo]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/feedback-synthesis-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/product/feedback-synthesis.md
git commit -m "feat: add feedback-synthesis agent (product)"
```

---

## Fase 3 — Marketing & Crecimiento (7 agentes)

### Task 15: content-strategy.md

**Files:**
- Create: `Startup-Cofounder/agents/marketing/content-strategy.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/content-strategy/SKILL.md \
  --jq '.content' | base64 -d > /tmp/content-strategy-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/marketing/content-strategy.md`:

```markdown
---
name: content-strategy
description: Cuando el founder quiere crear una estrategia de contenido para crecer. Activa con "estrategia de contenido", "content marketing", "blog", "newsletter", "qué publicar", "calendario editorial".
domain: marketing
reads: [inputs/]
outputs: [outputs/content-strategy.md]
---

# Content Strategy Agent

## Cuándo usar
- El founder quiere usar contenido para generar leads o brand awareness
- El founder no sabe qué tipo de contenido crear ni con qué frecuencia
- El founder quiere construir una audiencia antes del lanzamiento

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto o pitch deck (para entender el ICP)
- Contenido existente publicado (posts, artículos, newsletters)
- Datos de analytics si están disponibles
- Perfil del founder (para construir thought leadership)

Si inputs/ está vacío, pregunta: "¿A quién va dirigido tu producto y qué problema resuelves? ¿Tienes ya algún canal de contenido activo?"

## Workflow

1. **Leer inputs/** — Extrae: ICP y sus problemas/intereses, propuesta de valor del producto, canales existentes y su rendimiento, y voz/tono del founder si hay contenido previo.

2. **Diagnosticar** — Evalúa si hay estrategia o publicación ad-hoc. Identifica el canal con más potencial dado el ICP. Detecta qué temas son territorio natural del founder (autoridad, experiencia vivida).

3. **Producir output** — Escribe `outputs/content-strategy.md` con la estrategia de contenido, pilares temáticos, calendario editorial para 30 días y métricas de éxito.

## Output Format

`outputs/content-strategy.md`:

```
## Estrategia de contenido — [Empresa]

### ICP y sus intereses
[Quién es, qué lee, qué problemas tiene que el contenido puede resolver]

### Canales prioritarios
| Canal | Audiencia potencial | Frecuencia | Formato |
|---|---|---|---|

### Pilares temáticos (3-4)
1. [Pilar] — por qué el founder tiene autoridad aquí
2. ...

### Calendario editorial — primeros 30 días
| Semana | Canal | Tema | Ángulo | CTA |
|---|---|---|---|---|

### Métricas de éxito
[KPIs concretos: seguidores, tráfico, leads generados, open rate]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/content-strategy-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/marketing/content-strategy.md
git commit -m "feat: add content-strategy agent (marketing)"
```

---

### Task 16: launch-strategy.md

**Files:**
- Create: `Startup-Cofounder/agents/marketing/launch-strategy.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/launch-strategy/SKILL.md \
  --jq '.content' | base64 -d > /tmp/launch-strategy-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/marketing/launch-strategy.md`:

```markdown
---
name: launch-strategy
description: Cuando el founder se prepara para lanzar su producto o una feature importante. Activa con "lanzamiento", "launch", "Product Hunt", "cómo anunciar", "go-to-market", "estrategia de lanzamiento".
domain: marketing
reads: [inputs/]
outputs: [outputs/launch-strategy.md]
---

# Launch Strategy Agent

## Cuándo usar
- El founder está a semanas de lanzar su producto o una feature importante
- El founder quiere maximizar el impacto del lanzamiento con recursos limitados
- El founder quiere saber qué canales y tácticas usar en el lanzamiento

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto y propuesta de valor
- Lista de early adopters, waitlist o beta users
- Canales de distribución existentes (newsletter, redes, comunidades)
- Fecha objetivo de lanzamiento

Si inputs/ está vacío, pregunta: "¿Qué vas a lanzar, cuándo y a quién va dirigido principalmente?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor core, ICP, canales existentes, audiencia actual (tamaño de waitlist, seguidores, comunidades), y fecha de lanzamiento objetivo.

2. **Diagnosticar** — Evalúa qué tipo de lanzamiento tiene más sentido dado los recursos: Product Hunt, comunidades nicho, PR, outreach directo, o una combinación. Identifica si hay suficiente tracción previa para un lanzamiento público o si debe hacerse en fases.

3. **Producir output** — Escribe `outputs/launch-strategy.md` con el plan de lanzamiento semana a semana, tácticas por canal, copies clave y métricas de éxito.

## Output Format

`outputs/launch-strategy.md`:

```
## Plan de lanzamiento — [Producto] — [Fecha objetivo]

### Objetivo del lanzamiento
[Qué debe ser verdad en las 72h post-lanzamiento — métrica específica]

### Canales y tácticas

| Canal | Táctica | Responsable | Timing | KPI |
|---|---|---|---|---|

### Cronograma semana a semana

**T-4 semanas:** [acciones de preparación]
**T-2 semanas:** [acciones de calentamiento]
**T-1 semana:** [acciones de pre-lanzamiento]
**Día 0:** [acciones del día de lanzamiento]
**T+1 semana:** [follow-up y amplificación]

### Copies clave
- Headline del lanzamiento: [texto]
- Tagline de Product Hunt / HackerNews: [texto]
- Tweet/post de anuncio: [texto completo]

### Métricas de éxito
[KPIs a 24h, 72h y 1 semana]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/launch-strategy-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/marketing/launch-strategy.md
git commit -m "feat: add launch-strategy agent (marketing)"
```

---

### Task 17: landing-page.md

**Files:**
- Create: `Startup-Cofounder/agents/marketing/landing-page.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/landing-page/SKILL.md \
  --jq '.content' | base64 -d > /tmp/landing-page-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/marketing/landing-page.md`:

```markdown
---
name: landing-page
description: Cuando el founder necesita escribir el copy de su landing page. Activa con "landing page", "home page", "copy del sitio web", "página principal", "conversión del sitio".
domain: marketing
reads: [inputs/]
outputs: [outputs/landing-page.md]
---

# Landing Page Agent

## Cuándo usar
- El founder necesita escribir el copy de su landing page desde cero
- El founder quiere mejorar una landing page que no está convirtiendo
- El founder quiere asegurarse de que el mensaje de la landing conecta con el ICP

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto o pitch deck
- URL o screenshot de la landing actual (si existe)
- Testimonials o quotes de clientes
- Datos de conversión actuales si están disponibles

Si inputs/ está vacío, pregunta: "¿Qué hace tu producto, quién es tu cliente objetivo y cuál es el CTA principal de la landing (signup, demo, contacto)?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor diferencial, ICP y sus principales pain points, prueba social disponible (clientes, testimonials, métricas), y el CTA objetivo.

2. **Diagnosticar** — Evalúa si la landing actual (si existe) tiene: headline que captura el beneficio clave en <5 segundos, subheadline que añade contexto, prueba social creíble, CTA claro y repetido, y ausencia de jargon técnico que confunde al ICP.

3. **Producir output** — Escribe `outputs/landing-page.md` con el copy completo sección a sección, listo para implementar.

## Output Format

`outputs/landing-page.md`:

```
## Copy de Landing Page — [Empresa]

### Hero section
**Headline:** [Beneficio principal en <10 palabras]
**Subheadline:** [Contexto adicional en 1-2 frases]
**CTA principal:** [Texto del botón]
**CTA secundario (si aplica):** [Texto]

### Sección de problema
[Copy que hace que el visitante piense "eso me pasa a mí exactamente"]

### Sección de solución / producto
[Copy + descripción de 3-5 beneficios clave (no features)]

### Prueba social
[Testimonial 1: "[cita]" — Nombre, Cargo, Empresa]
[Métricas si las hay: "X empresas ya usan...", "Y% de mejora en Z"]

### Sección de features (si aplica)
[3 features con nombre, descripción breve y beneficio]

### FAQ (3-5 preguntas)
[Preguntas reales que tiene el ICP antes de convertir]

### CTA final
[Headline de cierre + CTA button]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/landing-page-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/marketing/landing-page.md
git commit -m "feat: add landing-page agent (marketing)"
```

---

### Task 18: cold-outreach.md

**Files:**
- Create: `Startup-Cofounder/agents/marketing/cold-outreach.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/cold-outreach/SKILL.md \
  --jq '.content' | base64 -d > /tmp/cold-outreach-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/marketing/cold-outreach.md`:

```markdown
---
name: cold-outreach
description: Cuando el founder necesita escribir emails de cold outreach para ventas B2B. Activa con "cold email", "prospección", "outreach a clientes", "secuencia de emails", "ventas outbound".
domain: marketing
reads: [inputs/]
outputs: [outputs/cold-outreach.md]
---

# Cold Outreach Agent

## Cuándo usar
- El founder necesita escribir emails de prospección para conseguir sus primeros clientes
- El founder quiere construir una secuencia de follow-ups automatizable
- El founder quiere personalizar outreach para un segmento específico de clientes

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto y propuesta de valor
- ICP o perfil del cliente objetivo
- Lista de prospects (si existe — nombre, empresa, cargo)
- Emails previos enviados (para mejorar el tono y los resultados)

Si inputs/ está vacío, pregunta: "¿A qué tipo de empresa y cargo va dirigido el outreach? ¿Qué problema específico les resuelves?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor diferencial para este segmento específico, pain point principal del ICP, prueba social disponible (clientes similares, métricas), y cualquier hook de personalización posible.

2. **Diagnosticar** — Evalúa si los emails existentes son demasiado largos, demasiado centrados en el producto en vez del problema del cliente, o carecen de CTA específico.

3. **Producir output** — Escribe `outputs/cold-outreach.md` con una secuencia de 3-4 emails (primer contacto + follow-ups), con subject lines y variantes de personalización.

## Output Format

`outputs/cold-outreach.md`:

```
## Secuencia de cold outreach — [Segmento objetivo]

### Email 1 — Día 0
**Asunto:** [Subject line — específico, no genérico]
**Cuerpo:**
[Email completo — máx 150 palabras]

### Email 2 — Día 3 (si no responde)
**Asunto:** Re: [Asunto anterior]
[Follow-up breve añadiendo un ángulo diferente]

### Email 3 — Día 7 (si no responde)
[Breakup email — cierre amigable que deja la puerta abierta]

### Variantes de personalización
[Cómo cambiar el email si el prospect es: startup / empresa grande / sector específico]

### A/B de subject lines para testear
1. [Opción A]
2. [Opción B]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/cold-outreach-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/marketing/cold-outreach.md
git commit -m "feat: add cold-outreach agent (marketing)"
```

---

### Task 19: sales-script.md

**Files:**
- Create: `Startup-Cofounder/agents/marketing/sales-script.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/sales-script/SKILL.md \
  --jq '.content' | base64 -d > /tmp/sales-script-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/marketing/sales-script.md`:

```markdown
---
name: sales-script
description: Cuando el founder necesita estructurar su demo o llamada de ventas. Activa con "sales script", "demo", "llamada de ventas", "cómo vender", "objeciones de clientes", "script de pitch a clientes".
domain: marketing
reads: [inputs/]
outputs: [outputs/sales-script.md]
---

# Sales Script Agent

## Cuándo usar
- El founder va a hacer demos de producto y quiere estructurarlas mejor
- El founder recibe siempre las mismas objeciones y no sabe cómo responderlas
- El founder quiere estandarizar el proceso de ventas para que otros lo repliquen

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto y casos de uso
- Notas de demos o llamadas previas (objeciones recibidas)
- Feedback de clientes que no convirtieron
- Propuesta de valor y diferenciadores

Si inputs/ está vacío, pregunta: "¿Cuánto dura una demo típica y cuáles son las 3 objeciones más frecuentes que escuchas?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor, casos de uso clave, objeciones más frecuentes recibidas, y el perfil del comprador (quién decide, quién usa, quién bloquea).

2. **Diagnosticar** — Evalúa si el script existente (si lo hay) empieza con el producto en vez del problema del cliente, si el demo sigue un flujo lógico, y si hay respuestas preparadas para las objeciones principales.

3. **Producir output** — Escribe `outputs/sales-script.md` con el script completo de la llamada/demo y el playbook de objeciones.

## Output Format

`outputs/sales-script.md`:

```
## Script de demo/ventas — [Producto]

### Apertura (2 min)
[Preguntas de discovery para entender el contexto del prospect antes de empezar]

### Conexión problema-solución (3 min)
[Cómo conectar lo que dijeron con lo que el producto resuelve]

### Demo del producto (10-15 min)
[Flujo de demo: qué mostrar primero, qué highlight, qué omitir]
- Momento 1: [qué mostrar y qué decir]
- Momento 2: ...

### Cierre y próximos pasos (5 min)
[Cómo conseguir el compromiso concreto al final de la llamada]

### Playbook de objeciones
| Objeción | Respuesta | Reencuadre |
|---|---|---|
| "Es muy caro" | ... | ... |
| "No es el momento" | ... | ... |
| "Necesito consultarlo" | ... | ... |
| [objeciones específicas del producto] | ... | ... |
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/sales-script-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/marketing/sales-script.md
git commit -m "feat: add sales-script agent (marketing)"
```

---

### Task 20: social-content.md

**Files:**
- Create: `Startup-Cofounder/agents/marketing/social-content.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/social-content/SKILL.md \
  --jq '.content' | base64 -d > /tmp/social-content-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/marketing/social-content.md`:

```markdown
---
name: social-content
description: Cuando el founder necesita crear posts para LinkedIn o Twitter/X. Activa con "post de LinkedIn", "tweet", "contenido para redes", "build in public", "thought leadership del founder".
domain: marketing
reads: [inputs/]
outputs: [outputs/social-content.md]
---

# Social Content Agent

## Cuándo usar
- El founder quiere publicar regularmente en LinkedIn o Twitter pero no sabe sobre qué
- El founder quiere hacer build in public y necesita ayuda con el formato
- El founder quiere compartir aprendizajes de la startup de forma que construya audiencia

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Notas, reflexiones o aprendizajes recientes del founder
- Métricas o hitos recientes de la startup
- Descripción del sector y la startup
- Posts anteriores que funcionaron bien (si existen)

Si inputs/ está vacío, pregunta: "¿Qué ha pasado en la startup esta semana que podría ser interesante para otros founders o potenciales clientes?"

## Workflow

1. **Leer inputs/** — Extrae: hitos recientes, aprendizajes, reflexiones del founder, y cualquier dato o historia que sea genuinamente interesante para la audiencia objetivo.

2. **Diagnosticar** — Identifica el tipo de contenido más adecuado: lección aprendida, dato sorprendente, historia personal, contrarian take, o milestone. Evalúa si la voz es auténtica o suena a marketing corporativo.

3. **Producir output** — Escribe `outputs/social-content.md` con 5-7 posts listos para publicar, con variantes para LinkedIn y Twitter.

## Output Format

`outputs/social-content.md`:

```
## Posts para publicar — [Semana de fecha]

### Post 1 — [Tipo: lección / hito / dato / historia]
**LinkedIn:**
[Post completo — párrafos cortos, hook en la primera línea]

**Twitter/X:**
[Versión condensada — hilo si necesario]

### Post 2...
[repetir]

## Calendario sugerido
| Día | Post | Canal | Hora recomendada |
|---|---|---|---|
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/social-content-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/marketing/social-content.md
git commit -m "feat: add social-content agent (marketing)"
```

---

### Task 21: seo-technical.md

**Files:**
- Create: `Startup-Cofounder/agents/marketing/seo-technical.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/seo-technical/SKILL.md \
  --jq '.content' | base64 -d > /tmp/seo-technical-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/marketing/seo-technical.md`:

```markdown
---
name: seo-technical
description: Cuando el founder quiere que su web aparezca en búsquedas relevantes. Activa con "SEO", "posicionamiento web", "keywords", "tráfico orgánico", "aparecer en Google".
domain: marketing
reads: [inputs/]
outputs: [outputs/seo-plan.md]
---

# SEO Technical Agent

## Cuándo usar
- El founder quiere generar tráfico orgánico pero no sabe por dónde empezar
- El founder quiere auditar el SEO de su web actual
- El founder quiere construir un plan de keywords relevante para su ICP

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- URL o descripción del sitio web
- Descripción del producto y el ICP
- Analytics del sitio si están disponibles (tráfico, bounce rate, páginas)
- Lista de competidores conocidos

Si inputs/ está vacío, pregunta: "¿Cuál es la URL de tu web y a qué busca tu cliente cuando tiene el problema que tú resuelves?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor, ICP, competidores, y cualquier dato de rendimiento SEO existente.

2. **Diagnosticar** — Evalúa el estado SEO actual: ¿hay keyword targeting? ¿Las páginas tienen meta titles y descriptions optimizadas? ¿Hay contenido que pueda rankear? ¿Hay problemas técnicos obvios?

3. **Producir output** — Escribe `outputs/seo-plan.md` con la estrategia de keywords, auditoría de páginas clave y plan de acción priorizado.

## Output Format

`outputs/seo-plan.md`:

```
## Plan SEO — [Empresa]

### Keywords objetivo

| Keyword | Intención | Dificultad estimada | Prioridad |
|---|---|---|---|
| [keyword primaria] | Informacional/Transaccional | Alta/Media/Baja | 1 |

### Auditoría de páginas clave
| Página | Meta title actual | Meta title sugerido | Issues |
|---|---|---|---|

### Acciones priorizadas
1. [Acción técnica — ej: añadir meta descriptions a todas las páginas]
2. [Acción de contenido — ej: crear página de comparación vs competidor X]
3. ...

### Calendario de contenido SEO (3 meses)
[Artículos/páginas a crear con keyword objetivo y brief]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/seo-technical-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/marketing/seo-technical.md
git commit -m "feat: add seo-technical agent (marketing)"
```

---

## Fase 4 — Legal & Operaciones (5 agentes)

### Task 22: contract-review.md

**Files:**
- Create: `Startup-Cofounder/agents/legal-ops/contract-review.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/contract-review/SKILL.md \
  --jq '.content' | base64 -d > /tmp/contract-review-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/legal-ops/contract-review.md`:

```markdown
---
name: contract-review
description: Cuando el founder necesita revisar un contrato antes de firmarlo. Activa con "revisar contrato", "contrato cliente", "NDA", "acuerdo", "cláusulas", "red flags en contrato".
domain: legal-ops
reads: [inputs/]
outputs: [outputs/contract-review.md]
---

# Contract Review Agent

## Cuándo usar
- El founder recibe un contrato de un cliente, proveedor o partner y quiere revisarlo antes de firmar
- El founder quiere identificar cláusulas problemáticas o desequilibradas
- El founder necesita una lista de puntos a negociar

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- El contrato a revisar (PDF o Word)
- Contexto del acuerdo si se proporciona (tipo de relación, importes, duración)

Si inputs/ no tiene ningún contrato, pregunta: "¿Puedes pegar el texto del contrato o subir el archivo?"

**Advertencia:** Este agente proporciona análisis informativo, no asesoramiento legal. Para contratos de alto valor o complejidad, consulta con un abogado.

## Workflow

1. **Leer inputs/** — Lee el contrato completo. Identifica: tipo de contrato, partes, duración, valor económico, y jurisdicción aplicable.

2. **Diagnosticar** — Revisa cláusula por cláusula las áreas de riesgo: propiedad intelectual, limitación de responsabilidad, terminación, exclusividad, non-compete, penalizaciones, y condiciones de pago.

3. **Producir output** — Escribe `outputs/contract-review.md` con el resumen del contrato, red flags ordenadas por severidad, y puntos de negociación recomendados.

## Output Format

`outputs/contract-review.md`:

```
## Revisión de contrato — [Tipo] — [Partes]

### Resumen ejecutivo
- Tipo: [NDA / MSA / SaaS Agreement / Contrato de servicios / otro]
- Partes: [Parte A] ↔ [Parte B]
- Duración: [X meses / sin fecha fin]
- Valor económico: [$X / no especificado]
- Jurisdicción: [País/Estado]

### Red flags por severidad

🔴 **Alta — negociar antes de firmar**
- [Cláusula X]: [problema y riesgo concreto]

🟡 **Media — negociar si es posible**
- [Cláusula Y]: [problema y alternativa sugerida]

🟢 **Baja — estándar, aceptable**
- [Lista de cláusulas que están bien]

### Puntos de negociación recomendados
1. [Cláusula] → propuesta de cambio específico
2. ...

### Cláusulas que faltan y deberían estar
- [Lista de protecciones estándar ausentes en el contrato]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/contract-review-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/legal-ops/contract-review.md
git commit -m "feat: add contract-review agent (legal-ops)"
```

---

### Task 23: terms-of-service.md

**Files:**
- Create: `Startup-Cofounder/agents/legal-ops/terms-of-service.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/terms-of-service/SKILL.md \
  --jq '.content' | base64 -d > /tmp/tos-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/legal-ops/terms-of-service.md`:

```markdown
---
name: terms-of-service
description: Cuando el founder necesita crear o revisar los términos y condiciones de su producto. Activa con "términos y condiciones", "terms of service", "ToS", "condiciones de uso", "términos de servicio".
domain: legal-ops
reads: [inputs/]
outputs: [outputs/terms-of-service.md]
---

# Terms of Service Agent

## Cuándo usar
- El founder va a lanzar su producto y necesita ToS antes de aceptar usuarios
- El founder tiene unos ToS genéricos y quiere adaptarlos a su modelo de negocio
- El founder quiere añadir cláusulas específicas a sus ToS existentes

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- ToS actuales (si existen)
- Descripción del producto y modelo de negocio
- Tipo de usuarios (B2B, B2C, marketplace)
- Jurisdicción principal de operación

Si inputs/ está vacío, pregunta: "¿Es un SaaS B2B, B2C, marketplace u otro modelo? ¿Desde qué país operas y a qué mercados?"

**Advertencia:** Este agente genera un borrador de trabajo. Para ToS finales que aplican a un producto real, valida con un abogado.

## Workflow

1. **Leer inputs/** — Extrae: tipo de producto, modelo de negocio, tipo de usuario, jurisdicción, y cualquier característica específica que necesite cobertura legal especial (pagos, datos de salud, menores, etc.).

2. **Diagnosticar** — Identifica qué cláusulas son críticas para este modelo de negocio específico y cuáles pueden ser estándar.

3. **Producir output** — Escribe `outputs/terms-of-service.md` con los ToS completos adaptados al modelo de negocio.

## Output Format

`outputs/terms-of-service.md` con estas secciones estándar adaptadas:

```
# Términos y Condiciones de Uso — [Empresa]
*Última actualización: [fecha]*

## 1. Aceptación de los términos
## 2. Descripción del servicio
## 3. Registro y cuenta de usuario
## 4. Uso aceptable
## 5. Propiedad intelectual
## 6. Privacidad y datos
## 7. Pagos y facturación [si aplica]
## 8. Limitación de responsabilidad
## 9. Modificaciones del servicio
## 10. Terminación
## 11. Ley aplicable y jurisdicción
## 12. Contacto
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/tos-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/legal-ops/terms-of-service.md
git commit -m "feat: add terms-of-service agent (legal-ops)"
```

---

### Task 24: privacy-policy.md

**Files:**
- Create: `Startup-Cofounder/agents/legal-ops/privacy-policy.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/privacy-policy/SKILL.md \
  --jq '.content' | base64 -d > /tmp/privacy-policy-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/legal-ops/privacy-policy.md`:

```markdown
---
name: privacy-policy
description: Cuando el founder necesita crear o revisar su política de privacidad. Activa con "política de privacidad", "privacy policy", "GDPR", "protección de datos", "LOPD", "tratamiento de datos".
domain: legal-ops
reads: [inputs/]
outputs: [outputs/privacy-policy.md]
---

# Privacy Policy Agent

## Cuándo usar
- El founder va a lanzar su producto y necesita política de privacidad (obligatoria si recopila datos)
- El founder opera en la UE y necesita cumplir con el GDPR
- El founder quiere revisar si su política actual cubre todos los tratamientos de datos que hace

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Política de privacidad actual (si existe)
- Descripción del producto y qué datos recoge
- Lista de terceros que procesan datos (analytics, CRM, emails, pagos)
- Jurisdicción y mercados objetivo

Si inputs/ está vacío, pregunta: "¿Qué datos recoge tu producto (email, nombre, datos de uso, datos de pago)? ¿Operas en la UE?"

**Advertencia:** Este agente genera un borrador. Para productos que tratan datos sensibles o en jurisdicciones específicas, valida con un abogado especializado en protección de datos.

## Workflow

1. **Leer inputs/** — Extrae: qué datos se recopilan, para qué propósito, con qué terceros se comparten, cuánto tiempo se retienen, y en qué jurisdicciones opera el producto.

2. **Diagnosticar** — Evalúa si el tratamiento de datos tiene base legal suficiente (consentimiento, interés legítimo, contrato), si faltan categorías de datos en la política actual, y si hay transferencias internacionales de datos que necesitan cobertura.

3. **Producir output** — Escribe `outputs/privacy-policy.md` con la política completa adaptada al producto y jurisdicción.

## Output Format

`outputs/privacy-policy.md` con estas secciones:

```
# Política de Privacidad — [Empresa]
*Última actualización: [fecha]*

## 1. Responsable del tratamiento
## 2. Datos que recopilamos
## 3. Finalidad y base legal del tratamiento
## 4. Terceros con quienes compartimos datos
## 5. Transferencias internacionales [si aplica]
## 6. Período de retención
## 7. Derechos del usuario (acceso, rectificación, supresión, portabilidad)
## 8. Cookies [si aplica]
## 9. Seguridad de los datos
## 10. Menores de edad [si aplica]
## 11. Modificaciones de esta política
## 12. Contacto y DPO [si aplica]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/privacy-policy-source.md, incluyendo requisitos GDPR específicos]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/legal-ops/privacy-policy.md
git commit -m "feat: add privacy-policy agent (legal-ops)"
```

---

### Task 25: process-docs.md

**Files:**
- Create: `Startup-Cofounder/agents/legal-ops/process-docs.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/process-docs/SKILL.md \
  --jq '.content' | base64 -d > /tmp/process-docs-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/legal-ops/process-docs.md`:

```markdown
---
name: process-docs
description: Cuando el founder necesita documentar procesos internos para que el equipo los ejecute de forma consistente. Activa con "SOP", "proceso interno", "documentar cómo hacemos X", "manual de operaciones", "onboarding de empleados".
domain: legal-ops
reads: [inputs/]
outputs: [outputs/process-docs.md]
---

# Process Documentation Agent

## Cuándo usar
- El founder hace algo repetidamente y quiere que otros en el equipo lo ejecuten igual
- El founder está contratando a alguien y necesita documentar cómo funciona la empresa
- El founder quiere reducir la dependencia de su conocimiento tácito no documentado

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Notas o descripción del proceso a documentar
- Documentación existente (aunque sea incompleta)
- Checklists o emails que describan pasos del proceso
- Capturas de pantalla o grabaciones de pantalla del proceso

Si inputs/ está vacío, pregunta: "¿Qué proceso quieres documentar? Descríbelo en 3-5 pasos aunque sean incompletos."

## Workflow

1. **Leer inputs/** — Extrae: objetivo del proceso, quién lo ejecuta, con qué frecuencia, qué herramientas usa, y los pasos aproximados ya identificados.

2. **Diagnosticar** — Identifica qué pasos del proceso son ambiguos o dependen de conocimiento no documentado. Detecta posibles puntos de fallo o decisiones que el ejecutor necesita tomar.

3. **Producir output** — Escribe `outputs/process-docs.md` con el SOP completo: objetivo, propietario, trigger, pasos detallados, puntos de decisión, herramientas y checklist de verificación.

## Output Format

`outputs/process-docs.md`:

```
# SOP: [Nombre del proceso]
*Propietario: [Rol] | Frecuencia: [diario/semanal/por evento] | Última revisión: [fecha]*

## Objetivo
[Qué debe lograrse cuando el proceso se completa correctamente]

## Cuándo ejecutar este proceso
[Trigger — qué evento o condición lo activa]

## Herramientas necesarias
[Lista de herramientas, accesos o recursos necesarios]

## Pasos

### Paso 1: [Nombre]
**Quién:** [Rol responsable]
**Qué hacer:** [Instrucciones detalladas]
**Herramienta:** [Herramienta específica]
**Si pasa X:** [Decisión o escalado]

[repetir por cada paso]

## Checklist de verificación
- [ ] [Lo que confirma que el proceso se completó correctamente]

## Errores comunes y cómo evitarlos
[Lista de errores frecuentes con solución]
```

## Frameworks & Best Practices

[COPIAR VERBATIM todos los frameworks de /tmp/process-docs-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/legal-ops/process-docs.md
git commit -m "feat: add process-docs agent (legal-ops)"
```

---

### Task 26: proposal-generation.md

**Files:**
- Create: `Startup-Cofounder/agents/legal-ops/proposal-generation.md`

- [ ] **Step 1: Fetch fuente**

```bash
gh api /repos/shawnpang/startup-founder-skills/contents/skills/proposal-generation/SKILL.md \
  --jq '.content' | base64 -d > /tmp/proposal-source.md
```

- [ ] **Step 2: Escribir archivo adaptado**

Escribir `Startup-Cofounder/agents/legal-ops/proposal-generation.md`:

```markdown
---
name: proposal-generation
description: Cuando el founder necesita crear una propuesta comercial, SOW o contrato de servicios. Activa con "propuesta comercial", "proposal", "SOW", "statement of work", "presupuesto formal", "contrato de servicios".
domain: legal-ops
reads: [inputs/]
outputs: [outputs/proposal.md]
---

# Proposal Generation Agent

## Cuándo usar
- Un cliente potencial ha pedido una propuesta formal con pricing y timeline
- El founder quiere formalizar un acuerdo con un partner o proveedor con un SOW
- El founder necesita un contrato de servicios rápido para empezar a trabajar

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Emails o notas de la conversación con el cliente (para entender el scope)
- Brief del cliente si lo hay
- Propuestas anteriores (para mantener formato consistente)
- Tarifas y estructura de precios del founder

Si inputs/ está vacío, pregunta: "¿Qué tipo de documento necesitas — propuesta comercial, SOW o contrato de servicios? ¿Cuál es el scope y el importe aproximado?"

## Workflow

1. **Leer inputs/** — Extrae: tipo de documento, partes involucradas, scope del trabajo, importe y estructura de pago, timeline, y cualquier requerimiento especial (propiedad intelectual, confidencialidad, exclusividad).

2. **Diagnosticar** — Determina qué cláusulas son críticas para este tipo de engagement. Identifica si hay requerimientos de jurisdicción específicos o si aplica GDPR (para datos de usuarios del cliente).

3. **Producir output** — Escribe `outputs/proposal.md` con el documento completo listo para enviar o convertir a PDF.

## Output Format

`outputs/proposal.md`:

```
# Propuesta / SOW — [Empresa cliente]
*Fecha: [fecha] | Válida hasta: [fecha + 30 días]*

## Partes
- **Proveedor:** [Nombre empresa, dirección, CIF]
- **Cliente:** [Nombre empresa, dirección, CIF]

## Alcance del trabajo
[Descripción detallada de entregables con criterios de aceptación]

## Timeline y fases
| Fase | Entregable | Fecha | Hito de pago |
|---|---|---|---|

## Condiciones económicas
- **Importe total:** €X (IVA no incluido)
- **Forma de pago:** [X% firma / X% entrega / X% cierre]
- **Condiciones:** Net-30 desde factura

## Propiedad intelectual
[Quién posee qué al finalizar el trabajo]

## Confidencialidad
[Duración y alcance]

## Terminación
[Condiciones de cancelación y penalizaciones]

## Aceptación
[Bloque de firmas]
```

## Frameworks & Best Practices

[COPIAR VERBATIM "Key Clauses Reference", reglas de jurisdicción EU/US/DACH y cualquier otro framework de /tmp/proposal-source.md]
```

- [ ] **Step 3: Commit**

```bash
git add Startup-Cofounder/agents/legal-ops/proposal-generation.md
git commit -m "feat: add proposal-generation agent (legal-ops)"
```

---

## Fase 5 — Verificación final

### Task 27: Verificar la suite completa

**Files:** (solo lectura)

- [ ] **Step 1: Verificar count de archivos**

```bash
find Startup-Cofounder/agents -name "*.md" | sort
```

Expected output: 26 archivos .md (9 fundraising + 5 product + 7 marketing + 5 legal-ops).

- [ ] **Step 2: Verificar que todos tienen el patrón correcto**

```bash
for f in $(find Startup-Cofounder/agents -name "*.md"); do
  echo "=== $f ==="
  grep -c "reads: \[inputs/\]" "$f" && echo "✓ reads inputs" || echo "✗ FALTA reads"
  grep -c "## Qué leer en inputs" "$f" && echo "✓ seccion inputs" || echo "✗ FALTA seccion"
  grep -c "outputs/" "$f" && echo "✓ outputs path" || echo "✗ FALTA outputs"
done
```

Todos los archivos deben mostrar ✓ en los tres checks.

- [ ] **Step 3: Verificar README referencia los 26 agentes**

```bash
grep -c "@agents/" Startup-Cofounder/README.md
```

Expected: 26

- [ ] **Step 4: Commit final**

```bash
git add Startup-Cofounder/
git commit -m "feat: complete Startup-Cofounder suite (26 agents)"
```
