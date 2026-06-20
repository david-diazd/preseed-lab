---
name: growth-model
description: Cuando el founder necesita diseñar su modelo de crecimiento. Activa con "growth model", "modelo de crecimiento", "growth loops", "flywheel", "cómo crecemos", "motor de crecimiento", "viral", "referral".
domain: growth
reads: [inputs/]
outputs: [outputs/growth-model.md]
---

# Growth Model Agent

## Cuándo usar
- El founder necesita definir cómo va a crecer la startup
- El equipo quiere identificar y priorizar sus canales de adquisición
- Inversores preguntan "¿cuál es tu growth engine?"

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (slides de tracción y crecimiento)
- Métricas de adquisición, activación, retención
- Datos de canales actuales (CAC por canal, conversión)
- Modelo financiero con proyecciones de usuarios

Si inputs/ está vacío, pregunta: "¿Cómo llegan tus usuarios hoy, cuánto cuesta adquirir uno, y cuál es tu retención a 30 días?"

## Workflow

1. **Leer inputs/** — Extrae: canales de adquisición actuales, métricas de funnel (AARRR), CAC, LTV, retención, y cualquier loop de crecimiento existente (referral, content, producto).

2. **Diagnosticar** — Evalúa: ¿dependen de un solo canal?, ¿el CAC es sostenible?, ¿hay loops compuestos o solo canales lineales?, ¿la retención soporta el modelo de growth?

3. **Producir output** — Escribe `outputs/growth-model.md` con modelo de crecimiento, loops priorizados y plan de experimentación.

## Output Format

`outputs/growth-model.md`:

```
# Growth Model — [Nombre Startup]

## Tipo de growth engine
[Viral / Paid / Content / Sales-led / Product-led — cuál es el primario y por qué]

## Funnel actual (AARRR)
| Stage | Métrica | Valor actual | Benchmark | Gap |
|---|---|---|---|---|
| Acquisition | | | | |
| Activation | | | | |
| Retention | | | | |
| Revenue | | | | |
| Referral | | | | |

## Growth loops identificados
### Loop 1: [Nombre]
[Diagrama: trigger → acción → output → re-trigger]
- Tiempo de ciclo: [X días]
- Coeficiente: [X usuarios genera cada usuario]
- Palanca principal: [qué optimizar]

### Loop 2: [Nombre]
...

## Canales de adquisición
| Canal | CAC | Volumen | Escalabilidad | Prioridad |
|---|---|---|---|---|

## Experimentos propuestos (próximos 90 días)
| Experimento | Hipótesis | Métrica | Criterio de éxito | Esfuerzo |
|---|---|---|---|---|

## North Star Metric
[La métrica que mejor captura el valor que entregas — con definición precisa]

## Proyección de crecimiento (3 escenarios)
| Mes | Conservador | Base | Optimista |
|---|---|---|---|
```

## Frameworks & Best Practices

- **Retention before acquisition.** If users leave after trying the product, spending on acquisition is pouring water into a leaky bucket. Fix retention first (D7 > 40% for consumer, D30 > 80% for B2B SaaS).
- **Loops > channels.** Channels are linear (spend $1 → get X users). Loops are compounding (users → action → more users). Every startup should have at least one loop.
- **The three growth engines (Eric Ries).** Sticky (retention-driven), viral (referral-driven), paid (CAC < LTV-driven). You need one primary engine, not all three.
- **North Star Metric guides everything.** Airbnb: nights booked. Slack: messages sent. Facebook: daily active users. Your NSM should measure the core value exchange, not vanity (signups, page views).
- **ICE framework for experiments.** Score each experiment by Impact (1-10), Confidence (1-10), Ease (1-10). Multiply for priority. Run 2-3 experiments per week, kill fast.
- **Activation is the highest-leverage stage.** Improving the percentage of signups who reach the "aha moment" improves every downstream metric. Define your activation event precisely.
- **One channel at a time.** At pre-seed, master one channel before diversifying. Going wide across 5 channels means being mediocre at all of them.
- **Compound growth rate is what matters.** 5% weekly growth = 12.6x annual growth. 10% weekly = 142x. Focus on the weekly growth rate, not absolute numbers.
