---
name: paid-ads-plan
description: Cuando el founder necesita diseñar campañas de paid acquisition. Activa con "ads", "publicidad", "Google Ads", "Meta Ads", "Facebook Ads", "paid acquisition", "campañas", "anuncios", "SEM".
domain: brand
reads: [inputs/]
outputs: [outputs/paid-ads-plan.md]
---

# Paid Ads Plan Agent

## Cuándo usar
- El founder quiere probar paid acquisition como canal de crecimiento
- El equipo ya tiene campañas corriendo pero quiere optimizarlas
- El founder necesita estimar presupuesto y ROI de paid ads

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Modelo financiero (CAC target, LTV)
- Landing page o web actual
- Datos de campañas anteriores (CTR, CPC, conversión)
- Análisis de competidores y su publicidad

Si inputs/ está vacío, pregunta: "¿Cuál es tu producto, cuánto puedes gastar al mes en ads, cuál es tu CAC target y tienes una landing page lista?"

## Workflow

1. **Leer inputs/** — Extrae: producto, ICP, CAC target, LTV, presupuesto disponible, landing page actual, y datos de campañas previas si existen.

2. **Diagnosticar** — Evalúa: ¿el CAC target es realista para el canal?, ¿la landing page está optimizada para conversión?, ¿el presupuesto es suficiente para obtener datos estadísticamente significativos?, ¿cuáles son los canales paid más probables?

3. **Producir output** — Escribe `outputs/paid-ads-plan.md` con estrategia de canales, estructura de campañas, copies/creativos y plan de presupuesto.

## Output Format

`outputs/paid-ads-plan.md`:

```
# Paid Ads Plan — [Nombre Startup]

## Evaluación de canales
| Canal | Fit con ICP | CPC estimado | Volumen | Recomendación |
|---|---|---|---|---|
| Google Search | | | | |
| Google Display | | | | |
| Meta (FB/IG) | | | | |
| LinkedIn | | | | |
| Twitter/X | | | | |
| TikTok | | | | |
| Reddit | | | | |

## Canal(es) recomendado(s)
[Justificación basada en ICP, intent y presupuesto]

## Estructura de campaña
### Campaña 1: [Objetivo]
| Elemento | Detalle |
|---|---|
| Plataforma | |
| Objetivo | Conversiones / Leads / Traffic |
| Audiencia | |
| Presupuesto diario | |
| Ad groups / Ad sets | |

#### Ad variations
| Ad | Headline | Description | CTA | Visual |
|---|---|---|---|---|

## Presupuesto y proyecciones
| Mes | Budget | Impresiones est. | Clicks est. | Leads est. | CAC est. |
|---|---|---|---|---|---|

## Funnel de conversión
[Landing → Signup → Activation → Paid]
[Conversion rates estimados en cada step]

## Plan de testing (primeras 4 semanas)
| Semana | Test | Variable | Budget | Criterio de éxito |
|---|---|---|---|---|

## Métricas a trackear
| Métrica | Tool | Frecuencia | Threshold para escalar |
|---|---|---|---|

## Cuándo NO hacer paid ads
[Señales de que no es el momento correcto]
```

## Frameworks & Best Practices

- **Don't run ads until your landing page converts.** If organic traffic doesn't convert on your landing page, paid traffic won't either. Fix the landing page first, then add paid fuel.
- **Start with high-intent channels.** Google Search captures existing demand (people searching for solutions). Social ads create demand (interrupting people's feed). Start with search if your category exists.
- **Minimum viable budget.** You need ~50 conversions per ad set per week for the algorithm to optimize. If your CPA is $50, that's $2,500/week minimum per ad set. Budget below this gets unreliable data.
- **Creative is the new targeting.** On Meta/TikTok, the algorithm finds your audience if you give it good creative. Focus 80% of effort on ad creative, 20% on audience targeting.
- **Test 3-5 ad variations minimum.** One headline, one image, one audience = one data point. You need multiple variations to learn what works. Rotate creative every 2-4 weeks to prevent ad fatigue.
- **Track the full funnel, not just clicks.** CPC is meaningless if clicks don't convert. Track cost per lead, cost per activation, and ultimately cost per paying customer.
- **Retargeting is the highest-ROI paid channel.** People who visited your site but didn't convert are warm leads. Retarget them with testimonials, case studies, and urgency. Retargeting typically has 2-5x better ROAS than cold ads.
- **Daily budget, not monthly.** Set daily budgets and check results daily during the first 2 weeks. Pause underperforming campaigns quickly. Scale winners gradually (20% budget increase per day max).
