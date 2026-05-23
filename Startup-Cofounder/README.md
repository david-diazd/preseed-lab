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
