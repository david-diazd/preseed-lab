---
name: pricing-strategy
description: Cuando el founder necesita definir o revisar su estrategia de pricing. Activa con "pricing", "precio", "cuánto cobrar", "freemium", "free trial", "planes", "tiers", "monetización".
domain: growth
reads: [inputs/]
outputs: [outputs/pricing-strategy.md]
---

# Pricing Strategy Agent

## Cuándo usar
- El founder va a lanzar y no sabe cuánto cobrar
- El founder quiere cambiar su pricing model (freemium, tiers, usage-based)
- El founder necesita justificar su pricing ante inversores

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Modelo financiero con unit economics
- Análisis de competidores y su pricing
- Feedback de clientes sobre willingness to pay
- Pitch deck (slides de modelo de negocio)

Si inputs/ está vacío, pregunta: "¿Qué vendes (SaaS, marketplace, servicio), quiénes son tus clientes (consumidores, SMB, enterprise), y cuánto cobras hoy o planeas cobrar?"

## Workflow

1. **Leer inputs/** — Extrae: modelo de negocio, segmentos de clientes, pricing actual o propuesto, costes (COGS, CAC), pricing de competidores, y feedback de willingness to pay.

2. **Diagnosticar** — Evalúa: ¿el precio refleja el valor entregado?, ¿es compatible con el CAC?, ¿el modelo de pricing alinea incentivos con el cliente?, ¿hay dinero en la mesa (underpriced) o está frenando adopción (overpriced)?

3. **Producir output** — Escribe `outputs/pricing-strategy.md` con modelo de pricing, tiers, justificación y plan de rollout.

## Output Format

`outputs/pricing-strategy.md`:

```
# Pricing Strategy — [Nombre Producto]

## Modelo de pricing recomendado
[Tipo: flat rate / tiered / usage-based / freemium / hybrid]
[Justificación: por qué este modelo para este producto y mercado]

## Tabla de planes
| | Free/Trial | Plan 1 | Plan 2 | Enterprise |
|---|---|---|---|---|
| Precio | | | | |
| Valor métrica | | | | |
| Feature 1 | ✅/❌ | | | |
| Feature 2 | | | | |
| Feature 3 | | | | |
| Soporte | | | | |

## Lógica de la escala de valor
[Qué aumenta con cada tier y por qué — la métrica de valor]

## Unit economics por plan
| Plan | Precio | COGS | Gross margin | CAC target | Payback |
|---|---|---|---|---|---|

## Pricing vs competencia
| Competidor | Precio | Modelo | Posicionamiento |
|---|---|---|---|

## Análisis de willingness to pay
[Métodos usados: Van Westendorp, Gabor-Granger, conversaciones con clientes]
[Rango de precio aceptable encontrado]

## Plan de rollout
| Fase | Acción | Criterio para avanzar |
|---|---|---|

## Errores a evitar
[Anti-patterns específicos para este tipo de producto]
```

## Frameworks & Best Practices

- **Price on value, not on cost.** Your cost to serve a customer is irrelevant to pricing. What matters is how much value the customer gets. If you save them $10K/month, charging $1K/month is fair regardless of your $50 hosting cost.
- **The value metric is the most important decision.** Per seat, per transaction, per GB, per API call — this determines how your revenue scales with customer success. The best value metrics grow as the customer gets more value.
- **Start higher than you think.** You can always lower prices. Raising them is painful. Most pre-seed founders underprice by 2-5x because they're afraid of rejection. Charge more.
- **Freemium is a growth strategy, not a pricing strategy.** Only use freemium if: (a) your marginal cost per free user is near zero, (b) free users generate value for paid users (network effects), or (c) you need massive adoption before monetizing.
- **Three plans is the sweet spot.** Good-Better-Best. The middle plan should be where you want most customers. The top plan exists to make the middle plan look reasonable (anchoring effect).
- **Annual pricing solves churn.** Offer a 15-20% discount for annual plans. This improves cash flow, reduces churn, and increases LTV.
- **Grandfather early customers.** Lock in early adopters at their original price forever. They took a bet on you. Reward that loyalty. It also reduces churn from price-sensitive early users.
- **Van Westendorp for validation.** Ask customers: (1) At what price is it too expensive? (2) Too cheap to be quality? (3) Starting to get expensive? (4) A great deal? The intersection reveals the acceptable price range.
