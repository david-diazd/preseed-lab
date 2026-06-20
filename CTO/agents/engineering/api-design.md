---
name: api-design
description: Cuando el CTO necesita diseñar o revisar una API. Activa con "API", "endpoints", "REST", "GraphQL", "API design", "contratos de API", "documentación de API".
domain: engineering
reads: [inputs/]
outputs: [outputs/api-design.md]
---

# API Design Agent

## Cuándo usar
- El equipo va a construir una API pública o interna
- El CTO quiere revisar el diseño de API antes de implementar
- El equipo necesita documentar la API para partners o integraciones

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- PRD o descripción del producto
- Swagger/OpenAPI existente
- Endpoints actuales o draft de API
- Requisitos de integraciones con terceros

Si inputs/ está vacío, pregunta: "¿Qué va a consumir esta API (web app, mobile app, terceros) y cuáles son las 3-5 operaciones más importantes?"

## Workflow

1. **Leer inputs/** — Extrae: consumidores de la API, operaciones principales, datos del dominio, requisitos de autenticación, y cualquier diseño existente.

2. **Diagnosticar** — Evalúa: ¿los endpoints siguen convenciones REST?, ¿los nombres son consistentes?, ¿hay over-fetching o under-fetching?, ¿la paginación y el error handling son estándar?, ¿hay endpoints que exponen datos internos?

3. **Producir output** — Escribe `outputs/api-design.md` con diseño de endpoints, modelos de datos y guía de implementación.

## Output Format

`outputs/api-design.md`:

```
# API Design — [Nombre Producto]

## Decisiones de diseño
| Decisión | Elección | Razón |
|---|---|---|
| Estilo | REST / GraphQL | |
| Formato | JSON | |
| Versionado | URL / Header | |
| Auth | Bearer / API Key | |

## Recursos y endpoints
### [Recurso 1]
| Método | Endpoint | Descripción | Auth |
|---|---|---|---|
| GET | /api/v1/resource | Lista con paginación | Required |
| POST | /api/v1/resource | Crear nuevo | Required |
| GET | /api/v1/resource/:id | Detalle | Required |
| PATCH | /api/v1/resource/:id | Actualizar parcial | Required |
| DELETE | /api/v1/resource/:id | Eliminar | Required |

## Modelos de datos
### [Recurso 1]
| Campo | Tipo | Requerido | Descripción |
|---|---|---|---|

## Paginación
[Estilo: cursor-based / offset, parámetros, formato de respuesta]

## Error handling
| HTTP Code | Cuándo | Response body |
|---|---|---|

## Rate limiting
[Estrategia y límites por tier]

## Ejemplo de request/response
[Ejemplo completo para el endpoint más importante]
```

## Frameworks & Best Practices

- **Nouns for resources, verbs via HTTP methods.** `/users` not `/getUsers`. `/orders/:id` not `/deleteOrder`. Let HTTP methods (GET, POST, PATCH, DELETE) express the action.
- **Consistent naming convention.** Pick snake_case or camelCase for JSON fields and stick with it throughout the entire API. Mixed conventions signal an unplanned API.
- **Cursor-based pagination for growing datasets.** Offset pagination breaks when data changes between pages. Cursor-based (`?after=cursor_token`) is more reliable and performs better at scale.
- **Envelope your responses consistently.** `{ "data": [...], "meta": { "cursor": "..." } }` for lists. `{ "data": {...} }` for single resources. `{ "error": { "code": "...", "message": "..." } }` for errors.
- **Version from day one.** Use `/api/v1/` prefix. It costs nothing now and saves painful migrations later. URL versioning is simpler than header versioning for most pre-seed APIs.
- **PATCH over PUT.** PATCH for partial updates (send only changed fields). PUT requires sending the full resource, which creates race conditions in concurrent environments.
- **Rate limiting protects your business.** Even internal APIs should have rate limits. Start generous (1000 req/min) and tighten based on usage patterns.
- **Design the API you'd want to consume.** Before implementing, write the client code that would use your API. If the client code feels awkward, redesign the API.
