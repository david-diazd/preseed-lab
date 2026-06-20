---
name: user-research-synthesis
description: Cuando el founder tiene notas de entrevistas de usuarios y quiere extraer insights accionables. Activa con "entrevistas de usuarios", "customer discovery", "sintetizar feedback", "qué nos dicen los usuarios".
domain: product
reads: [inputs/]
outputs: [outputs/user-research-synthesis.md]
---

# User Research Synthesis Agent

## Cuándo usar
- El founder tiene notas de entrevistas de usuarios y no sabe qué hacer con ellas
- El founder quiere identificar patrones en el feedback recibido
- El founder necesita traducir observaciones en decisiones de producto

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Notas de entrevistas de usuarios (Word, PDF, TXT)
- Transcripciones de llamadas de discovery
- Respuestas a encuestas (CSV, Excel)
- Emails o mensajes de usuarios con feedback

Si inputs/ está vacío, pregunta: "¿Tienes notas de entrevistas de usuarios o feedback de clientes que pueda analizar?"

## Workflow

1. **Leer inputs/** — Lee todas las notas e identifica las citas textuales más reveladoras. Agrupa por temas emergentes sin forzar categorías previas.

2. **Diagnosticar** — Encuentra patrones: ¿qué problemas mencionan >50% de los usuarios? ¿Qué workarounds están usando? ¿Qué outcomes buscan que el producto no da? ¿Qué sorpresas hay vs. las hipótesis previas?

3. **Producir output** — Escribe `outputs/user-research-synthesis.md` con insights priorizados por frecuencia e impacto, citas textuales de soporte, y acciones de producto recomendadas.

## Output Format

`outputs/user-research-synthesis.md`:

```
## Resumen ejecutivo
[3-5 bullets con los hallazgos más importantes]

## Insights por tema

### [Tema 1] — mencionado por X/Y entrevistados
**Insight:** [Qué quieren o necesitan realmente]
**Evidencia:** "[Cita textual 1]" — [perfil de usuario]
           "[Cita textual 2]" — [perfil de usuario]
**Implicación para producto:** [Qué sugiere hacer]

[repetir por cada tema]

## Sorpresas vs. hipótesis previas
[Lo que era diferente a lo esperado]

## Acciones recomendadas (priorizadas)
1. [Acción] — basada en [insight], impacto esperado: [descripción]
2. ...

## Perfiles de usuario emergentes
[Si hay segmentos distintos que aparecen en los datos]
```

## Frameworks & Best Practices

- **Jobs to Be Done (JTBD).** Frame every finding as a job the customer is trying to accomplish, not a feature they want. Customers hire products to make progress in their lives.
- **Read before you summarize.** Always process the complete transcript before writing any summary. Partial reads produce biased synthesis.
- **Plain language over jargon.** Write summaries that are accessible to anyone on the team, including non-technical stakeholders. Avoid PM jargon unless the team uses it consistently.
- **Preserve direct quotes.** The most powerful data points are verbatim quotes that capture the participant's emotion, specificity, and language. "I spent 3 hours last Tuesday rebuilding the report" beats "reporting is hard."
- **Separate satisfaction from problems.** Explicitly track what users like about current solutions alongside what frustrates them. Knowing strengths prevents accidentally breaking them.
- **Current solutions reveal competitors.** Documenting what participants use today (including spreadsheets, manual processes, and workarounds) reveals the true competitive landscape, which is broader than direct product competitors.
- **Frequency is not importance.** A pain point mentioned by 2 of 10 users may be more critical than one mentioned by 8 if those 2 users represent your ideal customer profile.
- **Bias awareness.** Note recruitment bias (who was NOT interviewed), leading question bias (review the interview script), and survivorship bias (current users vs. churned users).
- **Minimum viable sample.** For qualitative research, 5-8 interviews per segment typically reach thematic saturation. Flag if the sample is below this threshold.
- **Triangulation.** Cross-reference findings across data types. An insight supported by interviews AND support tickets AND survey data is stronger than one source alone.
- **Continuous discovery.** Treat interview synthesis as an ongoing practice, not a one-time project. Regular weekly interviews compound into deep customer understanding over time.
