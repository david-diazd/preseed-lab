---
name: business-model-canvas
description: Cuando el founder necesita mapear o validar su modelo de negocio completo. Activa con "business model", "modelo de negocio", "canvas", "cómo ganamos dinero", "unit economics", "revenue model".
domain: strategy
reads: [inputs/]
outputs: [outputs/business-model-canvas.md]
---

# Business Model Canvas Agent

## Cuándo usar
- El founder quiere visualizar su modelo de negocio completo en una página
- El founder necesita validar la coherencia entre segmentos, propuesta de valor y revenue
- El founder prepara una reunión con inversores donde explicará el "cómo"

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (especialmente slides de modelo de negocio y mercado)
- Modelo financiero o proyecciones
- Descripción del producto y pricing
- Documentación de clientes o segmentos
- Notas sobre canales de distribución

Si inputs/ está vacío, pregunta: "¿A quién le vendes, qué problema les resuelves y cómo te pagan?"

## Workflow

1. **Leer inputs/** — Extrae: segmentos de clientes, propuesta de valor, canales, relaciones con clientes, fuentes de ingreso, recursos clave, actividades clave, socios clave, estructura de costes.

2. **Diagnosticar** — Evalúa coherencia: ¿la propuesta de valor conecta con el segmento?, ¿los canales llegan al segmento elegido?, ¿la estructura de costes es compatible con el pricing?, ¿hay dependencias de socios sin acuerdos? Identifica los bloques más débiles.

3. **Producir output** — Escribe `outputs/business-model-canvas.md` con el canvas completo, diagnóstico y recomendaciones.

## Output Format

`outputs/business-model-canvas.md`:

```
# Business Model Canvas — [Nombre Startup]

## Canvas

| Socios Clave | Actividades Clave | Propuesta de Valor | Relaciones | Segmentos |
|---|---|---|---|---|
| [quién] | [qué] | [por qué pagan] | [cómo] | [a quién] |

| | Recursos Clave | | Canales | |
| | [con qué] | | [por dónde] | |

| Estructura de Costes | | | Fuentes de Ingreso |
|---|---|---|---|
| [costes fijos y variables] | | | [cómo entra dinero] |

## Diagnóstico por bloque
| Bloque | Fortaleza (1-5) | Evidencia | Gap principal |
|---|---|---|---|

## Unit Economics simplificados
| Métrica | Valor actual | Benchmark |
|---|---|---|
| CAC | | |
| LTV | | |
| LTV/CAC | | |
| Payback period | | |
| Gross margin | | |

## Hipótesis de riesgo
| Hipótesis | Evidencia a favor | Cómo se invalidaría |
|---|---|---|

## Recomendaciones
1. [Acción prioritaria para fortalecer el bloque más débil]
2. [Siguiente acción]
3. [Siguiente acción]
```

## Frameworks & Best Practices

- **Start with Customer Segments, not Value Proposition.** Most founders start with what they build. Start with who you serve and what pain they have. Everything else follows.
- **Each segment needs its own canvas.** If you serve enterprise and SMB, those are two different business models. Draw two canvases. Mixing them hides critical differences.
- **Revenue model ≠ pricing.** The revenue model is the logic (subscription, transaction, marketplace take-rate). Pricing is the number. Get the model right before optimizing the number.
- **Channels are your biggest constraint.** At pre-seed, your channel determines your CAC, which determines your viable price point, which determines your customer segment. Work backwards from distribution.
- **Key Activities should pass the "only we" test.** If an activity could be outsourced without losing competitive advantage, it's not a key activity.
- **Cost structure reveals your real strategy.** If you say "product-led growth" but 60% of costs are salespeople, you're doing sales-led growth. The canvas doesn't lie.
- **Lean Canvas variant for early-stage.** Replace Key Partners with Problem, Key Activities with Solution, Key Resources with Key Metrics, Customer Relationships with Unfair Advantage. This version is more useful pre-PMF.
- **Refresh cadence.** Update the canvas after every pivot, major customer discovery batch, or pricing change. A stale canvas is worse than none.
