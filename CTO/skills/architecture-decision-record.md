---
name: architecture-decision-record
description: Documenta una decisión de arquitectura con contexto y alternativas. Activa con "ADR", "architecture decision", "decisión técnica", "por qué elegimos X", "documentar decisión".
type: skill
scope: CTO
chains: [CTO/agents/engineering/architecture-review]
reads: [inputs/]
outputs: [outputs/adr-NNN.md]
---

# Architecture Decision Record Skill

## Cuándo usar
- Cuando el equipo toma una decisión técnica significativa
- Para documentar el "por qué" detrás de una elección de tecnología o diseño
- Para que futuros miembros del equipo entiendan decisiones pasadas

## Qué leer en inputs/
- Contexto de la decisión (problema, constraints)
- Alternativas evaluadas
- Pruebas de concepto realizadas

Si inputs/ está vacío, pregunta: "¿Qué decisión técnica necesitas documentar, cuáles fueron las alternativas y por qué elegiste esta opción?"

## Output Format

```
# ADR-[NNN]: [Título de la decisión]

**Status:** Proposed / Accepted / Deprecated / Superseded by ADR-XXX
**Date:** [Fecha]
**Deciders:** [Quién participó]

## Context
[Qué situación motivó esta decisión. Qué problema resolvemos.]

## Decision
[La decisión tomada, en una frase clara.]

## Alternatives Considered

### Opción A: [Nombre] (elegida)
- Pros: [lista]
- Cons: [lista]

### Opción B: [Nombre]
- Pros: [lista]
- Cons: [lista]

### Opción C: [Nombre]
- Pros: [lista]
- Cons: [lista]

## Consequences

### Positivas
- [Consecuencia positiva]

### Negativas
- [Trade-off aceptado]

### Risks
- [Riesgo conocido y mitigación]

## Review Date
[Cuándo revisar si esta decisión sigue siendo correcta]
```
