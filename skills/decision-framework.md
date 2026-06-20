---
name: decision-framework
description: Framework para tomar decisiones estratégicas estructuradas. Activa con "decidir", "decisión", "tradeoff", "pros y contras", "qué hacer", "dilema", "opción A vs B".
type: skill
scope: common
reads: [inputs/]
outputs: [outputs/decision-analysis.md]
---

# Decision Framework Skill

## Cuándo usar
- El founder enfrenta una decisión importante y no sabe qué camino tomar
- El equipo tiene múltiples opciones y necesita un análisis estructurado
- Para documentar el razonamiento detrás de una decisión importante

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción de las opciones a evaluar
- Datos relevantes para la decisión
- Contexto de negocio o restricciones

Si inputs/ está vacío, pregunta: "¿Cuál es la decisión que necesitas tomar, cuáles son las opciones y cuál es el deadline?"

## Workflow

1. **Leer inputs/** — Extrae: opciones, criterios de decisión, constraints, stakeholders afectados.
2. **Analizar** — Evalúa cada opción con análisis de reversibilidad, impacto y riesgo.
3. **Producir output** — Escribe `outputs/decision-analysis.md`.

## Output Format

```
# Decision Analysis — [Tema]

## La decisión
[Frase clara de qué se decide]

## Tipo de decisión
- Reversibilidad: [Alta/Baja] — Type 1 (irreversible) vs Type 2 (reversible)
- Urgencia: [Alta/Media/Baja]
- Impacto: [Alto/Medio/Bajo]

## Opciones

### Opción A: [Nombre]
| Pros | Contras |
|---|---|
| | |

### Opción B: [Nombre]
| Pros | Contras |
|---|---|
| | |

### Opción C: [No hacer nada / Status quo]
| Pros | Contras |
|---|---|
| | |

## Matriz de evaluación
| Criterio | Peso | Opción A | Opción B | Opción C |
|---|---|---|---|---|
| [Criterio 1] | | /10 | /10 | /10 |
| [Criterio 2] | | | | |
| **Total ponderado** | | | | |

## Análisis de riesgos
| Opción | Peor escenario | Probabilidad | Mitigación |
|---|---|---|---|

## Recomendación
[Opción recomendada con justificación de 2-3 frases]

## Pre-mortem
[Si elegimos la opción recomendada y falla, ¿por qué habrá sido?]

## Criterio de revisión
[Cuándo y cómo revisar si la decisión fue correcta]
```
