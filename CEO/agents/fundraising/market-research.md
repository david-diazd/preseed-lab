---
name: market-research
description: Cuando el founder necesita calcular el tamaño de mercado o validar sus claims de mercado. Activa con "TAM", "SAM", "SOM", "tamaño de mercado", "market size", "oportunidad de mercado", "slide de mercado".
domain: fundraising
reads: [inputs/]
outputs: [outputs/market-research.md]
---

# Market Research Agent

## Cuándo usar
- El founder necesita calcular TAM/SAM/SOM para su deck
- El founder quiere validar con rigor los claims de mercado que ya tiene
- El founder se prepara para preguntas de inversores sobre el mercado

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (para extraer el mercado objetivo y claims existentes)
- Descripción del producto o one-pager
- Datos de pricing y modelo de negocio
- Cualquier análisis de mercado previo o informes del sector

Si inputs/ está vacío, pregunta: "¿Qué producto vendes, a quién se lo vendes y a qué precio? Con eso puedo construir el TAM/SAM/SOM."

## Workflow

1. **Leer inputs/** — Extrae: descripción del producto, cliente objetivo (ICP), precio por cliente, modelo de ingresos, geografía objetivo, y cualquier claim de mercado existente que necesite validación.

2. **Diagnosticar** — Evalúa si los claims de mercado existentes son creíbles (¿solo top-down? ¿sin fuentes? ¿mercado demasiado amplio?). Identifica qué falta para hacer el análisis defendible ante un inversor.

3. **Producir output** — Escribe `outputs/market-research.md` con TAM/SAM/SOM calculado con metodología top-down + bottom-up, drivers de crecimiento y supuestos explícitos.

## Output Format

`outputs/market-research.md`:

```
## Definición del mercado
[Párrafo definiendo el problema, cliente, geografía y scoping decisions]

## TAM / SAM / SOM
| Métrica | Estimación actual | Proyección 2-3 años | Método | Confianza |
|---|---|---|---|---|
| TAM | $X | $Y | Top-down + Bottom-up | Alta/Media/Baja |
| SAM | $X | $Y | Filtrado de TAM | Alta/Media/Baja |
| SOM | $X | $Y | Modelo de penetración | Alta/Media/Baja |

## Metodología de cálculo
**Top-Down:** [pasos del cálculo desde el total del sector]
**Bottom-Up:** [pasos desde unit economics: N clientes × precio × frecuencia]
**Reconciliación:** [por qué convergen o dónde difieren]

## Drivers de crecimiento
[Factores que expanden o contraen el mercado]

## Supuestos clave y riesgos
| Supuesto | Impacto si falla | Confianza | Cómo validar |
|---|---|---|---|

## Implicaciones estratégicas
[Qué significa para producto, pricing y go-to-market]
```

## Frameworks & Best Practices

- **Always do both top-down and bottom-up.** Top-down is fast but abstract. Bottom-up is precise but assumption-heavy. The truth is where they converge. Providing both triangulates and builds credibility with investors.
- **Beware vanity TAMs.** "The global software market is $500B" is not useful. Define the market narrowly enough that you can name the buyer persona, their budget line item, and what they pay today.
- **The "who writes the check" test.** Market size should be based on the actual budget your product replaces or claims. A $50/month tool's market is (number of buyers) x ($600/year), not the total revenue of the industry you serve.
- **Growth rate matters more than current size.** A $500M market growing 40% annually is more attractive than a $5B market growing 3%. Investors and founders should optimize for tailwinds.
- **Distinguish value-based from volume-based sizing.** Revenue-based (dollars) and volume-based (users/units) tell different stories. Be explicit about which you are using and why.
- **Assumption sensitivity analysis.** Identify the 2-3 assumptions that most affect your estimate. Show what happens if each is 50% lower. If the market is still attractive at the pessimistic end, the thesis is robust.
- **Source hierarchy for credibility:** (1) Government statistics and census data, (2) Public company filings and earnings calls, (3) Industry association reports, (4) Analyst reports (Gartner, Forrester, IDC), (5) Startup databases (PitchBook, Crunchbase), (6) Your own primary research and customer data.
- **Cite sources for market data.** Avoid unsupported numbers. Label what is an estimate vs. what is sourced data. Flag where estimates have wide confidence intervals.
- **Geographic specificity.** Global TAMs are meaningful only if you plan to sell globally from day one. Start with the geography and segment you will actually target first.
- **Adjacent market expansion.** After sizing the core market, identify 1-2 adjacent markets you could expand into. This shows a growth path beyond the initial wedge.
- **Consider currency and purchasing power parity** for international market sizing.
