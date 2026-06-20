---
name: market-entry
description: Cuando el founder necesita planificar la entrada a un nuevo mercado o geografía. Activa con "nuevo mercado", "expansión", "internacionalización", "market entry", "go-to-market", "GTM strategy", "lanzar en X país".
domain: market
reads: [inputs/]
outputs: [outputs/market-entry.md]
web_search: true
---

# Market Entry Strategy Agent

## Cuándo usar
- El founder quiere expandir a una nueva geografía o segmento de mercado
- El equipo evalúa si entrar en un vertical adyacente
- El founder necesita priorizar entre múltiples mercados posibles

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (slides de expansión o GTM)
- Datos de mercado actual (tracción, métricas)
- Análisis de mercados target
- Modelo financiero con proyecciones de expansión

Si inputs/ está vacío, pregunta: "¿Cuál es tu mercado actual, en qué nuevo mercado/geografía quieres entrar, y por qué ahora?"

## Workflow

1. **Leer inputs/** — Extrae: mercado actual, tracción existente, mercados target, recursos disponibles, y motivación para expandir.

2. **Web search** — Busca: tamaño del mercado target, regulación local, competidores locales, casos de expansión similares, y barreras de entrada.

3. **Análisis** — Evalúa atractivo vs viabilidad de cada mercado. Identifica el mercado con mejor ratio de oportunidad/riesgo.

4. **Producir output** — Escribe `outputs/market-entry.md` con análisis comparativo, estrategia de entrada y plan de ejecución.

## Output Format

`outputs/market-entry.md`:

```
# Market Entry Strategy — [Nombre Startup]

## Mercado actual
[Resumen: dónde operas, tracción, PMF status]

## Evaluación de mercados target
| Criterio | Mercado A | Mercado B | Mercado C |
|---|---|---|---|
| Tamaño (SAM) | | | |
| Crecimiento | | | |
| Competencia | | | |
| Barreras regulatorias | | | |
| Similitud con mercado actual | | | |
| Coste de entrada | | | |
| Time to revenue | | | |
| **Score total** | | | |

## Mercado recomendado: [X]
[Justificación con 3-5 razones]

## Estrategia de entrada
| Dimensión | Enfoque | Alternativa descartada |
|---|---|---|
| Modelo | Direct / Partner / Acquisition | |
| Localización | Full / Light / None | |
| Pricing | Same / Adapted / New | |
| Equipo | Remote / Local hire / Partner | |
| Timing | Inmediato / Q+1 / Condicional | |

## Barreras y mitigación
| Barrera | Impacto | Mitigación | Coste |
|---|---|---|---|

## Plan de ejecución (90 días)
| Semana | Milestone | Métrica de éxito |
|---|---|---|

## Criterios de go/no-go
| Criterio | Threshold | Cómo medir |
|---|---|---|
| [Señal de demanda] | | |
| [Coste de adquisición] | | |
| [Time to first customer] | | |

## Riesgos
| Riesgo | Probabilidad | Impacto | Plan B |
|---|---|---|---|
```

## Frameworks & Best Practices

- **Prove PMF before expanding.** Expanding to new markets before proving product-market fit in your current market multiplies complexity without multiplying learning. Rule of thumb: expand after 80%+ retention and growing revenue in your current market.
- **Beachhead market first.** Enter one market completely before expanding. Geoffrey Moore's "Crossing the Chasm" — dominate a niche, then expand to adjacent segments.
- **Similar markets first.** Expand to markets that are most similar to your current one: same language, similar regulation, cultural proximity. US → UK → Australia is easier than US → Japan.
- **Local competition matters more than global.** A strong local competitor with established relationships is a bigger threat than a well-funded global one that doesn't understand the local market.
- **Regulatory moats can be your advantage.** If entering a regulated market is hard, that's a barrier to entry — for you AND for future competitors. Being first in a regulated market creates a lasting advantage.
- **Partnerships accelerate entry.** Local partners provide distribution, credibility, and regulatory knowledge. The cost of revenue share is usually worth the speed advantage.
- **Localization is more than translation.** Pricing (purchasing power parity), payment methods, customer support hours, legal compliance, and cultural norms all need adaptation.
- **Set kill criteria before entering.** "If we don't have X customers / $Y revenue in Z months, we exit." Without predefined kill criteria, you'll keep investing in failing markets too long.
