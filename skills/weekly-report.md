---
name: weekly-report
description: Genera un reporte semanal de progreso del equipo. Activa con "reporte semanal", "weekly update", "standup", "qué hicimos esta semana", "weekly report".
type: skill
scope: common
reads: [inputs/]
outputs: [outputs/weekly-report.md]
---

# Weekly Report Skill

## Cuándo usar
- Cada lunes para generar el reporte de la semana anterior
- Para preparar un update para inversores o advisors
- Para alinear al equipo sobre prioridades de la semana

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Notas de reuniones de la semana
- Métricas actualizadas
- OKRs o metas del trimestre
- Updates de equipo

Si inputs/ está vacío, pregunta: "¿Cuáles fueron los 3 logros principales de esta semana, los 3 bloqueos y las 3 prioridades para la próxima?"

## Workflow

1. **Leer inputs/** — Extrae: actividades completadas, métricas que cambiaron, bloqueos encontrados, decisiones tomadas.

2. **Estructurar** — Organiza por áreas (producto, growth, fundraising, ops) y conecta con OKRs si existen.

3. **Producir output** — Escribe `outputs/weekly-report.md`.

## Output Format

```
# Weekly Report — [Startup] — Semana del [fecha]

## Highlights
- 🟢 [Logro principal 1]
- 🟢 [Logro principal 2]
- 🟢 [Logro principal 3]

## Métricas clave
| Métrica | Semana anterior | Esta semana | Δ |
|---|---|---|---|

## Por área
### Producto
- Completado: ...
- En progreso: ...

### Growth
- Completado: ...
- En progreso: ...

### Fundraising / Ops
- Completado: ...
- En progreso: ...

## Bloqueos
| Bloqueo | Impacto | Acción necesaria | Owner |
|---|---|---|---|

## Prioridades próxima semana
1. [Prioridad con owner y deadline]
2. [Siguiente]
3. [Siguiente]

## Decisiones pendientes
| Decisión | Contexto | Deadline |
|---|---|---|
```
