---
name: board-meeting-prep
description: Prepara materiales para reunión de board o advisors. Activa con "board meeting", "reunión de board", "preparar board", "board deck", "junta directiva".
type: skill
scope: CEO
chains: [CEO/agents/fundraising/board-update, CEO/agents/strategy/okr-planning]
reads: [inputs/]
outputs: [outputs/board-meeting-prep.md]
---

# Board Meeting Prep Skill

## Cuándo usar
- 1-2 semanas antes de una reunión de board
- Para preparar el deck y los materiales de discusión
- Para estructurar la agenda y los asks del board

## Qué leer en inputs/
- Board deck o update anterior
- Métricas actualizadas
- OKRs y su progreso
- Temas pendientes del último board

Si inputs/ está vacío, pregunta: "¿Cuándo es la reunión del board, quiénes asisten, y cuáles son los 2-3 temas que necesitas discutir o donde necesitas ayuda?"

## Output Format

```
# Board Meeting Prep — [Fecha de reunión]

## Agenda propuesta (2h)
| Tiempo | Tema | Formato | Objetivo |
|---|---|---|---|
| 0:00-0:10 | Welcome + contexto | Presentación | Alinear |
| 0:10-0:30 | Métricas y OKRs | Dashboard | Informar |
| 0:30-1:00 | Tema estratégico 1 | Discusión | Decidir |
| 1:00-1:30 | Tema estratégico 2 | Discusión | Feedback |
| 1:30-1:50 | Fundraising/financiero | Update | Informar |
| 1:50-2:00 | Asks y cierre | Lista | Comprometer |

## Board deck (slides recomendados)
1. **Highlights del periodo** — 3 wins, 1-2 challenges
2. **Métricas clave** — Dashboard con tendencia
3. **OKR scorecard** — Verde/amarillo/rojo por objetivo
4. **Financiero** — Burn, runway, cash position
5. **Tema estratégico** — Contexto + opciones + recomendación
6. **Asks** — Qué necesitas del board

## Pre-read para el board
[Documento de 1-2 páginas enviado 3 días antes con contexto]

## Asks específicos
| Ask | De quién | Contexto | Urgencia |
|---|---|---|---|

## Temas a evitar / diferir
[Temas que no deben discutirse en esta reunión y por qué]

## Prep para Q&A
| Pregunta probable | Respuesta preparada |
|---|---|
```
