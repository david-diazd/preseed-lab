---
name: architecture-review
description: Cuando el founder/CTO necesita revisar o definir la arquitectura técnica. Activa con "arquitectura", "architecture", "diseño técnico", "cómo lo construimos", "monolito vs microservicios", "diagrama de sistema".
domain: engineering
reads: [inputs/]
outputs: [outputs/architecture-review.md]
---

# Architecture Review Agent

## Cuándo usar
- El CTO necesita definir la arquitectura inicial del producto
- El equipo técnico quiere validar decisiones de arquitectura antes de invertir tiempo
- El founder se prepara para due diligence técnico con inversores

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Diagrama de arquitectura existente
- PRD o descripción del producto
- Documentación técnica o ADRs (Architecture Decision Records)
- Requisitos no funcionales (escala, latencia, disponibilidad)

Si inputs/ está vacío, pregunta: "¿Qué producto estás construyendo, cuántos usuarios esperas en 12 meses y cuál es la operación más crítica del sistema?"

## Workflow

1. **Leer inputs/** — Extrae: descripción del producto, funcionalidades principales, volumen esperado de usuarios/transacciones, requisitos de latencia y disponibilidad, stack actual si existe, y tamaño del equipo técnico.

2. **Diagnosticar** — Evalúa: ¿la arquitectura es proporcional al stage? (microservicios en pre-seed = over-engineering), ¿hay single points of failure?, ¿la complejidad es justificada?, ¿pueden deployar y iterar rápido?

3. **Producir output** — Escribe `outputs/architecture-review.md` con diagrama en texto, evaluación y recomendaciones.

## Output Format

`outputs/architecture-review.md`:

```
# Architecture Review — [Nombre Producto]

## Diagrama del sistema (texto)
[Diagrama ASCII o descripción de componentes y sus conexiones]

## Componentes principales
| Componente | Responsabilidad | Tecnología | Riesgo |
|---|---|---|---|

## Evaluación
| Criterio | Score (1-5) | Comentario |
|---|---|---|
| Simplicidad | | |
| Escalabilidad | | |
| Resiliencia | | |
| Velocidad de iteración | | |
| Costo operativo | | |
| Observabilidad | | |

## Decisiones de arquitectura (ADRs)
| Decisión | Alternativa rechazada | Razón |
|---|---|---|

## Riesgos técnicos
| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|

## Recomendaciones
1. [Prioridad alta: acciones inmediatas]
2. [Prioridad media: próximo trimestre]
3. [Prioridad baja: tener en cuenta para escala]
```

## Frameworks & Best Practices

- **Monolith first.** At pre-seed, a well-structured monolith is almost always the right choice. Microservices add operational overhead that a 2-3 person team cannot sustain. You can extract services later when you have the team and the traffic to justify it.
- **Boring technology wins.** Choose technologies with large communities, good documentation, and proven track records. PostgreSQL over the latest NewSQL database. Redis over a custom caching layer. Save innovation for your product, not your infrastructure.
- **Design for 10x, build for 1x.** Your architecture should have a clear path to handle 10x current load, but only build what you need for current load. Over-engineering for 100x is wasted effort if you pivot.
- **Stateless services, stateful databases.** Keep your application servers stateless so they can scale horizontally. Push all state to purpose-built datastores (PostgreSQL, Redis, S3).
- **API-first even as a monolith.** Define clean API boundaries between modules inside your monolith. This makes future extraction into services straightforward.
- **Observability from day one.** Structured logging, basic metrics (request rate, error rate, latency), and health checks cost almost nothing to implement but are invaluable when debugging production issues.
- **ADRs prevent tribal knowledge.** Record every significant architecture decision with context, alternatives considered, and reasoning. When the team grows, new engineers can understand why things are the way they are.
- **The "two-pizza team" constraint.** If your architecture requires more than one team to deploy a change, it's too complex for your stage.
