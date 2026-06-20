---
name: market-sizing
description: Cuando el founder necesita calcular el tamaño de mercado con rigor. Activa con "TAM", "SAM", "SOM", "tamaño de mercado", "market size", "oportunidad de mercado", "cuánto vale el mercado".
domain: market
reads: [inputs/]
outputs: [outputs/market-sizing.md]
web_search: true
---

# Market Sizing Agent

## Cuándo usar
- El founder necesita calcular TAM/SAM/SOM para el deck o para estrategia
- Un inversor cuestiona el tamaño de mercado
- El equipo necesita validar si la oportunidad es suficientemente grande

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (slide de mercado)
- Análisis de mercado previo
- Datos de clientes o pricing
- Informes de industria

Si inputs/ está vacío, pregunta: "¿Cuál es tu producto, quién es tu cliente objetivo y cuánto cobras (o planeas cobrar)?"

## Workflow

1. **Leer inputs/** — Extrae: producto, cliente objetivo, pricing, geografía, segmentos de mercado, y cualquier estimación previa de TAM/SAM/SOM.

2. **Calcular con dos metodologías** — Top-down (informes de industria, tamaño global → filtrar) Y bottom-up (# clientes potenciales × precio × frecuencia). Si hay diferencia >3x entre ambos, investigar la discrepancia.

3. **Web search** — Busca datos actualizados de mercado: informes de industria, tamaños de mercados similares, crecimiento del sector, y fundraising de competidores (como proxy de tamaño de mercado).

4. **Producir output** — Escribe `outputs/market-sizing.md` con cálculos detallados y fuentes.

## Output Format

`outputs/market-sizing.md`:

```
# Market Sizing — [Nombre Startup]

## Definición del mercado
[Qué mercado estamos midiendo — definición precisa]

## TAM (Total Addressable Market)
### Metodología top-down
[Fuente → dato global → filtros aplicados → resultado]
**TAM top-down: $X**

### Metodología bottom-up
[# clientes potenciales × ACV × frecuencia]
**TAM bottom-up: $X**

### Reconciliación
[Por qué los números son similares / diferentes]

**TAM final: $X** (con justificación de cuál metodología se usa)

## SAM (Serviceable Addressable Market)
[Filtros aplicados: geografía, segmento, canal de distribución]
| Filtro | Reducción | Resultado |
|---|---|---|
**SAM: $X**

## SOM (Serviceable Obtainable Market — 3 años)
[Cuota de mercado realista basada en: velocidad de crecimiento, recursos, competencia]
| Supuesto | Valor |
|---|---|
| Clientes target año 1 | |
| Clientes target año 2 | |
| Clientes target año 3 | |
| ACV | |
**SOM (3 años): $X**

## Crecimiento del mercado
| Año | Tamaño estimado | CAGR | Fuente |
|---|---|---|---|

## Drivers de crecimiento
1. [Tendencia que expande el mercado]
2. [Cambio regulatorio o tecnológico]
3. [Cambio en comportamiento del consumidor]

## Riesgos de mercado
1. [Qué podría contraer el mercado]
2. [Riesgo regulatorio]

## Fuentes
[Lista de todas las fuentes usadas con links]
```

## Frameworks & Best Practices

- **Bottom-up is more credible than top-down.** "There are 500K dentists in the US × $200/month = $1.2B SAM" is more convincing than "The dental software market is $5B according to Gartner." Investors trust math they can verify.
- **TAM is not your market.** TAM is the theoretical maximum if you had 100% market share with every possible product. It's useful for context, not for planning. Focus on SAM and SOM.
- **SOM should be ambitious but defensible.** 1-5% of SAM in 3 years is typical for a well-funded startup. 10%+ requires extraordinary distribution advantage. 0.1% means the market doesn't need you.
- **Adjacent markets expand TAM over time.** Start with your current market, but show how you could expand: new geographies, new segments, new products. This is the "land and expand" story.
- **Beware "market creation" fallacy.** If your TAM requires the market to exist first, you have a market risk problem. "The AI for dentists market is $0 today but will be $5B" is not a TAM — it's a bet.
- **Use fundraising of competitors as a proxy.** If competitors have raised $100M+ collectively, the market is large enough. This data is publicly available on Crunchbase, PitchBook.
- **Update annually.** Market sizes change. COVID created markets and destroyed others. AI is doing the same. A market sizing from 2023 may be irrelevant in 2026.
- **Price sensitivity affects SAM.** Your SAM isn't just "people with the problem" — it's "people willing to pay your price for the solution." Price sensitivity narrows your serviceable market.
