---
name: lead-research
description: Cuando el founder necesita encontrar leads B2B cualificados con LinkedIn, email y señales de intención. Activa con "encontrar leads", "lead gen", "prospección", "lista de prospectos", "ICP en LinkedIn", "buscar decisores", "leads cualificados", "outbound leads".
domain: growth
reads: [inputs/]
outputs: [outputs/lead-research.md]
web_search: true
---

# Lead Research Agent

## Cuándo usar
- El founder necesita una lista de prospectos B2B para empezar outbound
- El founder tiene un ICP definido y quiere encontrar decisores que encajen
- El founder quiere activar campañas de cold email o LinkedIn y necesita volumen con calidad
- El founder está validando si un segmento tiene suficiente densidad de cuentas target

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto y propuesta de valor
- ICP definido (industria, tamaño de empresa, geografía, cargo del decisor)
- Lista previa de clientes o cuentas target
- Pitch deck (para extraer a quién vende realmente)
- Outputs previos de cold-outreach o market-research (para encadenar)

Si inputs/ está vacío, pregunta:
1. "¿A qué tipo de empresa vendes (sector, tamaño, geografía)?"
2. "¿Qué cargo del decisor quieres encontrar (CEO, Head of Sales, CTO, etc.)?"
3. "¿Cuántos leads quieres en la lista (10, 50, 100)?"
4. "¿Tienes alguna señal de intención específica que te interese (acaban de levantar ronda, están contratando, acaban de lanzar producto)?"

## Workflow

