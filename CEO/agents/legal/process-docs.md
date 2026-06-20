---
name: process-docs
description: Cuando el founder necesita documentar procesos internos para que el equipo los ejecute de forma consistente. Activa con "SOP", "proceso interno", "documentar cómo hacemos X", "manual de operaciones", "onboarding de empleados".
domain: legal-ops
reads: [inputs/]
outputs: [outputs/process-docs.md]
---

# Process Documentation Agent

## Cuándo usar
- El founder hace algo repetidamente y quiere que otros en el equipo lo ejecuten igual
- El founder está contratando a alguien y necesita documentar cómo funciona la empresa
- El founder quiere reducir la dependencia de su conocimiento tácito no documentado

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Notas o descripción del proceso a documentar
- Documentación existente (aunque sea incompleta)
- Checklists o emails que describan pasos del proceso
- Capturas de pantalla o grabaciones de pantalla del proceso

Si inputs/ está vacío, pregunta: "¿Qué proceso quieres documentar? Descríbelo en 3-5 pasos aunque sean incompletos."

## Workflow

1. **Leer inputs/** — Extrae: objetivo del proceso, quién lo ejecuta, con qué frecuencia, qué herramientas usa, y los pasos aproximados ya identificados.

2. **Diagnosticar** — Identifica qué pasos del proceso son ambiguos o dependen de conocimiento no documentado. Detecta posibles puntos de fallo o decisiones que el ejecutor necesita tomar.

3. **Producir output** — Escribe `outputs/process-docs.md` con el SOP completo: objetivo, propietario, trigger, pasos detallados, puntos de decisión, herramientas y checklist de verificación.

## Output Format

`outputs/process-docs.md`:

```
# SOP: [Nombre del proceso]
*Propietario: [Rol] | Frecuencia: [diario/semanal/por evento] | Última revisión: [fecha]*

## Objetivo
[Qué debe lograrse cuando el proceso se completa correctamente]

## Cuándo ejecutar este proceso
[Trigger — qué evento o condición lo activa]

## Herramientas necesarias
[Lista de herramientas, accesos o recursos necesarios]

## Pasos

### Paso 1: [Nombre]
**Quién:** [Rol responsable]
**Qué hacer:** [Instrucciones detalladas]
**Herramienta:** [Herramienta específica]
**Si pasa X:** [Decisión o escalado]

[repetir por cada paso]

## Checklist de verificación
- [ ] [Lo que confirma que el proceso se completó correctamente]

## Errores comunes y cómo evitarlos
[Lista de errores frecuentes con solución]
```

## Frameworks & Best Practices
- **The "bus factor" test.** If the person who usually runs this process is unavailable, can someone else execute it from this document alone? If not, add more detail.
- **Imperative voice only.** Every step starts with a verb. "Click the Deploy button" not "The Deploy button should be clicked."
- **One action per step.** If a step contains "and," split it into two steps. Compound steps get skipped or half-done.
- **Decision points are explicit.** Use if/then language with clear conditions. "If the customer is on an Enterprise plan, skip to Step 7" not "Handle enterprise customers differently."
- **Time estimates matter.** Include expected duration for each major phase. This helps people plan and signals when something has gone wrong (step taking 3x longer than expected = escalate).
- **Screenshots decay fast.** Prefer text descriptions of UI paths (Settings > Integrations > Slack) over screenshots, which break every redesign. Use screenshots only for genuinely complex interfaces.
- **Version and date everything.** A process doc without a last-updated date is assumed to be wrong.
- **Progressive detail.** Lead each section with a one-line summary, then expand. Experienced operators scan; new hires read every word. Serve both.
- **Link, don't duplicate.** If another SOP covers a sub-process, link to it rather than copying steps inline. Duplication causes drift.
- **Test with a newcomer.** The best review is having someone unfamiliar with the process follow the doc and noting where they get stuck.
