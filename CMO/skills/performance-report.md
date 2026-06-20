---
name: performance-report
description: Genera reporte de rendimiento de marketing. Activa con "marketing report", "reporte de marketing", "cómo van las campañas", "rendimiento de canales", "marketing metrics".
type: skill
scope: CMO
chains: [CMO/agents/growth/analytics-setup, CMO/agents/growth/growth-model]
reads: [inputs/]
outputs: [outputs/marketing-report.md]
---

# Marketing Performance Report Skill

## Cuándo usar
- Al final de cada mes para evaluar resultados de marketing
- Para reportar al CEO/board sobre rendimiento de marketing
- Para decidir dónde invertir más (o menos) el próximo mes

## Qué leer en inputs/
- Datos de campañas (CTR, CPC, conversiones)
- Métricas de canales orgánicos
- Revenue atribuido a marketing
- Presupuesto gastado vs planificado

Si inputs/ está vacío, pregunta: "¿Qué canales de marketing usas, tienes datos de rendimiento del último mes, y cuál es tu presupuesto de marketing?"

## Output Format

```
# Marketing Performance Report — [Mes Año]

## Resumen ejecutivo
[3 bullet points: what worked, what didn't, recommendation]

## KPIs del mes
| KPI | Target | Actual | vs Target | vs Mes anterior |
|---|---|---|---|---|
| Leads generados | | | | |
| CAC | | | | |
| Marketing Qualified Leads | | | | |
| Conversion rate | | | | |
| Website traffic | | | | |

## Rendimiento por canal
| Canal | Spend | Leads | CAC | Conv. rate | ROI | Trend |
|---|---|---|---|---|---|---|

## Top performers
### Mejor campaña
[Nombre, métricas, por qué funcionó]

### Mejor contenido
[Título, métricas, por qué funcionó]

### Peor performer
[Qué fue, qué salió mal, qué cambiar]

## Funnel completo
| Stage | Volumen | Conv. rate | Bottleneck |
|---|---|---|---|
| Visitors → Leads | | | |
| Leads → MQL | | | |
| MQL → Opportunity | | | |
| Opportunity → Customer | | | |

## Budget
| Canal | Presupuesto | Gastado | % usado | Resultado |
|---|---|---|---|---|

## Recomendaciones para próximo mes
| Acción | Canal | Budget propuesto | Expected impact |
|---|---|---|---|

## Experimentos a correr
| Experimento | Hipótesis | Métrica | Duración |
|---|---|---|---|
```
