---
name: cold-outreach
description: Cuando el founder necesita escribir emails de cold outreach para ventas B2B. Activa con "cold email", "prospección", "outreach a clientes", "secuencia de emails", "ventas outbound".
domain: marketing
reads: [inputs/]
outputs: [outputs/cold-outreach.md]
---

# Cold Outreach Agent

## Cuándo usar
- El founder necesita escribir emails de prospección para conseguir sus primeros clientes
- El founder quiere construir una secuencia de follow-ups automatizable
- El founder quiere personalizar outreach para un segmento específico de clientes

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto y propuesta de valor
- ICP o perfil del cliente objetivo
- Lista de prospects (si existe — nombre, empresa, cargo)
- Emails previos enviados (para mejorar el tono y los resultados)

Si inputs/ está vacío, pregunta: "¿A qué tipo de empresa y cargo va dirigido el outreach? ¿Qué problema específico les resuelves?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor diferencial para este segmento específico, pain point principal del ICP, prueba social disponible (clientes similares, métricas), y cualquier hook de personalización posible.

2. **Diagnosticar** — Evalúa si los emails existentes son demasiado largos, demasiado centrados en el producto en vez del problema del cliente, o carecen de CTA específico.

3. **Producir output** — Escribe `outputs/cold-outreach.md` con una secuencia de 3-4 emails (primer contacto + follow-ups), con subject lines y variantes de personalización.

## Output Format

`outputs/cold-outreach.md`:

```
## Secuencia de cold outreach — [Segmento objetivo]

### Email 1 — Día 0
**Asunto:** [Subject line — específico, no genérico]
**Cuerpo:**
[Email completo — máx 150 palabras]

### Email 2 — Día 3 (si no responde)
**Asunto:** Re: [Asunto anterior]
[Follow-up breve añadiendo un ángulo diferente]

### Email 3 — Día 7 (si no responde)
[Breakup email — cierre amigable que deja la puerta abierta]

### Variantes de personalización
[Cómo cambiar el email si el prospect es: startup / empresa grande / sector específico]

### A/B de subject lines para testear
1. [Opción A]
2. [Opción B]
```

## Frameworks & Best Practices

### The Core Principle
The word "cold" is the problem. Every message should feel like it comes from someone who understands the prospect's world. Research is what makes that possible.

### Message Structure
- **Connection request (LinkedIn):** Max 300 characters. Reference something specific. Never pitch in the request.
- **First message (24-48 hours after connection):** "Thanks for connecting" + bridge to a research signal + value statement + question. Keep it conversational.
- **Follow-up 1 (Day 7):** Introduce a new angle — different problem, proof point, or insight.
- **Follow-up 2 (Day 14):** Share something valuable (article, data, framework) with a soft reconnect.
- **Break-up (Day 21):** Professional close — "Closing the loop. If timing is ever right, I'm here."

### Writing Principles
- **Write like a peer, not a vendor.** Use contractions. If it sounds like marketing copy, rewrite it.
- **Every sentence must earn its place.** If it does not move toward a reply, cut it.
- **Lead with their world, not yours.** "You/your" should dominate over "I/we."
- **One ask, low friction.** Interest-based CTAs ("Worth exploring?") beat meeting requests.
- **Every message must reference a specific research signal** or explicitly default to Tier 3. This is a hard rule.

### Email Frameworks
- **Observation-Problem-Proof-Ask** — You noticed X, which usually means Y challenge. We helped Z with that. Interested?
- **Trigger-Insight-Ask** — Congrats on X. That usually creates Y challenge. We have helped similar companies. Curious?
- **Story-Bridge-Ask** — [Similar company] had [problem]. They [solved it this way]. Relevant to you?

### Subject Lines
- 2-4 words, lowercase, no punctuation tricks
- Should look like an internal email ("quick question," "re: [their company]")
- No product pitches, no urgency, no emojis

### What to Avoid
- Opening with "I hope this finds you well" or "My name is X and I work at Y"
- Jargon: "synergy," "leverage," "best-in-class," "leading provider"
- Feature dumps — one proof point beats ten features
- HTML formatting, images, or multiple links in cold emails
- Fake "Re:" or "Fwd:" subject lines
- Asking for 30-minute calls in first touch
- Sending identical templates with only the name swapped
- Pitching in a LinkedIn connection request

### Founder-Specific Advantages
- Founder-to-founder or founder-to-exec emails get 2-3x higher reply rates
- Lead with "I built this because..." — more compelling than "our company offers..."
- Offer what reps cannot: personal onboarding, product roadmap input, advisory relationships

### Personalization Tiers
- **Tier 1 (custom):** Named signals across multiple research sources — fully personalized message
- **Tier 2 (templated + personalized):** Company info and role context — template with personalized elements
- **Tier 3 (volume template):** No signals found — use volume approach with strong value prop

### Research Signals (ranked by strength)
- **Tier 1 (strongest):** Recent news — funding rounds, product launches, key hires
- **Tier 2:** LinkedIn activity — posts, comments, job changes
- **Tier 3:** Company growth signals — hiring trends, tech stack changes
- **Tier 4 (weakest):** Role/industry awareness only

## Examples

**Good email (Tier 2):**
> Subject: api alerts
>
> Hi [Name],
>
> Saw your team just shipped the new payments integration — nice work. Launches like that usually surface a wave of edge-case API failures that are tough to catch with standard monitoring.
>
> We built a tool that catches those failures before customers notice. Acme Corp cut their API downtime by 73% in the first month.
>
> Worth a quick look?

**Good LinkedIn connection request:**
> Hi [Name] — saw the payments launch. We help engineering teams catch API failures before customers do. Would love to connect.

**Follow-up (Day 7, new angle):**
> Hi [Name], quick thought — after launches like yours, the #1 issue teams tell us about isn't downtime, it's the silent failures that slip through alerts. Happy to share what patterns we see across 50+ engineering teams if useful.
