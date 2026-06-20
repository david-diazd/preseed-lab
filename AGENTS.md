# preseed-lab — Claude Code Startup Assistant (Pre-Seed)

Herramienta para ayudar a founders a preparar su ronda Pre-Seed mediante agentes especializados en Claude Code.

---

## Estructura del repositorio

```
/inputs        → Documentos del usuario (ejemplos incluidos; PDFs y XLSXs gitignored)
/outputs       → Resultados generados por los agentes (gitignored)
/skills        → 5 skills comunes compartidas entre roles
/CEO           → 24 agentes + 4 skills (estrategia, fundraising, legal, mercado)
/CTO           → 13 agentes + 4 skills (producto, ingeniería, tecnología)
/CMO           → 14 agentes + 4 skills (marketing, growth, brand)
/VC-agent      → 11 agentes de simulación VC + 3 perfiles de feedback
README.md      → Documentación principal
```

El usuario corre `claude` desde la raíz del repo. Para usar un agente, referencia el archivo markdown correspondiente. Los paths `inputs/` y `outputs/` resuelven desde la raíz.

---

## Instrucciones generales

- Al ejecutar un agente, lee primero el archivo `.md` del agente para entender su workflow, qué buscar en `inputs/` y qué formato de output producir.
- Los documentos del usuario están en `inputs/`. Nunca modifiques archivos en `inputs/`.
- Los resultados se escriben en `outputs/`. Usa el nombre de archivo indicado en el frontmatter `outputs:` de cada agente.
- Si `inputs/` está vacío, sigue la instrucción del agente (normalmente, preguntar al usuario qué necesita).
- Los agentes que tienen `web_search: true` en su frontmatter requieren buscar información actualizada en internet.
- Las skills encadenan varios agentes; sigue el campo `chains:` del frontmatter para el orden.

---

## Agentes por rol

### CEO (24 agentes)
| Dominio | Agentes |
|---|---|
| `CEO/agents/fundraising/` | pitch-deck, financial-model, data-room, investor-research, fundraising-email, accelerator-application, board-update, market-research, competitive-analysis |
| `CEO/agents/legal/` | contract-review, terms-of-service, privacy-policy, process-docs, proposal-generation |
| `CEO/agents/strategy/` | vision-mission, okr-planning, business-model-canvas, hiring-plan, cap-table, term-sheet-review |
| `CEO/agents/market/` | market-sizing, industry-analysis, customer-discovery, market-entry |

### CTO (13 agentes)
| Dominio | Agentes |
|---|---|
| `CTO/agents/product/` | prd-writing, mvp-scoping, roadmap-planning, user-research-synthesis, feedback-synthesis |
| `CTO/agents/engineering/` | architecture-review, tech-stack-evaluation, technical-debt, api-design, security-checklist, devops-setup, scalability-plan, technical-due-diligence |

### CMO (14 agentes)
| Dominio | Agentes |
|---|---|
| `CMO/agents/marketing/` | content-strategy, launch-strategy, landing-page, cold-outreach, sales-script, social-content, seo-technical |
| `CMO/agents/growth/` | growth-model, analytics-setup, pricing-strategy, partnership-strategy |
| `CMO/agents/brand/` | brand-positioning, messaging-framework, paid-ads-plan |

### VC-agent (11 agentes)
| Archivo | Función |
|---|---|
| `VC-agent/agents/pitch-deck-analyst.md` | Narrativa, estructura, storytelling |
| `VC-agent/agents/market-analyst.md` | TAM/SAM/SOM, competencia, timing |
| `VC-agent/agents/financial-analyst.md` | Unit economics, proyecciones, burn rate |
| `VC-agent/agents/vc-partner.md` | Simulación de decisión inversora |
| `VC-agent/agents/growth-expert.md` | GTM, tracción, estrategias de crecimiento |
| `VC-agent/agents/founder-validator.md` | Validación del equipo (web search) |
| `VC-agent/agents/competitive-intelligence.md` | Landscape competitivo real (web search) |
| `VC-agent/agents/market-validator.md` | Fact-check de claims de mercado (web search) |
| `VC-agent/agents/checklist-evaluator.md` | Checklist de readiness Pre-Seed (10 criterios) |
| `VC-agent/agents/global-scorer.md` | Score global ponderado + detección de deal-breakers |
| `VC-agent/agents/vc-qa-simulator.md` | Simulación de reunión con inversor |

---

## Skills

### Comunes (compartidas)
| Skill | Función |
|---|---|
| `skills/weekly-report.md` | Reporte semanal de progreso |
| `skills/swot-analysis.md` | Análisis SWOT completo |
| `skills/decision-framework.md` | Framework de decisión estructurada |
| `skills/meeting-notes.md` | Notas de reunión + action items |
| `skills/competitor-monitor.md` | Monitoreo de competidores (web search) |

### CEO
| Skill | Función |
|---|---|
| `CEO/skills/fundraising-pipeline.md` | Pipeline de fundraising end-to-end |
| `CEO/skills/board-meeting-prep.md` | Preparación de board meeting |
| `CEO/skills/investor-update.md` | Email de investor update mensual |
| `CEO/skills/strategic-review.md` | Revisión estratégica trimestral |

### CTO
| Skill | Función |
|---|---|
| `CTO/skills/sprint-planning.md` | Planificación de sprint |
| `CTO/skills/incident-postmortem.md` | Post-mortem de incidentes |
| `CTO/skills/tech-radar.md` | Radar tecnológico trimestral |
| `CTO/skills/architecture-decision-record.md` | ADRs formales |

### CMO
| Skill | Función |
|---|---|
| `CMO/skills/campaign-launch.md` | Checklist de lanzamiento de campaña |
| `CMO/skills/content-calendar.md` | Calendario de contenido mensual |
| `CMO/skills/performance-report.md` | Reporte de rendimiento de marketing |
| `CMO/skills/ab-test-analysis.md` | Análisis de A/B tests |

---

## Flujo de uso

1. El usuario sube sus documentos a `inputs/`
2. Abre Claude Code desde la raíz del repo
3. Referencia el agente deseado (e.g. lee `CEO/agents/strategy/okr-planning.md` y sigue su workflow)
4. Los resultados se guardan en `outputs/`

---

## Convenciones

- Escribe outputs en español salvo que el usuario pida otro idioma.
- Usa el formato markdown especificado en cada agente — no inventes formatos propios.
- Si el agente tiene sección "Related Skills", menciónalas al usuario al final del output.
- Ante la duda, pregunta antes de asumir.

---

## Contexto

Parte de **Startup Canarias** — iniciativa para impulsar el ecosistema emprendedor en Canarias.
