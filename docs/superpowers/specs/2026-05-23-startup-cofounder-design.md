# Startup-Cofounder — Design Spec

**Date:** 2026-05-23  
**Status:** Approved

---

## Overview

Startup-Cofounder es una suite de 26 agentes para Claude Code que ayuda a founders a mejorar y producir su documentación de startup. A diferencia del VC-agent (que evalúa), estos agentes **absorben los documentos existentes del founder, los diagnostican y producen versiones mejoradas directamente**.

Opera de forma totalmente independiente del VC-agent.

---

## Principio de diseño central

**No hay startup-context.md.** El founder no rellena ningún formulario. En su lugar, deposita sus documentos reales (Excel con P&L, Word con deck, PDFs, CSVs) en `inputs/`. Cada agente lee `inputs/`, extrae la información relevante para su dominio, y trabaja sobre ella.

Flujo universal de todos los agentes:
1. **Leer `inputs/`** — escanea y lee todos los archivos disponibles, extrae info relevante para el dominio. Si falta algo crítico, pregunta antes de continuar.
2. **Diagnosticar** — identifica gaps y puntos débiles aplicando el framework del dominio.
3. **Producir output** — escribe la versión mejorada/completa en `outputs/`.

---

## Estructura de carpetas

```
Startup-Cofounder/
├── inputs/                        ← el founder pone aquí sus docs (PDF, Excel, Word, PPT, CSV...)
├── outputs/                       ← versiones mejoradas generadas por los agentes
├── agents/
│   ├── fundraising/
│   │   ├── pitch-deck.md
│   │   ├── financial-model.md
│   │   ├── data-room.md
│   │   ├── investor-research.md
│   │   ├── fundraising-email.md
│   │   ├── accelerator-application.md
│   │   ├── board-update.md
│   │   ├── market-research.md
│   │   └── competitive-analysis.md
│   ├── product/
│   │   ├── prd-writing.md
│   │   ├── mvp-scoping.md
│   │   ├── roadmap-planning.md
│   │   ├── user-research-synthesis.md
│   │   └── feedback-synthesis.md
│   ├── marketing/
│   │   ├── content-strategy.md
│   │   ├── launch-strategy.md
│   │   ├── landing-page.md
│   │   ├── cold-outreach.md
│   │   ├── sales-script.md
│   │   ├── social-content.md
│   │   └── seo-technical.md
│   └── legal-ops/
│       ├── contract-review.md
│       ├── terms-of-service.md
│       ├── privacy-policy.md
│       ├── process-docs.md
│       └── proposal-generation.md
└── README.md
```

---

## Catálogo de agentes

### Fundraising (9 agentes)

| Agente | Fuente | Output |
|---|---|---|
| `pitch-deck.md` | shawnpang adaptado | Deck completo reescrito slide a slide en markdown |
| `financial-model.md` | Creado desde cero | P&L, unit economics, proyecciones 18-36m con supuestos explícitos |
| `data-room.md` | shawnpang adaptado | Checklist DD con estado (existe/falta/desactualizado) + drafts de docs faltantes |
| `investor-research.md` | shawnpang adaptado | Lista de inversores tiered (T1/T2/T3) con warm paths |
| `fundraising-email.md` | shawnpang adaptado | Cold outreach, warm intro, follow-ups, investor updates |
| `accelerator-application.md` | shawnpang adaptado | Essays y respuestas para YC, Techstars, y otros programas |
| `board-update.md` | shawnpang adaptado | Update mensual/trimestral estructurado para inversores |
| `market-research.md` | shawnpang adaptado | TAM/SAM/SOM con metodología top-down + bottom-up reconciliados |
| `competitive-analysis.md` | shawnpang adaptado | Landscape con perfiles de competidores, gaps y recomendación de posicionamiento |

### Producto & Estrategia (5 agentes)

| Agente | Fuente | Output |
|---|---|---|
| `prd-writing.md` | shawnpang adaptado | PRD estructurado de 8 secciones listo para ingeniería |
| `mvp-scoping.md` | shawnpang adaptado | Scope v1 vs defer, criterios de lanzamiento mínimo viable |
| `roadmap-planning.md` | shawnpang adaptado | Roadmap priorizado con dependencias y fases |
| `user-research-synthesis.md` | shawnpang adaptado | Síntesis de entrevistas/notas en insights accionables |
| `feedback-synthesis.md` | shawnpang adaptado | Patrones de feedback de usuarios en acciones priorizadas |

### Marketing & Crecimiento (7 agentes)

| Agente | Fuente | Output |
|---|---|---|
| `content-strategy.md` | shawnpang adaptado | Estrategia de contenido con calendario editorial |
| `launch-strategy.md` | shawnpang adaptado | Plan de lanzamiento con canales, timing y métricas |
| `landing-page.md` | shawnpang adaptado | Copy completo de landing page optimizado para conversión |
| `cold-outreach.md` | shawnpang adaptado | Secuencias de outreach B2B personalizadas |
| `sales-script.md` | shawnpang adaptado | Script de demo/ventas con manejo de objeciones |
| `social-content.md` | shawnpang adaptado | Posts para LinkedIn/Twitter del founder (voz y calendario) |
| `seo-technical.md` | shawnpang adaptado | Auditoría SEO + plan de keywords y estructura de contenido |

### Legal & Operaciones (5 agentes)

| Agente | Fuente | Output |
|---|---|---|
| `contract-review.md` | shawnpang adaptado | Revisión de contratos con red flags marcados y sugerencias |
| `terms-of-service.md` | shawnpang adaptado | ToS completo para SaaS/app |
| `privacy-policy.md` | shawnpang adaptado | Política de privacidad GDPR-ready |
| `process-docs.md` | shawnpang adaptado | SOPs y documentación de procesos internos |
| `proposal-generation.md` | shawnpang adaptado | Propuestas comerciales y SOWs con cláusulas clave |

---

## Formato de cada agente

Cada archivo `.md` sigue esta estructura:

```markdown
---
name: <nombre>
description: <cuándo activar este agente — trigger phrases>
domain: <fundraising | product | marketing | legal-ops>
reads: [inputs/]
outputs: [outputs/]
---

# <Nombre del Agente>

## Cuándo usar
...

## Qué leer en inputs/
Tipos de documentos relevantes que buscar en inputs/ para este dominio.
Si no hay ninguno disponible, qué preguntar al founder.

## Workflow
1. Leer inputs/ — ...
2. Diagnosticar — ...
3. Producir output — ...

## Output format
Descripción exacta del archivo que se escribe en outputs/.

## Frameworks & Best Practices
...
```

---

## Fuente de contenido

- **24 agentes** — adaptados de [shawnpang/startup-founder-skills](https://github.com/shawnpang/startup-founder-skills) (MIT). Se adaptan cambiando el workflow de "construir desde cero via entrevista" a "leer inputs del founder y mejorar". Los frameworks, best practices y output formats se conservan (son el valor principal del repo).
- **1 agente creado desde cero** — `financial-model.md`: no existe en el repo de referencia. Cubre P&L, unit economics, burn rate, runway y proyecciones 18-36m.
- **README.md** — creado desde cero, explica la estructura y cómo usar cada categoría.

---

## Lo que NO incluye (v1)

- Agentes de recruiting (job-description, interview-kit, employer-brand) — quedan para v2
- Integración con el VC-agent — es independiente por diseño
- Startup-context.md — reemplazado por inputs/ dinámico
- Automatización de outputs a PPTX/XLSX — queda para v2
