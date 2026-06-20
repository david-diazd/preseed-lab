---
name: okr-planning
description: Cuando el founder necesita definir objetivos y resultados clave para el trimestre. Activa con "OKR", "objetivos", "metas trimestrales", "key results", "planificación trimestral", "qué medir".
domain: strategy
reads: [inputs/]
outputs: [outputs/okr-plan.md]
---

# OKR Planning Agent

## Cuándo usar
- El founder necesita establecer prioridades claras para el próximo trimestre
- El founder tiene demasiadas cosas en marcha y necesita foco
- El founder quiere alinear al equipo sobre qué importa y qué no

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- OKRs anteriores y resultados
- Pitch deck o plan estratégico
- Métricas actuales del negocio
- Feedback de inversores o advisors
- Roadmap del producto

Si inputs/ está vacío, pregunta: "¿Cuáles son las 3 cosas más importantes que tu startup necesita lograr en los próximos 90 días?"

## Workflow

1. **Leer inputs/** — Extrae: stage de la startup, métricas actuales (revenue, usuarios, churn), prioridades estratégicas, constraints (equipo, funding, tiempo), y OKRs anteriores si existen.

2. **Diagnosticar** — Evalúa: ¿los objetivos son demasiados? (>3 por trimestre es señal de falta de foco), ¿los KRs son realmente medibles?, ¿hay KRs de vanity metrics?, ¿los OKRs están conectados con el stage de la startup?

3. **Producir output** — Escribe `outputs/okr-plan.md` con 2-3 objetivos, cada uno con 3-4 key results medibles.

## Output Format

`outputs/okr-plan.md`:

```
# OKRs — [Nombre Startup] — Q[N] [Año]

## Contexto del trimestre
[Stage de la startup, prioridad estratégica #1, constraint principal]

## Objetivo 1: [Verbo + resultado deseado]
Propietario: [Rol]
| Key Result | Baseline | Target | Método de medición |
|---|---|---|---|
| KR 1.1 | | | |
| KR 1.2 | | | |
| KR 1.3 | | | |

## Objetivo 2: [Verbo + resultado deseado]
...

## Objetivo 3 (opcional): [Verbo + resultado deseado]
...

## NO-Goals este trimestre
[Lista explícita de cosas importantes que NO se van a hacer y por qué]

## Check-in semanal
| Semana | KR 1.1 | KR 1.2 | KR 1.3 | KR 2.1 | ... | Confidence |
|---|---|---|---|---|---|---|
```

## Frameworks & Best Practices

- **2-3 Objectives max.** Pre-seed startups have one constraint: focus. More than 3 objectives means you haven't made hard choices. The CEO's job is to say no.
- **Key Results are outcomes, not tasks.** "Launch feature X" is a task. "Achieve 100 weekly active users on feature X" is a key result. If you can check it off without measuring anything, it's not a KR.
- **70% is the target.** If you hit 100% of all KRs, they were too easy. OKRs should be ambitious enough that 70% achievement represents strong execution.
- **Stage-appropriate metrics.** Pre-seed: problem validation, user engagement, retention. Don't set revenue OKRs before product-market fit unless revenue is the validation signal.
- **Input vs output KRs.** Balance "run 30 customer interviews" (input — controllable) with "achieve 40% D7 retention" (output — what matters). Pure input KRs are safe but uninformative. Pure output KRs are honest but can feel uncontrollable.
- **NO-Goals are as important as goals.** Explicitly list what you're NOT doing this quarter. This prevents drift and gives the team permission to say no.
- **Weekly check-ins, not quarterly reviews.** OKRs without weekly scoring are New Year's resolutions. Track confidence (green/yellow/red) weekly.
- **Cascading is overkill at pre-seed.** Company OKRs = team OKRs when you have <10 people. Don't create artificial hierarchy.
