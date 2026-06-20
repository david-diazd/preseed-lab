---
name: sprint-planning
description: Planifica el sprint con priorización y capacidad del equipo. Activa con "sprint planning", "planificar sprint", "qué hacemos esta semana", "backlog", "priorizar tareas".
type: skill
scope: CTO
chains: [CTO/agents/product/roadmap-planning, CTO/agents/product/mvp-scoping]
reads: [inputs/]
outputs: [outputs/sprint-plan.md]
---

# Sprint Planning Skill

## Cuándo usar
- Al inicio de cada sprint (semanal o bisemanal)
- Cuando hay que re-priorizar por cambio de contexto
- Para alinear al equipo técnico sobre qué construir

## Qué leer en inputs/
- Backlog o lista de tareas pendientes
- OKRs o prioridades del trimestre
- Feedback de usuarios o bugs reportados
- Capacidad del equipo (quién está disponible)

Si inputs/ está vacío, pregunta: "¿Cuántas personas están disponibles este sprint, cuánto dura el sprint, y cuáles son las 5 tareas más importantes del backlog?"

## Output Format

```
# Sprint Plan — Sprint [N] — [Fecha inicio - Fecha fin]

## Objetivo del sprint
[Una frase: qué debe ser verdad al final del sprint]

## Capacidad
| Persona | Disponibilidad | Foco |
|---|---|---|

## Tareas comprometidas
| # | Tarea | Owner | Estimación | Prioridad | Depende de |
|---|---|---|---|---|---|

## No comprometido (next sprint)
| Tarea | Por qué se difiere |
|---|---|

## Riesgos del sprint
| Riesgo | Mitigación |
|---|---|

## Definition of done
- [ ] [Criterio 1]
- [ ] [Criterio 2]
- [ ] [Criterio 3]

## Carry-over del sprint anterior
| Tarea | Razón del carry-over | Status |
|---|---|---|
```
