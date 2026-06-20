---
name: scalability-plan
description: Cuando el CTO necesita planificar cómo escalar el sistema. Activa con "escalar", "scalability", "rendimiento", "performance", "carga", "bottleneck", "cuellos de botella", "usuarios concurrentes".
domain: engineering
reads: [inputs/]
outputs: [outputs/scalability-plan.md]
---

# Scalability Plan Agent

## Cuándo usar
- El producto está creciendo y el equipo anticipa problemas de rendimiento
- Inversores preguntan "¿qué pasa si tienen 100x usuarios?"
- El equipo detecta degradación de rendimiento con el crecimiento actual

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Documentación de arquitectura
- Métricas de rendimiento actuales
- Proyecciones de crecimiento de usuarios
- Modelo financiero (para vincular escala con costes)

Si inputs/ está vacío, pregunta: "¿Cuántos usuarios/requests tienes hoy, cuántos esperas en 12 meses, y cuál es la operación más lenta o costosa de tu sistema?"

## Workflow

1. **Leer inputs/** — Extrae: arquitectura actual, volumen de datos y requests, proyecciones de crecimiento, operaciones críticas, y problemas de rendimiento actuales.

2. **Diagnosticar** — Identifica bottlenecks actuales y futuros: ¿dónde romperá primero? (DB, API, procesamiento, storage). Evalúa si los problemas son de escala vertical u horizontal.

3. **Producir output** — Escribe `outputs/scalability-plan.md` con análisis de bottlenecks, plan de escala por fase, y costes proyectados.

## Output Format

`outputs/scalability-plan.md`:

```
# Scalability Plan — [Nombre Producto]

## Perfil de carga actual
| Métrica | Valor actual | Tendencia |
|---|---|---|
| Usuarios activos diarios | | |
| Requests/segundo (p50) | | |
| Requests/segundo (p99) | | |
| Tamaño de DB | | |
| Response time (p50) | | |
| Response time (p99) | | |

## Bottleneck analysis
| Componente | Capacidad actual | Punto de quiebre | Señal de alerta |
|---|---|---|---|

## Plan de escala por fase

### Fase 1: [Usuarios actuales → 10x] — Optimizar
| Acción | Impacto | Esfuerzo | Prioridad |
|---|---|---|---|

### Fase 2: [10x → 50x] — Escalar horizontalmente
| Acción | Impacto | Esfuerzo | Prioridad |
|---|---|---|---|

### Fase 3: [50x → 100x+] — Re-arquitectar
| Acción | Impacto | Esfuerzo | Prioridad |
|---|---|---|---|

## Costes de infraestructura por fase
| Fase | Usuarios | Infra mensual | Coste por usuario |
|---|---|---|---|

## Quick wins (implementar ya)
1. [Acción de bajo esfuerzo / alto impacto]
2. [Siguiente]
3. [Siguiente]

## Métricas a monitorear
| Métrica | Herramienta | Alerta threshold |
|---|---|---|
```

## Frameworks & Best Practices

- **Premature optimization is the root of all evil.** Don't solve scaling problems you don't have. But do know where the bottlenecks will appear. Think about scale, don't build for scale.
- **Database is almost always the bottleneck.** Read replicas, connection pooling, query optimization, and proper indexing solve 90% of database scaling issues before you need sharding.
- **Cache aggressively.** Redis for hot data, CDN for static assets, HTTP caching headers for API responses. A cache hit is 100x cheaper than a database query.
- **Background jobs for anything non-blocking.** Email sending, report generation, data processing — anything that doesn't need to be in the HTTP response cycle should be in a job queue.
- **Horizontal before vertical.** Adding more servers is easier and cheaper than upgrading to bigger servers. Design stateless services that can run as multiple instances behind a load balancer.
- **Load testing before you need it.** Run load tests monthly with tools like k6 or Artillery. Know where things break before your users discover it for you.
- **Cost per user is the key metric.** Track infrastructure cost per active user. If this number increases with scale, your architecture has a problem. It should decrease or stay flat.
- **N+1 queries are the silent killer.** Most early performance problems come from ORM-generated N+1 queries, not from fundamental architecture issues. Profile before refactoring.
