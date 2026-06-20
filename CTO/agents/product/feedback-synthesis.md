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

### Opportunities Over Features
Never let customers design solutions. Prioritize opportunities (problems), not features. When a user says "I want a Gantt chart," the underlying opportunity might be "I need to visualize project timelines and communicate status to stakeholders." Always dig for the job-to-be-done behind the request.

### Opportunity Score (Dan Olsen)
Score each theme: Opportunity Score = Importance x (1 - Satisfaction), normalized to 0-1. This surfaces problems that are both important and underserved. A high-importance, high-satisfaction area is already well-served and should not be prioritized over a high-importance, low-satisfaction gap.

### Signal vs. Noise Rules
- **One customer saying it is not a pattern.** Require 3+ independent mentions of a theme before treating it as a signal. Exception: if the one customer is a whale account citing it as a churn risk.
- **Recency bias check.** A flood of recent feedback about one issue can overshadow a persistent problem. Always compare against the prior period.
- **Loudest does not equal most important.** Power users and vocal customers generate disproportionate feedback. Weight by segment size and revenue contribution, not volume alone.
- **Praise is data too.** Track what users love. Knowing your strengths prevents you from accidentally breaking them during a redesign.

### Assumption Testing
For each top-priority opportunity, identify the highest-risk assumption and design the cheapest possible test. Do not build the full solution to validate an assumption that could be tested with a prototype, survey, or Wizard of Oz experiment.

### Source-Specific Guidance
| Source | Strengths | Watch Out For |
|--------|-----------|---------------|
| Support tickets | High signal, specific problems | Skews toward bugs, misses satisfied users |
| NPS/surveys | Broad coverage, quantifiable | Low response rates can bias results |
| Feature request boards | Organized, vote counts available | Power users dominate voting |
| Sales call notes | Revenue-adjacent, prospect perspective | Prospects request features they may never use |
| App store reviews | Public, includes competitor comparisons | Skews negative, vague complaints |
| Social media | Unfiltered, real-time | Noisy, hard to segment |

### Avoiding Common Mistakes
- **Cherry-picking quotes** that support a pre-existing hypothesis. Present the full distribution, including contradictory feedback.
- **Conflating frequency with importance.** A low-frequency issue that causes churn matters more than a high-frequency annoyance users tolerate.
- **Delivering data without recommendations.** A theme map without action items is a report, not a synthesis. Always end with what to do next.
- **Ignoring the silent majority.** Users who never complain may be happy or disengaged. Segment analysis helps distinguish the two.

## Related Skills
- `user-research-synthesis` -- Chain when feedback analysis reveals gaps that need dedicated user research (interviews, usability tests).
- `churn-analysis` -- Chain when feedback themes correlate with churn patterns and need deeper retention analysis.
- `prd-writing` -- Chain when a clear opportunity emerges from the synthesis and needs to be specced into a PRD.

## Examples

### Example 1: Feature request prioritization
**User:** "Our feature request board has 150 items. Help me figure out what to build next quarter."

**Good output excerpt:**
> **Executive Summary:** 150 requests cluster into 9 themes. The top opportunity is not the most-requested feature (SSO, 34 votes) but the most underserved need: "real-time collaboration on shared documents" (Opportunity Score: 0.82). SSO scores lower (0.45) because existing workarounds satisfy most users adequately.
>
> **Opportunity 1: Real-time collaboration**
> - **Rationale:** 22 requests across 4 segments. Cited as expansion blocker in 3 enterprise deals worth $85K ARR. Current satisfaction: 2/10.
> - **Alternative solutions:** (a) Full real-time editing, (b) Lightweight commenting and presence indicators, (c) Async review workflow with notifications
> - **High-risk assumption:** Users want simultaneous editing, not just awareness of others' changes
> - **Cheapest test:** Add presence indicators only (show who is viewing a document) and measure whether collaboration-related tickets decrease

### Example 2: Multi-source synthesis
**User:** "We have 200 support tickets, 50 NPS responses, and notes from 10 customer interviews from last month. What are customers telling us?"

**Good output excerpt:**
> **Theme 1: CSV export broken for large datasets** (Opportunity Score: 0.91)
> - 47 support tickets, 8 NPS detractors, 3 interviews. Users hitting the 10K row limit work around it by splitting exports manually.
> - **Strategic alignment:** High -- data export is core to our "open platform" positioning.
> - **Cheapest test:** Not needed; this is a clear bug/limitation. Fix directly.
> - **Quick win:** Increase CSV export limit to 100K rows (engineering estimate: 2 days).
