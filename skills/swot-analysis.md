---
name: swot-analysis
description: Genera un análisis SWOT completo de la startup. Activa con "SWOT", "fortalezas y debilidades", "análisis estratégico", "dónde estamos parados".
type: skill
scope: common
reads: [inputs/]
outputs: [outputs/swot-analysis.md]
---

# SWOT Analysis Skill

## Cuándo usar
- El equipo necesita una foto completa de la posición estratégica
- Antes de una sesión de planificación estratégica
- Para preparar una reunión con inversores o advisors

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck
- Análisis de competidores
- Métricas del negocio
- Feedback de clientes
- Modelo financiero

Si inputs/ está vacío, pregunta: "Cuéntame sobre tu startup: qué hacen, cómo van las métricas, quién es la competencia, y qué te preocupa más."

## Workflow

1. **Leer inputs/** — Extrae: datos de todas las áreas disponibles.
2. **Analizar** — Cruza información interna (fortalezas/debilidades) con externa (oportunidades/amenazas).
3. **Producir output** — Escribe `outputs/swot-analysis.md`.

## Output Format

```
# SWOT Analysis — [Nombre Startup] — [Fecha]

## Matriz SWOT

|  | Positivo | Negativo |
|---|---|---|
| **Interno** | **Fortalezas** | **Debilidades** |
|  | • [F1] | • [D1] |
|  | • [F2] | • [D2] |
|  | • [F3] | • [D3] |
| **Externo** | **Oportunidades** | **Amenazas** |
|  | • [O1] | • [A1] |
|  | • [O2] | • [A2] |
|  | • [O3] | • [A3] |

## Estrategias cruzadas

### FO (Fortalezas × Oportunidades) — Atacar
| Estrategia | Fortaleza | Oportunidad |
|---|---|---|

### DO (Debilidades × Oportunidades) — Mejorar
| Estrategia | Debilidad a resolver | Oportunidad que habilita |
|---|---|---|

### FA (Fortalezas × Amenazas) — Defender
| Estrategia | Fortaleza que protege | Amenaza |
|---|---|---|

### DA (Debilidades × Amenazas) — Evitar
| Riesgo | Debilidad | Amenaza | Mitigación |
|---|---|---|---|

## Top 3 acciones estratégicas
1. [Acción con mayor impacto — basada en el cruce FO]
2. [Acción defensiva más urgente — basada en DA]
3. [Quick win de mejora — basada en DO]
```
