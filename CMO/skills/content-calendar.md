---
name: content-calendar
description: Genera calendario de contenido mensual multi-canal. Activa con "calendario de contenido", "content calendar", "qué publicar", "plan de contenido", "editorial calendar".
type: skill
scope: CMO
chains: [CMO/agents/marketing/content-strategy, CMO/agents/marketing/social-content]
reads: [inputs/]
outputs: [outputs/content-calendar.md]
---

# Content Calendar Skill

## Cuándo usar
- Al inicio del mes para planificar el contenido
- Cuando el founder no sabe qué publicar
- Para mantener consistencia en la publicación de contenido

## Qué leer en inputs/
- Estrategia de contenido existente
- Posts anteriores con buen rendimiento
- Calendario de eventos del sector
- Lanzamientos o hitos próximos de la startup

Si inputs/ está vacío, pregunta: "¿En qué canales publicas (LinkedIn, Twitter, blog, newsletter), con qué frecuencia, y cuáles son tus pilares de contenido?"

## Output Format

```
# Content Calendar — [Mes Año]

## Pilares de contenido
| Pilar | % del mix | Ejemplo de tema |
|---|---|---|

## Calendario semanal

### Semana 1 ([Fechas])
| Día | Canal | Tipo | Tema | Hook | CTA | Status |
|---|---|---|---|---|---|---|

### Semana 2 ([Fechas])
...

### Semana 3 ([Fechas])
...

### Semana 4 ([Fechas])
...

## Contenido largo (blog/newsletter)
| Título | Keyword target | Fecha publicación | Distribución |
|---|---|---|---|

## Fechas clave del mes
| Fecha | Evento | Contenido planificado |
|---|---|---|

## Métricas del mes anterior
| Canal | Seguidores | Engagement rate | Mejor post | Peor post |
|---|---|---|---|---|

## Reutilización de contenido
| Contenido original | Derivados |
|---|---|
| [Blog post X] | → Thread Twitter, → Carrusel LinkedIn, → Newsletter |
```
