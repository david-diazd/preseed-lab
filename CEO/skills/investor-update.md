---
name: investor-update
description: Genera un email de investor update mensual. Activa con "investor update", "update a inversores", "email mensual a inversores", "monthly update".
type: skill
scope: CEO
chains: [CEO/agents/fundraising/board-update]
reads: [inputs/]
outputs: [outputs/investor-update.md]
---

# Investor Update Skill

## Cuándo usar
- Primer lunes de cada mes para enviar el update mensual
- Cuando un inversor pide un update ad-hoc
- Para mantener warm a inversores que no invirtieron (aún)

## Qué leer en inputs/
- Métricas del mes
- Logros y hitos alcanzados
- Updates anteriores (para mantener consistencia)

Si inputs/ está vacío, pregunta: "¿Cuáles fueron los 3 highlights del mes, cómo van las métricas clave, y en qué necesitas ayuda?"

## Output Format

```
# Investor Update — [Startup] — [Mes Año]

**Subject line:** [Startup] Update [Mes] — [Un highlight en una frase]

---

Hi [Name],

## TL;DR
[3 bullet points: highlight, métrica, ask]

## Highlights
- ✅ [Logro 1 con número]
- ✅ [Logro 2 con número]
- ✅ [Logro 3 con número]

## Métricas
| Métrica | Mes anterior | Este mes | Δ | Tendencia |
|---|---|---|---|---|
| MRR/Revenue | | | | |
| Usuarios activos | | | | |
| [Métrica clave 3] | | | | |

## Challenges
- [Challenge 1 — qué están haciendo al respecto]
- [Challenge 2 — qué plan tienen]

## Cash position
| Métrica | Valor |
|---|---|
| Cash in bank | |
| Monthly burn | |
| Runway (meses) | |

## Asks
[1-2 asks específicos y accionables — intros, expertise, feedback]

---

Thanks for your support,
[Founder name]
```
