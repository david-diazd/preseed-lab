---
name: incident-postmortem
description: Genera un post-mortem estructurado después de un incidente. Activa con "post-mortem", "postmortem", "incidente", "qué pasó", "root cause", "outage", "caída del sistema".
type: skill
scope: CTO
reads: [inputs/]
outputs: [outputs/postmortem.md]
---

# Incident Postmortem Skill

## Cuándo usar
- Después de cualquier incidente que afectó a usuarios
- Cuando algo salió mal en producción
- Para documentar el aprendizaje y prevenir recurrencia

## Qué leer en inputs/
- Timeline del incidente
- Logs o capturas de error
- Comunicación durante el incidente (Slack, emails)
- Métricas de impacto

Si inputs/ está vacío, pregunta: "¿Qué pasó, cuándo empezó, cuándo se resolvió, cuántos usuarios fueron afectados, y cuál fue la causa?"

## Output Format

```
# Post-Mortem — [Título del incidente] — [Fecha]

## Resumen
| Dimensión | Detalle |
|---|---|
| Severidad | P0/P1/P2/P3 |
| Duración | [tiempo total] |
| Usuarios afectados | [número/porcentaje] |
| Impacto en revenue | [si aplica] |
| Status | Resuelto / Mitigado / En progreso |

## Timeline
| Hora | Evento | Quién |
|---|---|---|

## Root Cause
[Descripción técnica de la causa raíz — sin culpar a personas]

## 5 Whys
1. ¿Por qué [síntoma]? → Porque [causa 1]
2. ¿Por qué [causa 1]? → Porque [causa 2]
3. ¿Por qué [causa 2]? → Porque [causa 3]
4. ¿Por qué [causa 3]? → Porque [causa 4]
5. ¿Por qué [causa 4]? → Porque [causa raíz]

## Qué salió bien
- [Cosas que funcionaron en la respuesta]

## Qué salió mal
- [Cosas que empeoraron o ralentizaron la resolución]

## Action items
| # | Acción | Owner | Deadline | Tipo |
|---|---|---|---|---|
| 1 | | | | Prevent / Detect / Mitigate |
| 2 | | | | |

## Lecciones aprendidas
1. [Lección aplicable a futuro]
2. [Siguiente]
```
