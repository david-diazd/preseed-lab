---
name: seo-technical
description: Cuando el founder quiere que su web aparezca en búsquedas relevantes. Activa con "SEO", "posicionamiento web", "keywords", "tráfico orgánico", "aparecer en Google".
domain: marketing
reads: [inputs/]
outputs: [outputs/seo-plan.md]
---

# SEO Technical Agent

## Cuándo usar
- El founder quiere generar tráfico orgánico pero no sabe por dónde empezar
- El founder quiere auditar el SEO de su web actual
- El founder quiere construir un plan de keywords relevante para su ICP

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- URL o descripción del sitio web
- Descripción del producto y el ICP
- Analytics del sitio si están disponibles (tráfico, bounce rate, páginas)
- Lista de competidores conocidos

Si inputs/ está vacío, pregunta: "¿Cuál es la URL de tu web y a qué busca tu cliente cuando tiene el problema que tú resuelves?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor, ICP, competidores, y cualquier dato de rendimiento SEO existente.

2. **Diagnosticar** — Evalúa el estado SEO actual: ¿hay keyword targeting? ¿Las páginas tienen meta titles y descriptions optimizadas? ¿Hay contenido que pueda rankear? ¿Hay problemas técnicos obvios?

3. **Producir output** — Escribe `outputs/seo-plan.md` con la estrategia de keywords, auditoría de páginas clave y plan de acción priorizado.

## Output Format

`outputs/seo-plan.md`:

```
## Plan SEO — [Empresa]

### Keywords objetivo
| Keyword | Intención | Dificultad estimada | Prioridad |
|---|---|---|---|
| [keyword primaria] | Informacional/Transaccional | Alta/Media/Baja | 1 |

### Auditoría de páginas clave
| Página | Meta title actual | Meta title sugerido | Issues |
|---|---|---|---|

### Acciones priorizadas
1. [Acción técnica — ej: añadir meta descriptions a todas las páginas]
2. [Acción de contenido — ej: crear página de comparación vs competidor X]
3. ...

### Calendario de contenido SEO (3 meses)
[Artículos/páginas a crear con keyword objetivo y brief]
```

## Frameworks & Best Practices

- **Canonical tags are directives, not suggestions**: While Google treats them as hints, properly implemented canonicals are followed in the vast majority of cases. Always self-canonical pages and canonical duplicates to the preferred version.
- **JavaScript SEO**: Critical metadata (canonical, robots, structured data) must be in initial server-rendered HTML. Google can render JS but with delays and reliability gaps.
- **Mobile-first is complete**: Since July 2024, there is no "desktop index." The mobile version IS the version Google indexes. Full content parity is non-negotiable.
- **INP replaced FID**: FID was fully removed from Chrome tools by September 2024. All performance optimization should target INP (under 200ms), not FID.
- **Crawl budget**: Rarely an issue for sites under 10,000 pages. For larger sites, prioritize by removing low-value pages and fixing redirect chains.
- **Hreflang for international sites**: Implement correctly or not at all. Errors cause worse indexation than no hreflang tags.
- **Log file analysis**: Server logs reveal what Googlebot actually crawls vs. what you want crawled. This is the ground truth of crawlability.
- **Speed is a tiebreaker**: Rarely causes dramatic ranking changes alone, but affects user behavior metrics (bounce rate, time on site) which indirectly impact rankings.
- **E-E-A-T signals matter**: Author bios with credentials, about page, contact info, links to authoritative sources, HTTPS, privacy policy, terms of service.

### Audit Workflow (9 dimensions, 100-point scale)

1. **Crawlability audit** — Foundation; nothing else matters if search engines cannot crawl the site.
   - Check robots.txt for unintended disallow rules.
   - Verify XML sitemap exists, is submitted to Search Console, and is up to date.
   - Identify crawl errors (4xx, 5xx status codes).
   - Check for orphan pages (no internal links pointing to them).
   - Audit redirect chains — flatten to single hops. Chains of 3+ waste crawl budget and dilute link equity.
   - For sites with 10,000+ pages, analyze crawl budget efficiency and remove low-value pages from the index.
2. **Indexation audit** — Ensure crawled pages are actually indexed.
   - Check `site:domain.com` results vs. expected page count.
   - Look for `noindex` tags applied unintentionally.
   - Identify duplicate content issues and missing canonical tags.
   - Check for thin content pages that may be filtered out.
   - Review index coverage report in Search Console for excluded pages.
3. **Security and HTTPS** — HTTPS is a ranking signal and a trust requirement.
   - Verify HTTPS everywhere with proper redirects from HTTP.
   - Check for mixed content issues.
   - Validate SSL certificate and HSTS headers.
4. **URL structure** — Short, descriptive, hyphenated URLs without parameters.
   - Consistent URL patterns across the site.
   - No duplicate content from URL variations (trailing slashes, www vs. non-www).
   - Self-referencing canonical tags on every page.
5. **Mobile optimization** — As of July 2024, Google crawls and indexes ALL websites exclusively with the mobile Googlebot user-agent. Mobile-first is not optional.
   - Mobile and desktop content parity is mandatory.
   - Test with mobile-friendly tools.
   - Responsive design, no horizontal scroll, touch targets properly sized.
6. **Core Web Vitals** — Google uses these as ranking signals. Current targets:
   - **LCP (Largest Contentful Paint):** Target under 2.5 seconds. Fixes: optimize hero images, implement lazy loading, use CDN, reduce server response time.
   - **INP (Interaction to Next Paint):** Target under 200ms. INP replaced FID in March 2024. Fixes: reduce JavaScript execution time, break up long tasks, optimize event handlers.
   - **CLS (Cumulative Layout Shift):** Target under 0.1. Fixes: set explicit dimensions on images/embeds, avoid injecting content above existing content, use `font-display: swap`.
   - Check for render-blocking CSS/JS, unoptimized images, excessive third-party scripts.
7. **Structured data** — Implement schema markup for rich results.
   - Organization schema on the homepage.
   - Article/BlogPosting schema on content pages.
   - Product schema on product pages.
   - FAQ schema where applicable (boosts SERP real estate).
   - BreadcrumbList schema for navigation clarity.
   - Validate with Google's Rich Results Test.
8. **JavaScript rendering** — Critical for SPAs and JS-heavy sites.
   - Serve canonical tags, robots directives, and structured data in initial server-rendered HTML. Google may not reliably process these if injected via JavaScript.
   - Verify server-side rendering or pre-rendering is in place for critical content.
   - Test what Googlebot actually sees vs. what users see.
9. **AI crawler management** — Managing AI crawlers via robots.txt is a critical 2025-2026 consideration.
   - **GPTBot** (OpenAI), **ClaudeBot** (Anthropic), **PerplexityBot**, **Bytespider** (ByteDance), **Google-Extended**
   - Blocking Google-Extended does NOT affect Google Search indexing or AI Overviews — only Gemini training data.
   - Decide per-crawler based on business needs: allow, block, or rate-limit.

### Priority Tiers for Audit Reports
- **Critical issues** (blocking indexation or causing major ranking loss): fix immediately
- **High-impact improvements** (will meaningfully improve rankings): fix within 2 weeks
- **Medium improvements** (incremental gains): fix within 30 days
- **Low priority** (minor optimizations): address when convenient

Each item includes: the issue, why it matters for rankings, how to fix it, and estimated effort (low/medium/high).

## Related Skills
- `content-strategy` — when the audit reveals content gaps or thin content that needs a broader content plan
- `landing-page` — when key landing pages need both CRO and on-page SEO optimization
