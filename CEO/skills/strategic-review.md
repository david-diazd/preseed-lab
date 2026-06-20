---
name: strategic-review
description: Revisión estratégica trimestral del negocio. Activa con "revisión trimestral", "quarterly review", "planificación estratégica", "review trimestral", "cómo vamos".
type: skill
scope: CEO
chains: [skills/swot-analysis, CEO/agents/strategy/okr-planning, CEO/agents/strategy/business-model-canvas]
reads: [inputs/]
outputs: [outputs/strategic-review.md]
---

# Strategic Review Skill

## Cuándo usar
- Al final de cada trimestre para evaluar progreso y planificar el siguiente
- Cuando el founder siente que hay que cambiar de dirección
- Antes de una reunión de board o planificación anual

## Qué leer en inputs/
- OKRs del trimestre y resultados
- Métricas del negocio
- Feedback de clientes e inversores
- Análisis de competidores actualizado

Si inputs/ está vacío, pregunta: "¿Cuáles eran tus objetivos este trimestre, cómo fue, y qué cambiarías?"

## Output Format

```
# Strategic Review — Q[N] [Año]

## Scorecard del trimestre
| Objetivo | Target | Resultado | Score |
|---|---|---|---|

## Qué funcionó
1. [Con evidencia y números]
2. [Siguiente]

## Qué no funcionó
1. [Con análisis de por qué]
2. [Siguiente]

## Aprendizajes clave
1. [Insight accionable]
2. [Siguiente]

## Cambios estratégicos propuestos
| Cambio | Razón | Impacto esperado | Riesgo |
|---|---|---|---|

## Prioridades Q[N+1]
1. [Prioridad #1 con métrica de éxito]
2. [Prioridad #2]
3. [Prioridad #3]

## Recursos necesarios
| Recurso | Para qué | Urgencia |
|---|---|---|

## Preguntas abiertas para el equipo
1. [Pregunta estratégica sin respuesta clara]
2. [Siguiente]
```
