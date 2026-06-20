# CEO — Estrategia, Fundraising, Legal & Mercado

Suite de agentes y skills para el rol de CEO/Founder. Cubre estrategia empresarial, fundraising, legal, y análisis de mercado.

## Cómo funciona

1. Pon tus documentos en `inputs/` (raíz del repo)
2. Invoca el agente con `@CEO/agents/<dominio>/<nombre>.md`
3. Los resultados se guardan en `outputs/`

## Agentes disponibles

### Fundraising (9 agentes)
| Agente | Cuándo usarlo |
|---|---|
| `@CEO/agents/fundraising/pitch-deck.md` | Crear o mejorar tu pitch deck slide a slide |
| `@CEO/agents/fundraising/financial-model.md` | Revisar P&L, unit economics y proyecciones |
| `@CEO/agents/fundraising/data-room.md` | Preparar data room para due diligence |
| `@CEO/agents/fundraising/investor-research.md` | Construir lista de inversores tiered |
| `@CEO/agents/fundraising/fundraising-email.md` | Cold outreach, follow-ups e investor updates |
| `@CEO/agents/fundraising/accelerator-application.md` | Essays para YC, Techstars y otros programas |
| `@CEO/agents/fundraising/board-update.md` | Updates mensuales/trimestrales a inversores |
| `@CEO/agents/fundraising/market-research.md` | TAM/SAM/SOM con metodología rigurosa |
| `@CEO/agents/fundraising/competitive-analysis.md` | Landscape competitivo y posicionamiento |

### Legal (5 agentes)
| Agente | Cuándo usarlo |
|---|---|
| `@CEO/agents/legal/contract-review.md` | Revisar contratos con red flags |
| `@CEO/agents/legal/terms-of-service.md` | ToS completo para SaaS/app |
| `@CEO/agents/legal/privacy-policy.md` | Política de privacidad GDPR-ready |
| `@CEO/agents/legal/process-docs.md` | SOPs y documentación de procesos |
| `@CEO/agents/legal/proposal-generation.md` | Propuestas comerciales y SOWs |

### Strategy (6 agentes)
| Agente | Cuándo usarlo |
|---|---|
| `@CEO/agents/strategy/vision-mission.md` | Definir visión, misión y valores |
| `@CEO/agents/strategy/okr-planning.md` | OKRs trimestrales con key results medibles |
| `@CEO/agents/strategy/business-model-canvas.md` | Mapear y validar el modelo de negocio |
| `@CEO/agents/strategy/hiring-plan.md` | Planificar contrataciones y estructura de equipo |
| `@CEO/agents/strategy/cap-table.md` | Analizar cap table y simular dilución |
| `@CEO/agents/strategy/term-sheet-review.md` | Analizar term sheets recibidos |

### Market (4 agentes)
| Agente | Cuándo usarlo |
|---|---|
| `@CEO/agents/market/market-sizing.md` | Calcular TAM/SAM/SOM con rigor (web search) |
| `@CEO/agents/market/industry-analysis.md` | Análisis de industria con Porter y PESTEL (web search) |
| `@CEO/agents/market/customer-discovery.md` | Diseñar entrevistas y sintetizar customer discovery |
| `@CEO/agents/market/market-entry.md` | Planificar entrada a nuevos mercados (web search) |

## Skills

| Skill | Cuándo usarlo |
|---|---|
| `@CEO/skills/fundraising-pipeline.md` | Gestionar pipeline de inversores end-to-end |
| `@CEO/skills/board-meeting-prep.md` | Preparar materiales para reunión de board |
| `@CEO/skills/investor-update.md` | Generar email de investor update mensual |
| `@CEO/skills/strategic-review.md` | Revisión estratégica trimestral |

## Flujo recomendado para fundraising

1. `@CEO/agents/market/market-sizing.md` — valida el tamaño de mercado
2. `@CEO/agents/fundraising/pitch-deck.md` — mejora el deck
3. `@CEO/agents/fundraising/financial-model.md` — valida los números
4. `@CEO/agents/fundraising/competitive-analysis.md` — refuerza competencia
5. `@CEO/agents/fundraising/data-room.md` — prepara el data room
6. `@CEO/agents/fundraising/investor-research.md` — construye la lista
7. `@CEO/skills/fundraising-pipeline.md` — gestiona el pipeline
