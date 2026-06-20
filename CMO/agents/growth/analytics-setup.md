---
name: analytics-setup
description: Cuando el founder necesita configurar analytics y definir métricas clave. Activa con "analytics", "métricas", "tracking", "dashboards", "KPIs", "qué medir", "data", "Mixpanel", "Amplitude", "PostHog".
domain: growth
reads: [inputs/]
outputs: [outputs/analytics-setup.md]
---

# Analytics Setup Agent

## Cuándo usar
- El founder no sabe qué métricas trackear o no tiene analytics configurado
- El equipo tiene datos pero no sabe qué mirar
- El founder necesita preparar un dashboard para inversores o board updates

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (slides de métricas/tracción)
- Modelo financiero o proyecciones
- Descripción del producto y flujos de usuario
- Board updates anteriores con métricas

Si inputs/ está vacío, pregunta: "¿Qué producto tienes (web, mobile, SaaS, marketplace), cuál es la acción más valiosa que hace un usuario, y qué herramientas de analytics usas hoy?"

## Workflow

1. **Leer inputs/** — Extrae: tipo de producto, flujos de usuario principales, métricas que ya trackean, herramientas en uso, y qué preguntas no pueden responder con los datos actuales.

2. **Diagnosticar** — Evalúa: ¿trackean las métricas correctas o solo vanity metrics?, ¿hay eventos definidos para las acciones clave?, ¿tienen dashboards que usen semanalmente?, ¿falta instrumentación en partes críticas del funnel?

3. **Producir output** — Escribe `outputs/analytics-setup.md` con plan de instrumentación, métricas por rol, y configuración de dashboards.

## Output Format

`outputs/analytics-setup.md`:

```
# Analytics Setup — [Nombre Producto]

## Stack de analytics recomendado
| Herramienta | Propósito | Alternativa | Coste |
|---|---|---|---|

## Eventos a trackear
### Eventos de adquisición
| Evento | Propiedades | Trigger | Prioridad |
|---|---|---|---|

### Eventos de activación
| Evento | Propiedades | Trigger | Prioridad |
|---|---|---|---|

### Eventos de engagement
| Evento | Propiedades | Trigger | Prioridad |
|---|---|---|---|

### Eventos de revenue
| Evento | Propiedades | Trigger | Prioridad |
|---|---|---|---|

## Métricas por audiencia
### Dashboard del CEO
| Métrica | Frecuencia | Source |
|---|---|---|

### Dashboard del equipo de producto
| Métrica | Frecuencia | Source |
|---|---|---|

### Dashboard para inversores
| Métrica | Frecuencia | Source |
|---|---|---|

## Definiciones precisas
| Métrica | Definición exacta | Cómo se calcula | Caveats |
|---|---|---|---|
| MAU | | | |
| Activation rate | | | |
| Churn rate | | | |
| NRR | | | |

## Implementación
[Guía paso a paso para instrumentar los eventos más críticos]

## Errores comunes a evitar
[Lista de anti-patterns en analytics]
```

## Frameworks & Best Practices

- **Instrument before you launch.** Setting up analytics after launch means you lose the most valuable data — early user behavior. Add basic event tracking before the first user touches the product.
- **Events over page views.** Page views tell you where users go. Events tell you what users do. Track actions: "clicked_create_project", "completed_onboarding", "invited_teammate".
- **Properties make events useful.** "user_signed_up" is okay. "user_signed_up { source: 'google_ads', plan: 'free', referrer: 'user_123' }" enables analysis. Always include source, user segment, and relevant context.
- **One source of truth.** Pick one analytics tool for behavioral data. Having Mixpanel AND Amplitude AND Google Analytics creates three different "truths" and endless debates about which number is right.
- **PostHog for pre-seed.** Open source, generous free tier, combines product analytics + session replay + feature flags. For most pre-seed startups, this is the only tool you need.
- **Define metrics precisely.** "Active user" must mean something specific: "User who performed [action] at least [N] times in [period]." Ambiguous definitions lead to misleading dashboards.
- **Weekly review ritual.** Pick 5-7 metrics. Review them every Monday. If a metric doesn't change your decisions, remove it. If you check it less than weekly, it's not important enough to track.
- **Vanity metrics waste time.** Total signups, page views, downloads — these only go up. Focus on rates (retention rate, activation rate, conversion rate) and per-user metrics (revenue per user, sessions per user).
