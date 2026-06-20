---
name: competitive-analysis
description: Cuando el founder necesita analizar su competencia o posicionar su producto. Activa con "competidores", "landscape competitivo", "cómo nos diferenciamos", "moat", "comparación con X", "posicionamiento".
domain: fundraising
reads: [inputs/]
outputs: [outputs/competitive-analysis.md]
---

# Competitive Analysis Agent

## Cuándo usar
- El founder necesita preparar el slide de competencia del deck
- El founder quiere entender cómo diferenciarse de los players existentes
- El founder se prepara para preguntas de inversores sobre competencia

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (especialmente el slide de competencia existente)
- Descripción del producto y propuesta de valor
- Análisis de competencia previo
- Datos de clientes o feedback que mencione alternativas

Si inputs/ está vacío, pregunta: "¿Cuál es tu producto y quiénes son tus 3-5 competidores más directos?"

## Workflow

1. **Leer inputs/** — Extrae: descripción del producto, cliente objetivo, propuesta de valor diferencial, competidores ya identificados por el founder, y cualquier feedback de clientes sobre alternativas.

2. **Diagnosticar** — Evalúa el análisis existente: ¿dice "no tenemos competidores"? (red flag), ¿usa una 2x2 donde mágicamente dominas? (no convincente), ¿ignora al status quo ("no hacer nada") como competidor? Identifica gaps en el análisis.

3. **Producir output** — Escribe `outputs/competitive-analysis.md` con perfiles de 5 competidores, mapa de diferenciación y recomendación de posicionamiento.

## Output Format

`outputs/competitive-analysis.md`:

```
## Vista general del mercado
[Párrafo sobre estructura, número de players, fragmentación]

## Perfiles de competidores (x5)
### [Nombre competidor]
| Dimensión | Detalle |
|---|---|
| Perfil | Funding, tamaño, fundación |
| Fortalezas del producto | ... |
| Gaps del producto | ... |
| Modelo y pricing | ... |
| Por qué son peligrosos | ... |

## Oportunidades de diferenciación
- [Pain points sin resolver por ningún competidor]
- [Segmentos desatendidos]
- [Cambios de mercado que crean oportunidad]

## Recomendación de posicionamiento
- Posicionamiento sugerido y framing de categoría
- Diferenciadores clave a enfatizar (con evidencia)
- Segmentos donde ganar es más fácil
- Competidores a monitorizar y por qué
- Riesgos competitivos a 12-18 meses
```

## Frameworks & Best Practices

- **Primary sources over secondhand.** Use the competitor's own product (sign up for free trials), pricing page, job postings (reveal strategy), and customer reviews over analyst reports. Job postings are strategy signals -- hiring ML engineers means AI investment, enterprise sales reps means upmarket movement.
- **Status quo is your biggest competitor.** For most startups, the real competitor is "do nothing" or "use a spreadsheet." Analyze this alternative with the same rigor as named competitors.
- **Compete on a different axis.** If incumbents compete on features, compete on simplicity. If they compete on price, compete on experience. Winning means changing the evaluation criteria, not beating incumbents at their own game.
- **Track momentum, not just position.** A well-funded competitor with flat growth is weaker than an unfunded one growing 20% month-over-month. Monitor hiring velocity, product release cadence, and review sentiment trends.
- **Distinguish direct from adjacent.** Direct competitors solve the same problem for the same customer. Adjacent competitors solve the same problem differently or solve a related problem. Both matter but require different strategic responses.
- **Feature comparison honesty.** Mark your own product's gaps accurately. An internal competitive analysis that overstates your strengths is useless. The purpose is truth, not comfort.
- **Refresh cadence.** Update quarterly in fast-moving markets, semi-annually in slower ones. Track funding rounds, executive moves, and product launches as trigger events for ad-hoc updates.
- **Identify subtle differentiation.** The most durable competitive advantages are often not feature-based -- they are distribution advantages, data moats, ecosystem effects, or brand trust built over time.
