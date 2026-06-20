---
name: ab-test-analysis
description: Analiza resultados de A/B tests y recomienda decisiones. Activa con "A/B test", "test results", "split test", "experiment results", "qué variante ganó", "significancia estadística".
type: skill
scope: CMO
chains: [CMO/agents/growth/analytics-setup]
reads: [inputs/]
outputs: [outputs/ab-test-analysis.md]
---

# A/B Test Analysis Skill

## Cuándo usar
- Cuando un A/B test termina y hay que tomar una decisión
- Para diseñar un test con la muestra y duración correctas
- Para interpretar resultados y evitar errores estadísticos comunes

## Qué leer en inputs/
- Datos del test (variantes, muestras, conversiones)
- Hipótesis original del test
- Duración del test
- Segmentos analizados

Si inputs/ está vacío, pregunta: "¿Qué testeaste (A vs B), cuánto tráfico tuvo cada variante, cuántas conversiones, y cuánto duró el test?"

## Output Format

```
# A/B Test Analysis — [Nombre del test]

## Setup
| Dimensión | Detalle |
|---|---|
| Hipótesis | [Si cambiamos X, entonces Y mejorará porque Z] |
| Métrica primaria | |
| Métricas secundarias | |
| Duración | |
| Muestra mínima requerida | |

## Resultados
| Variante | Visitors | Conversiones | Conv. rate | Confidence |
|---|---|---|---|---|
| Control (A) | | | | |
| Variante (B) | | | | |

## Análisis estadístico
| Métrica | Valor |
|---|---|
| Diferencia relativa | [+X%] |
| Significancia estadística | [Sí/No — p-value] |
| Confidence level | [%] |
| Power | [%] |
| Efecto observado | [Dentro/fuera del MDE] |

## Decisión
**Recomendación:** [Implementar B / Mantener A / Test inconcluso — re-run]
**Razón:** [Justificación estadística y de negocio]

## Segmentación
| Segmento | Control | Variante | Diferencia | Nota |
|---|---|---|---|---|
| [Segmento 1] | | | | |
| [Segmento 2] | | | | |

## Learnings
1. [Qué aprendimos sobre el usuario/producto]
2. [Siguiente]

## Next experiments
| Test propuesto | Hipótesis | Métrica | Prioridad |
|---|---|---|---|

## Errores comunes detectados
[Si aplica: peeking, stopping early, multiple comparisons, etc.]
```
