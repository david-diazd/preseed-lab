---
name: technical-due-diligence
description: Cuando el CTO necesita prepararse para un due diligence técnico de inversores. Activa con "due diligence técnico", "technical DD", "revisión técnica de inversores", "preparar para DD".
domain: engineering
reads: [inputs/]
outputs: [outputs/technical-due-diligence.md]
---

# Technical Due Diligence Agent

## Cuándo usar
- La startup va a pasar por un due diligence técnico como parte de una ronda
- El CTO quiere anticipar preguntas técnicas de inversores
- El equipo quiere autoevaluar la madurez técnica antes de fundraising

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Documentación técnica y de arquitectura
- Métricas de desarrollo (deploy frequency, cycle time)
- Código fuente o repositorios (estructura)
- Historial de incidentes o post-mortems

Si inputs/ está vacío, pregunta: "¿En qué ronda estás, cuántas personas tiene el equipo técnico, y cuáles son las 3 cosas de las que estás más orgulloso y las 3 que más te preocupan técnicamente?"

## Workflow

1. **Leer inputs/** — Extrae: stack tecnológico, tamaño del equipo, procesos de desarrollo, métricas de ingeniería, propiedad intelectual, y estado de seguridad/compliance.

2. **Diagnosticar** — Evalúa cada área que los inversores revisarán: code quality, architecture decisions, team capabilities, development velocity, security posture, technical risk, IP ownership.

3. **Producir output** — Escribe `outputs/technical-due-diligence.md` con self-assessment, áreas de mejora, y preparación para preguntas comunes.

## Output Format

`outputs/technical-due-diligence.md`:

```
# Technical Due Diligence Prep — [Nombre Startup]

## Self-Assessment
| Área | Score (1-5) | Evidencia | Risk level |
|---|---|---|---|
| Architecture & scalability | | | |
| Code quality & practices | | | |
| Security & compliance | | | |
| Team & talent | | | |
| Development velocity | | | |
| Technical differentiation | | | |
| IP & ownership | | | |
| Infrastructure & operations | | | |

## Fortalezas técnicas (lead with these)
1. [Fortaleza con evidencia cuantitativa]
2. [Siguiente]
3. [Siguiente]

## Áreas de mejora (address proactively)
| Área | Estado actual | Plan de mejora | Timeline |
|---|---|---|---|

## Preguntas frecuentes de DD y respuestas sugeridas
| Pregunta | Respuesta recomendada | Evidencia |
|---|---|---|
| "¿Por qué este stack?" | | |
| "¿Cómo escalan a 100x?" | | |
| "¿Cuál es su mayor riesgo técnico?" | | |
| "¿Cómo protegen la IP?" | | |
| "¿Cuánto de esto es open source vs propietario?" | | |
| "¿Qué pasa si el CTO se va?" | | |

## Documentación a preparar
- [ ] Architecture diagram (actualizado)
- [ ] Development process documentation
- [ ] Security practices summary
- [ ] Team org chart with responsibilities
- [ ] IP assignment agreements
- [ ] Key technical metrics dashboard

## Red flags que arreglar antes del DD
[Lista de issues que un reviewer técnico encontraría y que puedes arreglar proactivamente]
```

## Frameworks & Best Practices

- **Honesty wins DD.** Investors doing technical DD can spot bullshit. Present genuine strengths and acknowledge real weaknesses with mitigation plans. This builds trust faster than pretending everything is perfect.
- **The "bus factor" question is real.** If one person leaving would cripple the product, that's a legitimate risk. Mitigate with documentation, code reviews, and knowledge sharing. Have a credible answer.
- **Code quality > code complexity.** Reviewers aren't impressed by complex architecture. They're impressed by clean, well-tested, well-documented code that ships reliably.
- **IP assignment is non-negotiable.** Every contributor (employees, contractors, founders) must have signed IP assignment agreements. Missing IP assignment can kill a deal.
- **Open source dependencies are fine.** Using open source doesn't reduce your IP value. What matters is that your proprietary code (business logic, data models, algorithms) is owned by the company with proper licenses for open-source dependencies.
- **Demo the development process.** Walk through: "This is how a feature goes from idea to production." Show the PR process, tests, deployment, monitoring. Process maturity impresses more than architecture slides.
- **Metrics speak louder than claims.** "We deploy 5 times per day with a 2% rollback rate" is more convincing than "we have a robust CI/CD pipeline."
- **Prepare for code walkthrough.** Pick 2-3 areas of the codebase that showcase your best practices. Walk through them explaining decisions. This is your chance to show craftsmanship.
