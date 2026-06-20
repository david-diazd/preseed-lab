---
name: fundraising-pipeline
description: Gestiona el pipeline de fundraising de principio a fin. Activa con "pipeline de inversores", "fundraising pipeline", "estado de la ronda", "seguimiento inversores", "CRM de inversores".
type: skill
scope: CEO
chains: [CEO/agents/fundraising/investor-research, CEO/agents/fundraising/fundraising-email, CEO/agents/fundraising/pitch-deck]
reads: [inputs/]
outputs: [outputs/fundraising-pipeline.md]
---

# Fundraising Pipeline Skill

## Cuándo usar
- El founder está en proceso de fundraising y necesita organizar el pipeline
- Para hacer seguimiento de conversations con inversores
- Para preparar el siguiente paso con cada inversor

## Qué leer en inputs/
- Lista de inversores contactados y su estado
- Notas de reuniones con inversores
- Term sheets o SAFEs recibidos
- Feedback recibido de inversores

Si inputs/ está vacío, encadena: primero ejecuta `@CEO/agents/fundraising/investor-research.md` para generar la lista inicial.

## Output Format

```
# Fundraising Pipeline — [Startup] — [Fecha]

## Resumen de la ronda
| Dimensión | Valor |
|---|---|
| Objetivo de ronda | |
| Levantado hasta ahora | |
| Inversores en pipeline | |
| Meetings completados | |
| Term sheets recibidos | |

## Pipeline por stage
### 🎯 Target (sin contactar)
| Inversor | Tesis | Check size | Fit score | Intro path |
|---|---|---|---|---|

### 📧 Contactado (esperando respuesta)
| Inversor | Fecha contacto | Vía | Follow-up date |
|---|---|---|---|

### 📞 En conversación
| Inversor | Stage | Último contacto | Próximo paso | Sentimiento |
|---|---|---|---|---|

### 📋 Due Diligence
| Inversor | Docs pedidos | Entregados | Pendientes |
|---|---|---|---|

### ✅ Term Sheet / Comprometido
| Inversor | Monto | Valoración | Condiciones | Status |
|---|---|---|---|---|

### ❌ Pasó / No fit
| Inversor | Razón | Aprendizaje | Reconectar en |
|---|---|---|---|

## Próximas acciones (esta semana)
| Acción | Inversor | Deadline |
|---|---|---|

## Métricas del funnel
| Métrica | Valor |
|---|---|
| Conversion rate: contacto → meeting | |
| Conversion rate: meeting → follow-up | |
| Conversion rate: follow-up → term sheet | |
| Tiempo promedio del ciclo | |
```
