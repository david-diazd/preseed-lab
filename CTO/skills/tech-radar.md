---
name: tech-radar
description: Evalúa tecnologías emergentes relevantes para la startup. Activa con "tech radar", "nuevas tecnologías", "qué tecnologías evaluar", "radar tecnológico", "technology assessment".
type: skill
scope: CTO
chains: [CTO/agents/engineering/tech-stack-evaluation]
reads: [inputs/]
outputs: [outputs/tech-radar.md]
web_search: true
---

# Tech Radar Skill

## Cuándo usar
- Revisión trimestral de tecnologías emergentes
- Cuando el equipo se pregunta si adoptar una nueva herramienta/framework
- Para informar al equipo sobre qué tecnologías vigilar

## Qué leer en inputs/
- Stack tecnológico actual
- Problemas técnicos que podrían resolverse con nueva tecnología
- Lista de tecnologías que el equipo quiere evaluar

Si inputs/ está vacío, pregunta: "¿Cuál es tu stack actual y hay alguna tecnología o herramienta que estés considerando adoptar?"

## Output Format

```
# Tech Radar — [Startup] — Q[N] [Año]

## Adopt (usar en producción)
| Tecnología | Por qué | Riesgo | Impact |
|---|---|---|---|

## Trial (probar en proyecto acotado)
| Tecnología | Hipótesis | Timeline | Criterio de éxito |
|---|---|---|---|

## Assess (investigar y evaluar)
| Tecnología | Potencial | Cuándo evaluar | Quién |
|---|---|---|---|

## Hold (no adoptar ahora)
| Tecnología | Por qué no ahora | Reconsiderar cuándo |
|---|---|---|

## Cambios desde el último radar
| Tecnología | Movimiento | Razón |
|---|---|---|

## Tendencias relevantes
1. [Tendencia tecnológica con impacto en el producto]
2. [Siguiente]
```
