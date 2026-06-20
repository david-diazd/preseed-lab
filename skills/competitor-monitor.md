---
name: competitor-monitor
description: Monitorea cambios en competidores y genera alertas. Activa con "monitorear competencia", "qué hizo X", "competitor update", "cambios en competidores", "qué está pasando con la competencia".
type: skill
scope: common
reads: [inputs/]
outputs: [outputs/competitor-update.md]
web_search: true
---

# Competitor Monitor Skill

## Cuándo usar
- Revisión periódica (quincenal/mensual) de la competencia
- Cuando un competidor lanza algo nuevo o levanta una ronda
- Para preparar una reunión donde la competencia será tema

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Análisis de competidores previo
- Lista de competidores a monitorear
- Último competitor update

Si inputs/ está vacío, pregunta: "¿Quiénes son tus 3-5 competidores principales que quieres monitorear?"

## Workflow

1. **Leer inputs/** — Extrae: lista de competidores, último análisis, métricas de referencia.
2. **Web search** — Busca por cada competidor: últimas noticias, product launches, fundraising, hiring, pricing changes, reviews recientes.
3. **Producir output** — Escribe `outputs/competitor-update.md`.

## Output Format

```
# Competitor Update — [Fecha]

## Alertas importantes
| Competidor | Evento | Impacto para nosotros | Acción sugerida |
|---|---|---|---|

## Por competidor

### [Competidor 1]
- **Producto:** [Cambios recientes]
- **Funding:** [Rondas o cambios financieros]
- **Equipo:** [Hires notables o cambios]
- **Marketing:** [Campañas, partnerships, eventos]
- **Pricing:** [Cambios en pricing o modelo]
- **Señal:** 🟢 Sin cambios / 🟡 Cambio menor / 🔴 Cambio significativo

### [Competidor 2]
...

## Tendencias del landscape
[Patrones observados a nivel de mercado]

## Implicaciones estratégicas
1. [Acción recomendada basada en movimientos de la competencia]
2. [Siguiente]

## Fuentes
[Links usados]
```
