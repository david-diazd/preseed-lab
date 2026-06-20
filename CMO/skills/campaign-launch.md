---
name: campaign-launch
description: Checklist end-to-end para lanzar una campaña de marketing. Activa con "lanzar campaña", "campaign launch", "nueva campaña", "campaign checklist".
type: skill
scope: CMO
chains: [CMO/agents/marketing/launch-strategy, CMO/agents/marketing/content-strategy, CMO/agents/brand/messaging-framework]
reads: [inputs/]
outputs: [outputs/campaign-launch.md]
---

# Campaign Launch Skill

## Cuándo usar
- Al planificar una campaña de marketing (producto, contenido, paid)
- Para asegurar que no falta ningún paso antes del lanzamiento
- Para coordinar assets, copies y canales

## Qué leer en inputs/
- Brief de campaña o descripción del objetivo
- Assets disponibles (creativos, copies, landing pages)
- Presupuesto asignado
- Calendario y fechas clave

Si inputs/ está vacío, pregunta: "¿Cuál es el objetivo de la campaña, a quién va dirigida, qué presupuesto tienes y cuándo la lanzas?"

## Output Format

```
# Campaign Launch — [Nombre campaña] — [Fecha]

## Objetivo
| Dimensión | Detalle |
|---|---|
| Goal | [Objetivo específico y medible] |
| Audiencia | [ICP de la campaña] |
| Budget | |
| Duración | [Fecha inicio - fin] |

## Pre-launch checklist
- [ ] Messaging aprobado
- [ ] Landing page live y testeada
- [ ] UTM parameters configurados
- [ ] Analytics/tracking verificado
- [ ] Creativos finales en todas las dimensiones
- [ ] Copies por canal listos
- [ ] Email sequences programadas
- [ ] Social posts programados
- [ ] Paid ads configuradas (no publicadas)
- [ ] A/B tests definidos
- [ ] Budget distribuido por canal
- [ ] Equipo alineado sobre timeline

## Assets por canal
| Canal | Asset | Status | Owner | Link |
|---|---|---|---|---|

## Copies
### Email
- Subject: [texto]
- Preview text: [texto]
- CTA: [texto]

### Social
- LinkedIn: [texto]
- Twitter: [texto]
- Instagram: [texto]

### Paid
- Headline: [texto]
- Description: [texto]
- CTA: [texto]

## Timeline
| Día | Canal | Acción | Status |
|---|---|---|---|

## KPIs
| Métrica | Target | Actual | Status |
|---|---|---|---|

## Post-campaign
- [ ] Métricas recopiladas
- [ ] Informe de resultados generado
- [ ] Learnings documentados
- [ ] Decisión sobre next steps
```
