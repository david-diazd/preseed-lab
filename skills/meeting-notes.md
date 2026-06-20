---
name: meeting-notes
description: Estructura notas de reunión y extrae action items. Activa con "notas de reunión", "meeting notes", "resumen de reunión", "action items", "minuta".
type: skill
scope: common
reads: [inputs/]
outputs: [outputs/meeting-notes.md]
---

# Meeting Notes Skill

## Cuándo usar
- Después de una reunión para estructurar las notas
- Para extraer action items claros con owners y deadlines
- Para documentar decisiones tomadas en reunión

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Notas crudas de la reunión
- Transcripción de la call
- Agenda previa

Si inputs/ está vacío, pregunta: "Pega tus notas de la reunión o cuéntame qué se discutió, qué se decidió y qué quedó pendiente."

## Workflow

1. **Leer inputs/** — Extrae: temas discutidos, decisiones tomadas, tareas asignadas, preguntas sin responder.
2. **Estructurar** — Organiza por temas, separa decisiones de discusiones, y crea action items con formato RACI.
3. **Producir output** — Escribe `outputs/meeting-notes.md`.

## Output Format

```
# Meeting Notes — [Tema] — [Fecha]

**Asistentes:** [Lista]
**Duración:** [X min]

## Resumen ejecutivo
[2-3 frases con lo más importante]

## Temas discutidos

### 1. [Tema]
- [Puntos clave discutidos]
- **Decisión:** [Si se tomó alguna]
- **Pendiente:** [Si quedó sin resolver]

### 2. [Tema]
...

## Decisiones tomadas
| # | Decisión | Contexto | Owner |
|---|---|---|---|

## Action items
| # | Tarea | Owner | Deadline | Status |
|---|---|---|---|---|
| 1 | | | | ⬜ |
| 2 | | | | ⬜ |

## Preguntas sin responder
| Pregunta | Quién debe responder | Deadline |
|---|---|---|

## Próxima reunión
- Fecha: [Si se acordó]
- Temas a tratar: [Si se definieron]
```
