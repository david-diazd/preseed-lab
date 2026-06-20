# CTO — Producto, Ingeniería & Tecnología

Suite de agentes y skills para el rol de CTO/Technical Cofounder. Cubre producto, arquitectura, ingeniería y operaciones técnicas.

## Cómo funciona

1. Pon tus documentos en `inputs/` (raíz del repo)
2. Invoca el agente con `@CTO/agents/<dominio>/<nombre>.md`
3. Los resultados se guardan en `outputs/`

## Agentes disponibles

### Product (5 agentes)
| Agente | Cuándo usarlo |
|---|---|
| `@CTO/agents/product/prd-writing.md` | PRD estructurado de features |
| `@CTO/agents/product/mvp-scoping.md` | Definir scope v1 vs defer |
| `@CTO/agents/product/roadmap-planning.md` | Roadmap priorizado con dependencias |
| `@CTO/agents/product/user-research-synthesis.md` | Sintetizar entrevistas en insights |
| `@CTO/agents/product/feedback-synthesis.md` | Patrones de feedback en acciones |

### Engineering (8 agentes)
| Agente | Cuándo usarlo |
|---|---|
| `@CTO/agents/engineering/architecture-review.md` | Definir o revisar arquitectura técnica |
| `@CTO/agents/engineering/tech-stack-evaluation.md` | Elegir o evaluar el stack tecnológico |
| `@CTO/agents/engineering/technical-debt.md` | Evaluar y priorizar deuda técnica |
| `@CTO/agents/engineering/api-design.md` | Diseñar APIs REST/GraphQL |
| `@CTO/agents/engineering/security-checklist.md` | Auditar seguridad y compliance |
| `@CTO/agents/engineering/devops-setup.md` | Configurar CI/CD e infraestructura |
| `@CTO/agents/engineering/scalability-plan.md` | Planificar escalabilidad del sistema |
| `@CTO/agents/engineering/technical-due-diligence.md` | Prepararse para due diligence técnico |

## Skills

| Skill | Cuándo usarlo |
|---|---|
| `@CTO/skills/sprint-planning.md` | Planificar sprint con capacidad del equipo |
| `@CTO/skills/incident-postmortem.md` | Post-mortem estructurado de incidentes |
| `@CTO/skills/tech-radar.md` | Evaluar tecnologías emergentes (web search) |
| `@CTO/skills/architecture-decision-record.md` | Documentar decisiones de arquitectura |

## Flujo recomendado para nuevo producto

1. `@CTO/agents/product/mvp-scoping.md` — define el MVP
2. `@CTO/agents/engineering/tech-stack-evaluation.md` — elige el stack
3. `@CTO/agents/engineering/architecture-review.md` — diseña la arquitectura
4. `@CTO/agents/product/prd-writing.md` — documenta el PRD
5. `@CTO/agents/product/roadmap-planning.md` — crea el roadmap
6. `@CTO/skills/sprint-planning.md` — planifica el primer sprint
