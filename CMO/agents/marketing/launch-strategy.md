---
name: launch-strategy
description: Cuando el founder se prepara para lanzar su producto o una feature importante. Activa con "lanzamiento", "launch", "Product Hunt", "cómo anunciar", "go-to-market", "estrategia de lanzamiento".
domain: marketing
reads: [inputs/]
outputs: [outputs/launch-strategy.md]
---

# Launch Strategy Agent

## Cuándo usar
- El founder está a semanas de lanzar su producto o una feature importante
- El founder quiere maximizar el impacto del lanzamiento con recursos limitados
- El founder quiere saber qué canales y tácticas usar en el lanzamiento

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto y propuesta de valor
- Lista de early adopters, waitlist o beta users
- Canales de distribución existentes (newsletter, redes, comunidades)
- Fecha objetivo de lanzamiento

Si inputs/ está vacío, pregunta: "¿Qué vas a lanzar, cuándo y a quién va dirigido principalmente?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor core, ICP, canales existentes, audiencia actual (tamaño de waitlist, seguidores, comunidades), y fecha de lanzamiento objetivo.

2. **Diagnosticar** — Evalúa qué tipo de lanzamiento tiene más sentido dado los recursos: Product Hunt, comunidades nicho, PR, outreach directo, o una combinación. Identifica si hay suficiente tracción previa para un lanzamiento público o si debe hacerse en fases.

3. **Producir output** — Escribe `outputs/launch-strategy.md` con el plan de lanzamiento semana a semana, tácticas por canal, copies clave y métricas de éxito.

## Output Format

`outputs/launch-strategy.md`:

```
## Plan de lanzamiento — [Producto] — [Fecha objetivo]

### Objetivo del lanzamiento
[Qué debe ser verdad en las 72h post-lanzamiento — métrica específica]

### Canales y tácticas
| Canal | Táctica | Responsable | Timing | KPI |
|---|---|---|---|---|

### Cronograma semana a semana
**T-4 semanas:** [acciones de preparación]
**T-2 semanas:** [acciones de calentamiento]
**T-1 semana:** [acciones de pre-lanzamiento]
**Día 0:** [acciones del día de lanzamiento]
**T+1 semana:** [follow-up y amplificación]

### Copies clave
- Headline del lanzamiento: [texto]
- Tagline de Product Hunt / HackerNews: [texto]
- Tweet/post de anuncio: [texto completo]

### Métricas de éxito
[KPIs a 24h, 72h y 1 semana]
```

## Frameworks & Best Practices

### The Sideways Sales Letter (Jeff Walker's Product Launch Formula)
Instead of one long sales letter, spread the sales message across 3-4 pieces of pre-launch content over 7-14 days. Each piece delivers value while building desire:

- **PLC 1: The Opportunity** — Why now? What is possible? Introduce the new opportunity or approach. Share proof and results. Open a loop teasing PLC 2.
- **PLC 2: The Transformation** — What will change when they embrace this? Deep dive with case studies, before/after results. Handle the "Is this for me?" objection. Tease PLC 3.
- **PLC 3: The Ownership Experience** — What is it like to have this solution? Walk through the product. Testimonials about the experience. Handle the "Can I do this?" objection. Tease the offer.
- **PLC 4: The Offer** — Full offer presentation with the value stack, bonuses, guarantee, and a clear call to action with urgency.

### Results in Advance (Frank Kern)
Give away your best material for free during pre-launch. When you deliver massive value before asking for the sale, you build reciprocity and prove competence. Do not hold back your best content out of fear — generosity in pre-launch drives sales at cart open.

### Launch Timeline Template

| Phase | Timing | Activities |
|-------|--------|------------|
| Pre-Pre-Launch | 4-6 weeks before | Seed the idea, build launch list, survey audience |
| PLC 1 | 10-14 days before | Release Opportunity content |
| PLC 2 | 7-10 days before | Release Transformation content |
| PLC 3 | 4-7 days before | Release Ownership content |
| PLC 4 / Cart Open | Launch day | Release Offer, open cart |
| Cart Open | Days 1-3 | Daily emails, testimonials, FAQ |
| Final Push | Days 4-5 | Multiple daily emails, urgency, countdown |
| Cart Close | Days 5-7 | Final call emails, cart closes (for real) |
| Post-Launch | Days 8-14 | Thank buyers, follow up non-buyers, debrief |

### S-Tier Launch Tactics (Must-Do)
1. **Create 3-4 pieces of pre-launch content.** Do not just announce the product. Build desire over 7-14 days.
2. **Build a launch list before launching.** A dedicated opt-in identifies your hottest leads.
3. **Create real scarcity.** Use a genuine cart close date. When it closes, it closes. Fake deadlines destroy trust permanently.
4. **Stack your offer.** Present bonuses that eliminate objections. Total perceived value should be 10x+ price.
5. **Send multiple emails during cart open.** Send 2-3 emails per day during the final 48 hours. Most sales happen in the last 24 hours.
6. **Do a seed launch first.** For new products, launch to a small group to get testimonials and refine the offer before going big.

### A-Tier Launch Tactics (Highly Effective)
1. **Recruit JV partners** with audiences matching your ideal customer. Provide swipe files and leaderboard prizes.
2. **Create a launch event** (webinar, challenge, live series) to build engagement during pre-launch.
3. **Implement behavioral triggers.** Track who watches PLCs, clicks, and visits the sales page. Send different follow-up based on behavior.
4. **Use countdown timers** on the sales page and in emails for visual urgency.
5. **Plan your post-launch sequence.** Non-buyers from this launch are warm leads for the next one.

### Common Mistakes to Avoid
- **Launching without pre-launch content** — Announcing a product without building anticipation leads to weak sales.
- **Fake scarcity** — Extending a deadline after saying it is final destroys trust.
- **Only emailing once during launch** — You need multiple touchpoints. Under-emailing is the most common launch mistake.
- **Skipping the seed launch** — Launching an unvalidated product to a big list is high risk.
- **No post-launch follow-up** — Non-buyers are warm leads. Stay in touch.

## Related Skills
- `content-strategy` — When the launch needs supporting content to sustain post-launch momentum
- `social-content` — When launch messaging needs to be adapted for social platforms
- `email-marketing` — When the launch relies on email sequences for waitlist nurture and follow-up
- `landing-page` — When the launch requires a dedicated sales page optimized for conversion

## Examples

**Example 1: Online course launch**
> "I have a 5,000-person email list and a new course on data analytics. Help me plan the launch."

Good output: Recommend an internal launch with full PLC sequence. PLC 1 (10 days before): video on "The 3 Myths Holding Back Your Data Career." PLC 2 (7 days before): case study of a student who achieved a specific result. PLC 3 (4 days before): walkthrough of the course modules and ownership experience. Cart open for 5 days with a fast-action bonus (first 48 hours get a live Q&A session). Email sequence: 2 emails per PLC release, daily emails during cart open, 3 emails on cart close day. Target: $100-150K launch based on list size and typical conversion rates.

**Example 2: SaaS product with seed launch**
> "We have a new SaaS tool and only 200 beta users. Should we do a big launch or start small?"

Good output: Recommend a seed launch first — offer the product to 50-100 beta users at founding member pricing to validate demand, collect testimonials, and refine the offer. Use their feedback to build PLC content for the internal launch 6-8 weeks later. Only consider a JV launch after the internal launch proves the funnel converts.
