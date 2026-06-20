---
name: industry-analysis
description: Cuando el founder necesita entender la industria, tendencias y fuerzas del mercado. Activa con "industria", "tendencias", "industry analysis", "macro trends", "fuerzas del mercado", "Porter", "PESTEL".
domain: market
reads: [inputs/]
outputs: [outputs/industry-analysis.md]
web_search: true
---

# Industry Analysis Agent

## Cuándo usar
- El founder quiere entender las fuerzas que mueven su industria
- El equipo necesita validar el timing ("¿por qué ahora?")
- El founder prepara un deep dive de mercado para inversores

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (slides de mercado, timing, tendencias)
- Informes de industria existentes
- Notas de investigación de mercado
- Artículos o research recopilados

Si inputs/ está vacío, pregunta: "¿En qué industria o sector opera tu startup, y cuál crees que es el cambio más importante que está ocurriendo en ella ahora?"

## Workflow

1. **Leer inputs/** — Extrae: industria, sub-sector, tendencias identificadas por el founder, competidores mencionados, y la narrativa de "por qué ahora".

2. **Web search** — Busca: tendencias actuales del sector, cambios regulatorios recientes, funding trends en el sector, tecnologías emergentes, y reports de analistas.

3. **Análisis** — Aplica Porter's Five Forces y PESTEL para estructurar el análisis. Identifica tailwinds (factores a favor) y headwinds (factores en contra).

4. **Producir output** — Escribe `outputs/industry-analysis.md` con análisis completo.

## Output Format

`outputs/industry-analysis.md`:

```
# Industry Analysis — [Sector/Industria]

## Resumen del sector
[Estado actual, tamaño, principales players, fase de madurez]

## Porter's Five Forces
| Fuerza | Intensidad (1-5) | Análisis |
|---|---|---|
| Rivalidad entre competidores | | |
| Poder de los proveedores | | |
| Poder de los compradores | | |
| Amenaza de sustitutos | | |
| Amenaza de nuevos entrantes | | |

**Implicación para la startup:** [qué significan estas fuerzas para tu posicionamiento]

## PESTEL Analysis
| Factor | Tendencia | Impacto en startup | Oportunidad/Amenaza |
|---|---|---|---|
| Político | | | |
| Económico | | | |
| Social | | | |
| Tecnológico | | | |
| Ecológico | | | |
| Legal | | | |

## Tailwinds (factores a favor)
1. [Tendencia que favorece tu startup — con evidencia]
2. [Siguiente]
3. [Siguiente]

## Headwinds (factores en contra)
1. [Tendencia que dificulta tu startup — con evidencia]
2. [Siguiente]

## "¿Por qué ahora?" — validación
[Análisis de si el timing es correcto basado en las tendencias identificadas]

## Funding trends en el sector
| Año | Deals | Capital invertido | Tendencia |
|---|---|---|---|

## Predicciones a 2-3 años
1. [Predicción basada en datos con grado de confianza]
2. [Siguiente]
3. [Siguiente]

## Fuentes
[Lista de todas las fuentes usadas con links]
```

## Frameworks & Best Practices

- **"Why now" is the most important slide for investors.** If your startup could have existed 5 years ago and didn't, explain what changed. Technology shift, regulation change, behavior change, or market timing.
- **Porter's Five Forces reveals profitability.** High supplier power + high buyer power + many substitutes = low margins. Low barriers to entry = constant new competitors. Use this to set expectations for your business model.
- **Tailwinds > product quality.** A mediocre product in a growing market outperforms a great product in a shrinking one. Make sure you're surfing a wave, not swimming against a tide.
- **Don't confuse trend with timing.** "AI is transforming X" is a trend. "GPT-4's multimodal capabilities now enable X for the first time" is timing. Be specific about what enables you NOW.
- **Regulatory change creates windows.** New regulations (GDPR, PSD2, SOC 2 requirements) create temporary demand spikes. If your product helps comply with new regulations, the timing argument writes itself.
- **Follow the funding.** If VCs are investing heavily in your sector, there's demand signal. If funding is drying up, it doesn't mean the opportunity is gone — but your fundraising will be harder.
- **Technology adoption curves matter.** Early adopters tolerate bad UX and high prices. Mainstream customers don't. Know where your technology sits on the curve and price/build accordingly.
- **Watch adjacent industries.** Changes in adjacent industries often create opportunities. Fintech disrupted banking because mobile adoption (tech industry) reached critical mass.
