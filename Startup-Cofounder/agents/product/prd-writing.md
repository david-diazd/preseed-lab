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

- **Problem before solution.** Spend 40% of the document on sections 1-5 (the "why") before touching section 7 (the "what"). A PRD that jumps to the solution is a spec, not a PRD.
- **One objective, not five.** A PRD with multiple objectives is multiple PRDs. Split them. Each PRD should have a single primary metric it moves.
- **Market segments defined by needs.** Describe who this is for based on the problems they face and jobs they hire the product to do, not by demographics or firmographics alone.
- **Value Proposition clarity.** For each segment, explicitly state the customer jobs addressed, gains provided, and pains eliminated. Use the Value Curve to show where you differentiate from competitors.
- **Data-driven specificity.** Replace vague language with specific numbers. "Improve retention" is not a metric; "Increase D7 retention from 25% to 35% within 8 weeks of launch" is.
- **Scope creep guard.** Explicitly list what is NOT in scope. Revisit the out-of-scope list when stakeholders propose additions.
- **Relative timeframes over dates.** Use phases and relative windows rather than exact calendar dates. This prevents false precision and allows flexibility.
- **Assumption tracking.** List the top 3 assumptions underlying the PRD. For each, state supporting evidence and what would invalidate it.
- **Audience awareness.** Engineers need technical constraints and edge cases. Designers need user flows and personas. Executives need the summary and metrics. Write for all three in a single document.
- **Living document.** State the PRD version and last-updated date. PRDs that never change were never read.
- **Lightweight PRD triggers:** pre-PMF exploration, hackathon projects, internal tools, experiments with <2 week timelines.
- **Full PRD triggers:** cross-team initiatives, features with external dependencies, anything touching payments or compliance.

## Related Skills
- `roadmap-planning` — Chain after writing PRDs to slot the initiative into the broader roadmap with dependencies and timelines.
- `mvp-scoping` — Chain before writing a PRD to determine what to include in v1 vs. defer to later releases.
- `user-research-synthesis` — Chain before writing a PRD to ground the Background and Market Segments sections in real customer data.

## Examples

### Example 1: Lightweight PRD prompt
**User:** "We need a PRD for adding Slack notifications to our project management tool."

**Good output excerpt:**
> **Summary:** Add configurable Slack notifications so that teams using ProjectFlow are alerted to task updates, mentions, and deadline changes without leaving their primary communication tool. This addresses the #1 feature request from our Q3 customer survey (38% of respondents).
>
> **Objective:** Enable team leads on paid plans to receive real-time project updates in Slack, resulting in a 20% reduction in average response time to task assignments within 6 weeks of launch.
>
> **Market Segment:** Teams of 10+ coordinating across tools, whose primary pain is context-switching between project management and communication platforms.
>
> **Out of scope:** Microsoft Teams integration, custom notification templates, Slack bot commands.

### Example 2: Full PRD prompt
**User:** "Write a full PRD for our new self-serve onboarding flow. We're losing 60% of signups before they complete setup."

**Good output excerpt:**
> **Background:** Current onboarding requires 7 steps and takes an average of 12 minutes. Hotjar recordings show 45% of users abandon at the "connect data source" step. Competitor X reduced their onboarding to 3 steps in Q2 and reported a 2x improvement in activation. Our support team handles 30+ onboarding tickets per week, costing approximately $4,500/month.
>
> **Value Proposition:** Eliminate the "connect data source" friction by offering a sample dataset that lets users experience core value before committing to integration. Differentiated from Competitor X which still requires immediate data connection.
>
> **Release:**
> - Phase 1: Internal dogfood with the team (2 weeks)
> - Phase 2: 10% of new signups via feature flag
> - Phase 3: 50% rollout if activation rate > 45%
> - Phase 4: GA if no P0 bugs and support ticket volume decreases
> - Rollback trigger: activation rate drops below current 40% baseline
