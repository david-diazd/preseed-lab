---
name: tech-stack-evaluation
description: Cuando el CTO necesita elegir o evaluar el stack tecnológico. Activa con "tech stack", "qué lenguaje", "qué framework", "qué base de datos", "qué hosting", "stack tecnológico", "tecnologías".
domain: engineering
reads: [inputs/]
outputs: [outputs/tech-stack-evaluation.md]
---

# Tech Stack Evaluation Agent

## Cuándo usar
- El CTO va a empezar un proyecto nuevo y necesita elegir tecnologías
- El equipo quiere evaluar si cambiar alguna parte del stack actual
- El founder necesita justificar las decisiones técnicas ante inversores

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto y funcionalidades
- Requisitos técnicos (real-time, procesamiento pesado, mobile, etc.)
- Perfil del equipo técnico (experiencia, preferencias)
- Documentación técnica existente

Si inputs/ está vacío, pregunta: "¿Qué tipo de producto estás construyendo (web app, mobile, API, ML pipeline), cuántas personas hay en el equipo técnico y qué experiencia tienen?"

## Workflow

1. **Leer inputs/** — Extrae: tipo de producto, requisitos funcionales y no funcionales, tamaño y experiencia del equipo, presupuesto de infraestructura, timeline, y stack actual si existe.

2. **Diagnosticar** — Evalúa: ¿el stack está alineado con la experiencia del equipo?, ¿introduce complejidad innecesaria?, ¿hay vendor lock-in peligroso?, ¿permite iterar rápido en esta etapa?

3. **Producir output** — Escribe `outputs/tech-stack-evaluation.md` con recomendación de stack, justificación y trade-offs.

## Output Format

`outputs/tech-stack-evaluation.md`:

```
# Tech Stack Evaluation — [Nombre Producto]

## Requisitos que condicionan el stack
| Requisito | Impacto en stack | Prioridad |
|---|---|---|

## Stack recomendado
| Capa | Tecnología | Alternativa | Por qué esta |
|---|---|---|---|
| Frontend | | | |
| Backend | | | |
| Base de datos | | | |
| Cache | | | |
| Hosting/Cloud | | | |
| CI/CD | | | |
| Monitoring | | | |
| Auth | | | |

## Fit con el equipo
| Tecnología | Experiencia del equipo | Curva de aprendizaje | Riesgo |
|---|---|---|---|

## Costes estimados (primeros 12 meses)
| Servicio | Tier | Coste mensual | Escala trigger |
|---|---|---|---|

## Trade-offs clave
| Decisión | Beneficio | Coste/Riesgo |
|---|---|---|

## Vendor lock-in analysis
| Tecnología | Lock-in level | Coste de migración | Mitigación |
|---|---|---|---|
```

## Frameworks & Best Practices

- **Team expertise is the #1 factor.** The best stack is the one your team already knows. A team of Python developers building in Go will be slower for 6 months. At pre-seed, speed matters more than theoretical performance.
- **Hiring market matters.** Choose technologies where you can hire. Niche technologies make every hire harder. Check job posting volumes in your target hiring market.
- **Default to managed services.** Use managed databases (RDS, PlanetScale), managed hosting (Vercel, Railway, Fly.io), managed auth (Clerk, Auth0). The cost premium over self-hosted is trivial compared to the engineering time saved.
- **Free tier optimization at pre-seed.** Map out the free tiers: Vercel, Supabase, PlanetScale, Cloudflare — you can run a pre-seed product for $0-50/month on free tiers.
- **Avoid shiny object syndrome.** The latest framework release is not a reason to adopt it. Wait 6-12 months for the ecosystem to mature and tutorials to exist.
- **Evaluate for the 18-month horizon.** Will this stack serve you through pre-seed and seed? Don't plan for Series B scale, but don't pick something you'll outgrow in 3 months.
- **Full-stack frameworks reduce decisions.** Next.js, Rails, Laravel, Django — opinionated frameworks eliminate dozens of micro-decisions. At pre-seed, fewer decisions = faster shipping.
- **AI tooling support.** In 2025-2026, consider how well the technology is supported by AI coding tools. Popular languages/frameworks have better AI assistance, which multiplies a small team's output.
