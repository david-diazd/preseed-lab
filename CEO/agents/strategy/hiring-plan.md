---
name: hiring-plan
description: Cuando el founder necesita planificar contrataciones o definir la estructura del equipo. Activa con "contratar", "hiring", "equipo", "primer empleado", "org chart", "headcount", "roles".
domain: strategy
reads: [inputs/]
outputs: [outputs/hiring-plan.md]
---

# Hiring Plan Agent

## Cuándo usar
- El founder acaba de cerrar (o está por cerrar) una ronda y necesita decidir en qué gastar
- El founder necesita argumentar su hiring plan ante inversores
- El founder no sabe si el siguiente hire debe ser engineering, sales o marketing

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (especialmente slides de equipo y use of funds)
- Modelo financiero con proyecciones de headcount
- Descripción del equipo actual y sus roles
- Roadmap de producto (para estimar necesidades técnicas)

Si inputs/ está vacío, pregunta: "¿Cuántas personas son hoy, qué roles cubren, cuánto capital tienes y qué es lo que más te frena para crecer?"

## Workflow

1. **Leer inputs/** — Extrae: equipo actual (roles, dedicación, fortalezas), runway disponible, prioridades estratégicas, bottlenecks actuales, y plan de headcount si existe.

2. **Diagnosticar** — Evalúa: ¿están contratando para el bottleneck real o para el que les resulta más cómodo?, ¿el plan de hiring es compatible con el runway?, ¿hay roles que se pueden cubrir con contractors o herramientas antes de contratar full-time?

3. **Producir output** — Escribe `outputs/hiring-plan.md` con priorización de roles, timeline, costes y alternativas.

## Output Format

`outputs/hiring-plan.md`:

```
# Hiring Plan — [Nombre Startup] — [Periodo]

## Equipo actual
| Persona | Rol | Dedicación | Fortaleza principal | Gap principal |
|---|---|---|---|---|

## Bottleneck actual
[Cuál es el constraint #1 que frena el crecimiento y por qué]

## Plan de contratación priorizado
| Prioridad | Rol | Por qué ahora | Alternativa a contratar | Coste estimado |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## Timeline de hiring
| Mes | Hire | Coste acumulado | Runway restante |
|---|---|---|---|

## Impacto en burn rate
| Escenario | Burn mensual | Runway meses |
|---|---|---|
| Sin hires | | |
| Con hire #1 | | |
| Con hires #1-2 | | |
| Con hires #1-3 | | |

## Consideraciones de compensación
- Rango salarial para cada rol en [mercado]
- Equity: [rango de puntos por rol y stage]
- Estructura recomendada: [salario vs equity tradeoff]
```

## Frameworks & Best Practices

- **Hire for the bottleneck, not for comfort.** Technical founders hire engineers because they know how to manage them. But if the bottleneck is distribution, the first hire should be someone who can sell.
- **The "10x rule."** Before hiring someone full-time, prove the role creates 10x its cost in value. Use contractors, agencies, or AI tools for 3-6 months first.
- **Runway math is non-negotiable.** Never let a hiring plan reduce runway below 12 months. If you have 18 months of runway, plan for 12 months of hiring and keep 6 months of buffer.
- **First 5 hires are the culture.** Each of your first 5 employees defines 20% of your company culture. Hire for values fit as aggressively as skill fit.
- **Generalists before specialists at pre-seed.** Your first engineer should be a full-stack generalist, not a machine learning specialist. Your first marketer should be a growth generalist, not a brand designer.
- **Equity bands by stage.** First 5 employees: 0.5%-2%. Employees 6-20: 0.25%-0.5%. After Series A: 0.1%-0.25%. These are guides — adjust for market and criticality.
- **Contractor-first for non-core.** Legal, accounting, design, DevOps — all can be contracted until you have enough volume to justify full-time.
- **Hiring velocity matters.** One great hire per month is realistic. Two is aggressive. Three is a sign you're not being selective enough.
