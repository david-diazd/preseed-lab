---
name: landing-page
description: Cuando el founder necesita escribir el copy de su landing page. Activa con "landing page", "home page", "copy del sitio web", "página principal", "conversión del sitio".
domain: marketing
reads: [inputs/]
outputs: [outputs/landing-page.md]
---

# Landing Page Agent

## Cuándo usar
- El founder necesita escribir el copy de su landing page desde cero
- El founder quiere mejorar una landing page que no está convirtiendo
- El founder quiere asegurarse de que el mensaje de la landing conecta con el ICP

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto o pitch deck
- URL o screenshot de la landing actual (si existe)
- Testimonials o quotes de clientes
- Datos de conversión actuales si están disponibles

Si inputs/ está vacío, pregunta: "¿Qué hace tu producto, quién es tu cliente objetivo y cuál es el CTA principal de la landing (signup, demo, contacto)?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor diferencial, ICP y sus principales pain points, prueba social disponible (clientes, testimonials, métricas), y el CTA objetivo.

2. **Diagnosticar** — Evalúa si la landing actual (si existe) tiene: headline que captura el beneficio clave en <5 segundos, subheadline que añade contexto, prueba social creíble, CTA claro y repetido, y ausencia de jargon técnico que confunde al ICP.

3. **Producir output** — Escribe `outputs/landing-page.md` con el copy completo sección a sección, listo para implementar.

## Output Format

`outputs/landing-page.md`:

```
## Copy de Landing Page — [Empresa]

### Hero section
**Headline:** [Beneficio principal en <10 palabras]
**Subheadline:** [Contexto adicional en 1-2 frases]
**CTA principal:** [Texto del botón]
**CTA secundario (si aplica):** [Texto]

### Sección de problema
[Copy que hace que el visitante piense "eso me pasa a mí exactamente"]

### Sección de solución / producto
[Copy + descripción de 3-5 beneficios clave (no features)]

### Prueba social
[Testimonial 1: "[cita]" — Nombre, Cargo, Empresa]
[Métricas si las hay: "X empresas ya usan...", "Y% de mejora en Z"]

### Sección de features (si aplica)
[3 features con nombre, descripción breve y beneficio]

### FAQ (3-5 preguntas)
[Preguntas reales que tiene el ICP antes de convertir]

### CTA final
[Headline de cierre + CTA button]
```

## Frameworks & Best Practices

### Page-Specific CRO
- **Homepage:** Clear positioning for cold visitors, quick path to primary conversion, handle both "ready to buy" and "still researching" visitors.
- **Landing page:** Message-match with traffic source, single CTA (remove navigation if possible), complete argument on one page.
- **Pricing page:** Clear plan comparison, recommended plan indication, address "which plan is right for me?" anxiety.
- **Feature page:** Connect feature to benefit, include use cases and examples, clear path to try/buy.
- **Blog post:** Contextual CTAs matching content topic, inline CTAs at natural stopping points.

### Copy Principles
- **The headline is the most important element on the page.** If the headline does not stop the scroll, nothing else matters. Test headlines before anything else.
- **Specificity beats cleverness.** "Save 12 hours per week on reporting" outperforms "Work smarter, not harder" every time.
- **The subheadline does the heavy lifting.** The headline earns attention; the subheadline explains the value. Use it to clarify who the product is for, what it does, and why it matters.
- **Awareness-level matching.** Match copy depth to visitor awareness. Paid search visitors are typically solution-aware (want pricing and CTAs). Social ad visitors are typically problem-aware or unaware (need problem education first). Traffic source reveals awareness level.

### Conversion Principles
- **One page, one goal.** Never give the visitor two equal choices. Every element should push toward the primary CTA.
- **Above-the-fold rule.** Visitor should understand what you do, who it is for, and what to do next within 5 seconds.
- **Risk reversal near final CTA.** Address "what if it doesn't work?" -- free trial, money-back guarantee, or no-commitment language.
- **Social proof placement.** Small proof element in hero section ("Trusted by 500+ teams"), dedicated proof section below the fold.
- **Testimonial specificity.** "This product is great" is worthless. "We reduced onboarding time from 3 weeks to 2 days" is persuasive. Seek specific, outcome-driven testimonials with numbers.
- **Reduce cognitive load.** Every additional choice, link, or piece of information adds friction. Cut anything that does not directly support the primary conversion.
- **Mobile-first.** Over 60% of traffic is mobile. Design for thumb zones. Ensure CTAs are tappable without zooming.

## Related Skills
- `content-strategy` -- when the landing page needs supporting content to drive traffic
- `cold-outreach` -- when the landing page is the destination for outbound campaigns and copy must align with email messaging

## Examples

**Example 1: Page audit**
> "Here's our landing page copy. We're getting 15k visitors/month but only 1.2% conversion. What's wrong?"

Good output: Quick wins (e.g., rewrite feature-focused headline to outcome-focused), high-impact changes (restructure page sections, add social proof to hero), and test ideas (3 headline variants, 2 CTA copy options). Each recommendation includes the specific issue, the fix, and expected impact.

**Example 2: New page draft**
> "We're launching a waitlist page for our developer tool. Target audience is backend engineers frustrated with deployment complexity."

Good output: Full section-by-section copy. Hero headline: "Deploy to production in 3 commands, not 30 steps." Problem agitation naming the specific pain. 3-step "how it works" section. Social proof placeholder guidance. CTA: "Join 2,400 engineers on the waitlist." Two alternative headline options and layout notes.

**Example 3: A/B test recommendations**
> "Our signup page converts at 3.5%. What should we test first?"

Good output: Priority-ordered test plan. (1) Headline -- 3 variants reframing value prop from feature-first to outcome-first. (2) CTA copy -- "Start free trial" vs. "See it in action" vs. "Get started in 2 minutes." (3) Hero trust element -- customer count or logo bar. Each test includes control, variant, hypothesis, and minimum sample size guidance.
