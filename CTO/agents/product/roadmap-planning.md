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
- El founder necesita priorizar con constraint de recursos limitados

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

- **Outcomes over outputs.** "Build advanced search filters" is an output. "Enable customers to find products 50% faster through intuitive discovery" is an outcome. Output-focused roadmaps create false precision and misalign teams around features rather than results.
- **The outcome statement format.** "Enable [customer segment] to [desired customer outcome] so that [business impact]." This forces clarity on who benefits, what changes, and why it matters.
- **The "So What?" test.** If you cannot articulate the outcome a feature drives, keep asking "So what?" until you reach real customer or business value. Multiple outputs may achieve one outcome -- focus on the outcome.
- **RICE scoring.**
  - **Reach:** How many users/accounts will this affect per quarter?
  - **Impact:** On a scale of 0.25 (minimal) to 3 (massive), how much will this move the target metric?
  - **Confidence:** As a percentage, how sure are you about reach and impact estimates?
  - **Effort:** Person-weeks required.
  - **Score:** (Reach x Impact x Confidence) / Effort.
- **Three-horizon structure.** Now/Next/Later avoids the false precision of Gantt charts. Commit to Now, plan for Next, explore Later.
- **Outcome roadmaps are resilient to change.** Because they describe the "why" rather than the "what," they survive strategy pivots and new information better than feature roadmaps.
- **Say no explicitly.** A roadmap is defined as much by what it excludes. Maintain a "Not Doing" list and share the reasoning.
- **Align with OKRs.** Every outcome statement should map to a company or product OKR. Orphan initiatives signal misalignment.
- **Revisit quarterly.** Roadmaps older than one quarter are stale. Build in review cadences.
- **Stage-appropriate planning.**
  - **Pre-PMF:** Roadmaps should be 4-6 week sprints focused on learning. No 12-month plans.
  - **Post-PMF:** Quarterly roadmaps tied to OKRs. Balance growth features with infrastructure and debt.
  - **Scaling:** Semi-annual roadmaps with cross-team coordination. Dependencies become the hard problem.
- **Avoid roadmap theater.** Do not create elaborate roadmaps to appease stakeholders if the team lacks the capacity or conviction to execute.
