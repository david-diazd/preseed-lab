---
name: devops-setup
description: Cuando el CTO necesita configurar CI/CD, infraestructura o procesos de deployment. Activa con "CI/CD", "deploy", "infraestructura", "DevOps", "pipeline", "staging", "producción", "Docker", "Kubernetes".
domain: engineering
reads: [inputs/]
outputs: [outputs/devops-setup.md]
---

# DevOps Setup Agent

## Cuándo usar
- El equipo necesita configurar su pipeline de CI/CD desde cero
- El CTO quiere mejorar la frecuencia y confiabilidad de los deploys
- El equipo pasa de deploy manual a automatizado

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Documentación técnica o de arquitectura
- Configuración de CI/CD existente
- Descripción del stack y hosting
- Proceso de deployment actual

Si inputs/ está vacío, pregunta: "¿Qué stack usas, dónde está hosteado, cómo deployáis actualmente y cuántas veces al día/semana hacéis deploy?"

## Workflow

1. **Leer inputs/** — Extrae: stack tecnológico, proveedor de cloud/hosting, proceso de deploy actual, frecuencia de deploy, entornos (dev/staging/prod), y pain points del equipo.

2. **Diagnosticar** — Evalúa: ¿el deploy es manual o automatizado?, ¿hay tests en el pipeline?, ¿existe staging?, ¿cuánto tarda un deploy?, ¿hay rollback automatizado?

3. **Producir output** — Escribe `outputs/devops-setup.md` con arquitectura de CI/CD, configuración recomendada y guía de implementación.

## Output Format

`outputs/devops-setup.md`:

```
# DevOps Setup — [Nombre Producto]

## Estado actual
| Dimensión | Actual | Target |
|---|---|---|
| Deploy frequency | | |
| Lead time (commit → prod) | | |
| Change failure rate | | |
| Time to recovery | | |

## Arquitectura de CI/CD
[Diagrama de flujo: commit → test → build → deploy → monitor]

## Entornos
| Entorno | Propósito | URL | Auto-deploy | Datos |
|---|---|---|---|---|
| Development | Local dev | localhost | N/A | Mock/seed |
| Staging | Pre-prod testing | | Sí, desde main | Copy sanitizada |
| Production | Live | | Manual trigger | Real |

## Pipeline de CI
| Step | Herramienta | Tiempo estimado | Bloquea deploy |
|---|---|---|---|
| Lint | | | Sí |
| Type check | | | Sí |
| Unit tests | | | Sí |
| Integration tests | | | Sí |
| Build | | | Sí |
| Security scan | | | No (warn) |

## Pipeline de CD
| Trigger | Acción | Rollback |
|---|---|---|

## Monitoreo post-deploy
| Métrica | Herramienta | Alerta |
|---|---|---|

## Configuración paso a paso
[Guía de implementación con comandos y archivos de configuración]

## Costes
| Servicio | Plan | Coste mensual |
|---|---|---|
```

## Frameworks & Best Practices

- **Ship small, ship often.** Multiple deploys per day with small changes is safer than one big weekly deploy. Small changes = small blast radius = easy rollback.
- **Automate the golden path.** Push to main → tests run → build → deploy to staging → manual approval → deploy to prod. This should work without any human touching a server.
- **No Kubernetes at pre-seed.** Use PaaS (Vercel, Railway, Fly.io, Render) or simple container hosting (ECS Fargate, Cloud Run). Kubernetes requires a dedicated person to manage. You don't have that person.
- **Feature flags over branches.** Long-lived feature branches create merge hell. Ship behind feature flags (LaunchDarkly, Flagsmith, simple ENV vars) to decouple deployment from release.
- **Staging must be realistic.** Staging with no data or fake data doesn't catch real bugs. Use sanitized production data or realistic seed data.
- **Database migrations must be reversible.** Every migration should have a rollback path. Test rollbacks in staging before applying to production.
- **Infrastructure as Code (light version).** At pre-seed, you don't need Terraform. But do version your Dockerfiles, docker-compose, and deployment configs. No manual server configuration.
- **Monitor the four DORA metrics.** Deployment frequency, lead time for changes, change failure rate, time to restore service. These tell you if your DevOps is improving or degrading.