1. **Leer inputs/** — Extrae: producto, propuesta de valor, ICP (industria + tamaño + geografía), cargo target, señales de intención deseadas, y volumen solicitado. Si el ICP es vago, refínalo con el founder antes de buscar.

2. **Definir queries de búsqueda** — Construye 3-5 queries de web search combinando:
   - Cargo + industria (ej: "Head of Sales fintech Spain LinkedIn")
   - Señal de intención + cargo (ej: "CTO hired recently SaaS 2026")
   - Empresa objetivo + decisor (ej: "[empresa] VP Engineering LinkedIn")
   - Listas curadas: "[cargo] [industria] site:linkedin.com/in"
   - Directorios y herramientas: Apollo, RocketReach, Crunchbase, BuiltWith, job boards

3. **Buscar y enriquecer** — Por cada lead candidato, captura:
   - Nombre completo
   - Cargo actual (verificado en LinkedIn o web oficial)
   - Empresa (verificar que encaje con ICP)
   - LinkedIn URL
   - Email (inferido por patrón corporativo: firstname@empresa.com, firstname.lastname@empresa.com, f.lastname@empresa.com, etc.)
   - Fuente de la que se obtuvo
   - Señal de personalización (algo reciente que permita hook de outreach)

4. **Producir output** — Escribe `outputs/lead-research.md` con tabla de leads, score de cualificación, fuentes utilizadas y gaps de cobertura.

## Output Format

`outputs/lead-research.md`:

```
## Lista de leads — [ICP] — [Fecha]

### Resumen de búsqueda
- Total leads encontrados: [N]
- Empresas únicas cubiertas: [N]
- Tasa de emails con alta confianza: [%]
- Señales de intención detectadas: [N leads]
- Fuentes principales: [LinkedIn, Apollo, web oficial, etc.]

### Tabla de leads (ordenados por score)

| # | Nombre | Cargo | Empresa | LinkedIn | Email (confianza) | Señal | Score |
|---|--------|-------|---------|----------|-------------------|-------|-------|
| 1 | María García | VP Sales | Acme Corp | linkedin.com/in/mariagarcia | maria.garcia@acme.com (alta) | Acaban de anunciar ronda de €5M | 95 |
| 2 | ... |

### Score breakdown
- **A (90-100)**: Match exacto de ICP + señal de intención reciente + email alta confianza
- **B (75-89)**: Match de ICP + email verificado o cargo senior
- **C (60-74)**: Match parcial de ICP o email inferido sin verificar
- **D (<60)**: Match débil, requiere validación manual

### Patrones de email identificados
- [firstname].[lastname]@empresa.com (45%)
- [firstname]@empresa.com (30%)
- f.[lastname]@empresa.com (15%)
- Otros (10%)

### Señales de intención más frecuentes detectadas
1. [Hiring spree en X cargo] — N leads
2. [Ronda reciente] — N leads
3. [Lanzamiento de producto] — N leads
4. [Expansión geográfica] — N leads

### Gaps de cobertura
- [Industrias donde no encontré leads suficientes]
- [Geografías con baja cobertura]
- [Cargos que requieren búsqueda más profunda]

### Próximos pasos recomendados
- Encadenar con `cold-outreach` para redactar secuencia de emails
- Validar emails con herramienta dedicada antes de enviar (Hunter, NeverBounce, Apollo)
- Priorizar Tier A en primera oleada, Tier B en segunda
```

## Frameworks & Best Practices

### Definición de ICP antes de buscar

Nunca busques sin ICP definido. Si el founder dice "cualquier SaaS B2B", el resultado será ruido. Refina con:
- **Industria vertical** (no solo "tech" — fintech, healthtech, edtech, martech, etc.)
- **Tamaño de empresa** por empleados o revenue (10-50, 50-200, 200-1000, 1000+)
- **Geografía** (España, Europa, LATAM, global)
- **Stage de la empresa** (seed, series A, growth, established)
- **Cargo del decisor** (poder de compra real, no solo "manager")

### Señales de intención (ranked by strength)

1. **Tier 1 (recientes, <30 días)**:
   - Funding round anunciada
   - Hiring spree en el cargo o departamento target
   - Lanzamiento de producto o feature
   - Expansión geográfica
   - M&A o partnership anunciado

2. **Tier 2 (30-90 días)**:
   - Cargos nuevos asumidos
   - Contenido publicado sobre el problema que resuelves
   - Cambios de stack tecnológico
   - Aparición en prensa sectorial

3. **Tier 3 (90+ días o weaker)**:
   - Tamaño de empresa encaja
   - Industria encaja
   - Cargo encaja sin señal adicional

### Patrones de email corporativo

Antes de inventar emails, **verifica el patrón en la web**:
- Busca "[empresa] email format" o "[empresa] contact"
- Revisa páginas de equipo en su web
- Usa Apollo, Hunter.io, RocketReach como referencia cruzada
- Si no hay patrón claro, prueba los 2-3 más comunes del sector

**Patrones por probabilidad (B2B típico)**:
- `firstname@empresa.com` — startups pequeñas, equipos <50
- `firstname.lastname@empresa.com` — empresa mediana-grande
- `f.lastname@empresa.com` — corporativo clásico
- `firstnamel@empresa.com` (first initial + lastname) — tech moderno

**Si el dominio no es guessable**:
- Marca como "email no disponible" en la tabla
- Sugiere LinkedIn InMail o manual lookup como alternativa

### Fuentes de búsqueda (en orden de eficiencia)

1. **LinkedIn público** (`site:linkedin.com/in` + cargo + empresa) — más fiable para nombre + cargo
2. **Web oficial de la empresa** — equipo, about us, blog de autores
3. **Crunchbase / PitchBook** — para empresas y funding signals
4. **Apollo.io / Hunter.io / RocketReach** — cuando estén en results de búsqueda
5. **Job boards** (LinkedIn Jobs, Indeed, InfoJobs) — señales de hiring
6. **Twitter/X bios** — para validar cargo y encontrar emails personales (a veces)
7. **Press releases** — para funding, M&A, launches
8. **GitHub / Stack Overflow** — para leads técnicos
9. **Podcast appearances** — para leads con autoridad sectorial

### Límites éticos y legales

- **No scrapees LinkedIn con herramientas prohibidas** (viola ToS). Usa solo datos públicos.
- **No compres listas de email masivas** (bajas tasas, alto spam risk, GDPR concern).
- **Aplica GDPR/CAN-SPAM siempre**: opt-out claro, datos precisos, base legal documentada.
- **Verifica emails antes de enviar**: nunca envíes a emails no verificados (bounce daña tu sender reputation).
- **No inventes cargos ni empresas**: si no lo verificas, márcalo como "a verificar".

### Cuándo NO usar este agente

- El founder todavía no tiene ICP definido → usar primero `market-research` o `customer-discovery`
- El fundador quiere leads para inversores, no clientes → usar `investor-research`
- El founder quiere emails para una lista que ya tiene, solo enriquecer → este agente puede hacerlo, pero el workflow es más rápido con herramientas dedicadas
- El volumen pedido es >200 leads con email verificado → este agente da lista curada, no base de datos masiva (para eso: Apollo, ZoomInfo, Lusha, Cognism)

### Encadenamiento con otros agentes

Este agente es **input natural** para:
- `cold-outreach` — toma la tabla de leads y redacta emails personalizados por lead
- `sales-script` — para llamadas en frío sobre los mismos leads
- `partnership-strategy` — para identificar partners potenciales
- `fundraising-email` — si el "lead" es un inversor (cross-use)

Related Skills:
- `skills/competitor-monitor.md` — para monitorizar empresas target y detectar señales
- `CMO/skills/performance-report.md` — para medir conversión de la lista generada
