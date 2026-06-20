---
name: technical-debt
description: Cuando el CTO necesita evaluar y priorizar deuda técnica. Activa con "deuda técnica", "technical debt", "refactoring", "código legacy", "tech debt", "calidad del código".
domain: engineering
reads: [inputs/]
outputs: [outputs/technical-debt.md]
---

# Technical Debt Assessment Agent

## Cuándo usar
- El equipo siente que está yendo cada vez más lento y no sabe por qué
- El CTO necesita justificar tiempo de refactoring ante el founder/board
- Antes de una ronda, para preparar el due diligence técnico

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Documentación técnica o post-mortems
- Listado de bugs recurrentes
- Métricas de velocidad del equipo (cycle time, deploy frequency)
- Diagramas de arquitectura
- Notas sobre problemas técnicos recurrentes

Si inputs/ está vacío, pregunta: "¿Qué tarea que antes tomaba horas ahora toma días? ¿Qué partes del sistema le da miedo tocar al equipo?"

## Workflow

1. **Leer inputs/** — Extrae: áreas problemáticas identificadas, frecuencia de bugs, velocidad del equipo, partes del código que nadie quiere tocar, y workarounds acumulados.

2. **Diagnosticar** — Clasifica la deuda en categorías: deliberada ("sabíamos que era un shortcut"), inadvertida ("no sabíamos que esto sería un problema"), bit rot ("era correcto pero ya no lo es"). Evalúa el interés que paga cada deuda.

3. **Producir output** — Escribe `outputs/technical-debt.md` con inventario, priorización y plan de pago.

## Output Format

`outputs/technical-debt.md`:

```
# Technical Debt Assessment — [Nombre Producto]

## Resumen ejecutivo
[Estado general: ¿la deuda es manejable, preocupante o crítica?]

## Inventario de deuda
| ID | Área | Descripción | Tipo | Interés (impacto/mes) | Coste de fix |
|---|---|---|---|---|---|

## Clasificación por tipo
### Deliberada (shortcuts conscientes)
[Lista con contexto de por qué se tomó el shortcut]

### Inadvertida (aprendizaje posterior)
[Lista de cosas que ahora se harían diferente]

### Bit rot (degradación por cambio de contexto)
[Lista de cosas que eran correctas pero ya no lo son]

## Priorización
| Prioridad | ID | ROI (impacto/coste) | Riesgo de no actuar |
|---|---|---|---|

## Plan de pago
| Sprint/Semana | Deuda a abordar | Horas estimadas | Impacto esperado |
|---|---|---|---|

## Regla del 20%
[Recomendación de cuánto tiempo dedicar a deuda técnica por sprint]

## Métricas de salud a trackear
| Métrica | Valor actual | Target | Frecuencia |
|---|---|---|---|
```

## Frameworks & Best Practices

- **Not all debt is bad.** Deliberate technical debt taken consciously to ship faster is a strategic tool. The key is tracking it and paying it down before the interest compounds.
- **Measure the interest, not the principal.** A messy module that nobody touches has zero interest. A messy module that the team changes daily has massive interest. Prioritize by impact on velocity, not by code aesthetics.
- **The "tax" framing works for non-technical stakeholders.** "We're paying a 30% tax on every feature because of X" is more persuasive than "the code is messy."
- **20% rule.** Dedicate ~20% of engineering time to debt reduction. This prevents accumulation without stopping feature work. Adjust up if velocity is declining, down if velocity is stable.
- **Boy Scout Rule.** Leave the code better than you found it. Small improvements on every PR compound over time without requiring dedicated refactoring sprints.
- **Refactoring ≠ rewriting.** Incremental refactoring (extract function, rename, split module) is low risk. Full rewrites are high risk and almost never justified at pre-seed.
- **Track cycle time as a canary.** If the time from "start coding" to "deployed in production" is increasing, technical debt is likely the cause. This metric makes debt visible.
- **Pre-seed debt tolerance is high.** You're supposed to have some debt. The goal is product-market fit, not perfect code. Only fix debt that slows you down meaningfully.
