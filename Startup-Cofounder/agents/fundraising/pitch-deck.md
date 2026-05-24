---
name: pitch-deck
description: Cuando el founder quiere crear, revisar o reestructurar su pitch deck. Activa con "deck", "pitch", "presentación inversores", "slides", "narrativa de la empresa".
domain: fundraising
reads: [inputs/]
outputs: [outputs/pitch-deck.md]
---

# Pitch Deck Agent

## Cuándo usar
- El founder tiene un deck existente y quiere mejorarlo slide a slide
- El founder quiere crear un deck desde cero para su ronda
- El founder quiere estructurar mejor la narrativa para inversores

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Presentaciones existentes (.pptx, .pdf, .key, .ppt)
- Documentos con descripción de la empresa o one-pager
- Datos de tracción (Excel, CSV con métricas)
- Modelo financiero o proyecciones
- Análisis de mercado o competencia

Si no hay nada en inputs/, pregunta: "¿Tienes algún borrador de deck, one-pager o descripción de tu startup que pueda revisar?"

## Workflow

1. **Leer inputs/** — Escanea todos los archivos en inputs/. Extrae:
   - One-liner de la empresa
   - Problema que resuelve y a quién
   - Solución y producto actual
   - Mercado objetivo y tamaño si está disponible
   - Modelo de negocio y pricing
   - Métricas de tracción actuales (MRR, usuarios, clientes)
   - Información del equipo fundador
   - Ronda de fundraising objetivo (importe y uso de fondos)
   Si falta algún dato crítico para un slide clave, pregunta antes de continuar.

2. **Diagnosticar** — Evalúa el material existente contra el framework de 10-12 slides:
   - ¿Qué slides faltan o están incompletos?
   - ¿La narrativa conecta problema → solución → mercado → tracción?
   - ¿Hay métricas de vanidad en vez de métricas que importan a inversores?
   - ¿El ask es específico con milestones concretos?

3. **Producir output** — Escribe `outputs/pitch-deck.md` con el deck completo reescrito, slide a slide. Cada slide incluye título, mensaje clave, contenido, sugerencia visual y la pregunta del inversor que responde.

## Output Format

`outputs/pitch-deck.md` — un H3 por slide:

```
### Slide N: [Título]
**Mensaje clave:** [Lo que el inversor debe recordar]
**Contenido:**
- ...
**Sugerencia visual:** [Qué gráfico, imagen o screenshot va aquí]
**Pregunta del inversor que responde:** [La pregunta implícita en la mente del VC]
```

## Frameworks & Best Practices

### The 10-12 Slide Framework

| # | Slide | Purpose | Common Mistakes |
|---|-------|---------|-----------------|
| 1 | **Title / Hook** | Company name, one-liner, and a memorable hook stat or image | Burying the one-liner; using a generic tagline |
| 2 | **Problem** | Make the pain visceral and specific to your ICP | Being too abstract; citing a problem everyone already knows |
| 3 | **Solution** | Show what you built and how it eliminates the pain | Feature-dumping; not connecting back to the problem |
| 4 | **Demo / Product** | Screenshot, GIF, or live product walkthrough | Showing the admin panel instead of the user-facing magic |
| 5 | **Market Size** | TAM/SAM/SOM with a credible bottoms-up calculation | Using only top-down "the market is $X trillion" numbers |
| 6 | **Business Model** | How you make money, unit economics, pricing | Not showing actual or projected unit economics |
| 7 | **Traction** | The chart that goes up and to the right | Vanity metrics; hiding the Y-axis; mixing timeframes |
| 8 | **Competition** | Why you win — positioning matrix or comparison table | Claiming "no competitors"; using a 2x2 where you magically own the top-right |
| 9 | **Team** | Founders + key hires, relevant backgrounds | Listing every employee; not explaining founder-market fit |
| 10 | **Go-to-Market** | How you acquire customers today and at scale | Saying "we'll go viral" without a concrete channel strategy |
| 11 | **Financials / Ask** | How much you're raising, use of funds, key projections | Not specifying what milestones the money unlocks |
| 12 | **Closing / Vision** | The big dream — where this goes in 5-10 years | Being too conservative; forgetting contact info |

### Narrative Arc Rules

- **Slide 1-3**: Establish tension. The audience should feel the problem before you show the answer.
- **Slide 4-7**: Build credibility. Prove you have a real product with real traction in a real market.
- **Slide 8-10**: Prove defensibility. Show you can win against alternatives and scale.
- **Slide 11-12**: Make the ask and paint the vision. End with ambition, not logistics.

### Stage-Specific Guidance

- **Pre-seed / Seed**: Emphasize problem depth, founder-market fit, and early signals (waitlist, LOIs, design partners). Financial projections can be lighter.
- **Series A**: Emphasize repeatable go-to-market, unit economics, and a clear path from current traction to 3-5x growth. Investors expect real revenue data.

### Principles

- Every slide title should be an assertion, not a label. "We grew 30% MoM for 6 months" beats "Traction".
- Remove any slide that does not advance the narrative. If you cannot articulate why a slide exists, cut it.
- The deck should be understandable by a partner who reads it at 11pm on their iPad without you presenting.
- Use no more than 3 fonts and 2 brand colors. Clutter kills credibility.
- Data beats adjectives. Replace "fast-growing" with "3x YoY".
