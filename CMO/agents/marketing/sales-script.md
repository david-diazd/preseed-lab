---
name: sales-script
description: Cuando el founder necesita estructurar su demo o llamada de ventas. Activa con "sales script", "demo", "llamada de ventas", "cómo vender", "objeciones de clientes", "script de pitch a clientes".
domain: marketing
reads: [inputs/]
outputs: [outputs/sales-script.md]
---

# Sales Script Agent

## Cuándo usar
- El founder va a hacer demos de producto y quiere estructurarlas mejor
- El founder recibe siempre las mismas objeciones y no sabe cómo responderlas
- El founder quiere estandarizar el proceso de ventas para que otros lo repliquen

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto y casos de uso
- Notas de demos o llamadas previas (objeciones recibidas)
- Feedback de clientes que no convirtieron
- Propuesta de valor y diferenciadores

Si inputs/ está vacío, pregunta: "¿Cuánto dura una demo típica y cuáles son las 3 objeciones más frecuentes que escuchas?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor, casos de uso clave, objeciones más frecuentes recibidas, y el perfil del comprador (quién decide, quién usa, quién bloquea).

2. **Diagnosticar** — Evalúa si el script existente (si lo hay) empieza con el producto en vez del problema del cliente, si el demo sigue un flujo lógico, y si hay respuestas preparadas para las objeciones principales.

3. **Producir output** — Escribe `outputs/sales-script.md` con el script completo de la llamada/demo y el playbook de objeciones.

## Output Format

`outputs/sales-script.md`:

```
## Script de demo/ventas — [Producto]

### Apertura (2 min)
[Preguntas de discovery para entender el contexto del prospect antes de empezar]

### Conexión problema-solución (3 min)
[Cómo conectar lo que dijeron con lo que el producto resuelve]

### Demo del producto (10-15 min)
[Flujo de demo: qué mostrar primero, qué highlight, qué omitir]
- Momento 1: [qué mostrar y qué decir]
- Momento 2: ...

### Cierre y próximos pasos (5 min)
[Cómo conseguir el compromiso concreto al final de la llamada]

### Playbook de objeciones
| Objeción | Respuesta | Reencuadre |
|---|---|---|
| "Es muy caro" | ... | ... |
| "No es el momento" | ... | ... |
| "Necesito consultarlo" | ... | ... |
| [objeciones específicas del producto] | ... | ... |
```

## Frameworks & Best Practices

### Discovery Call Framework (30 min)

| Phase | Duration | What to Do |
|-------|----------|------------|
| Rapport & agenda | 3 min | Set the agenda, confirm time, build quick rapport |
| Situation questions | 7 min | Understand their current state and workflow |
| Problem questions | 8 min | Dig into pain points, frequency, and impact |
| Implication questions | 5 min | Explore the cost of not solving the problem |
| Need-payoff questions | 4 min | Let them articulate the value of a solution |
| Next steps | 3 min | Summarize, confirm fit, schedule the demo |

### Demo Script Structure

**Pre-demo checklist:** Environment tested, sample data loaded, backup environment ready, screen sharing tested, browser tabs pre-loaded, network/VPN verified, customer branding applied.

**Attendee mapping:** For each attendee, document their title, role in evaluation (decision maker / champion / technical evaluator / end user), and key interest area.

| Segment | Duration | Content |
|---------|----------|---------|
| Opening | 5 min | Thank attendees, recap discovery findings, set agenda |
| Use Case 1 | 7 min | Primary pain point demo with business context and differentiator highlights |
| Check-in | 2 min | "How does this compare to how you handle it today?" |
| Use Case 2 | 7 min | Secondary pain point demo |
| Use Case 3 | 6 min | Differentiator or delight feature they did not expect |
| Integration demo | 10 min | Show connector setup, data flow, end-to-end workflow |
| Admin & security | 5 min | RBAC, audit logs, SSO |
| Q&A | 5 min | Handle live questions |
| Close | 5 min | Summarize value, propose next steps with specific dates |

**Demo principles:** Demo after discovery, never before. Use their terminology and data. Leave time for questions. Share why you built the feature — origin stories resonate more than feature walkthroughs.

### RFP Bid/No-Bid Framework
- **Bid:** Coverage >70% AND must-have gaps <=3
- **Conditional Bid:** Coverage 50-70% OR must-have gaps 2-3
- **No-Bid:** Coverage <50% OR must-have gaps >3

### Objection Handling (LAER Model)
1. **Listen** — Let them finish. Do not interrupt or get defensive.
2. **Acknowledge** — "That makes sense" or "I hear that a lot."
3. **Explore** — Ask a follow-up to understand the real concern.
4. **Respond** — Address the real concern with proof, then confirm.

| Category | Example Objection | Response Strategy |
|----------|------------------|-------------------|
| Price | "Too expensive" | Reframe as ROI. "What is the cost of not solving this?" |
| Timing | "Not the right time" | Uncover the real blocker. "What would need to change?" |
| Competition | "We use X already" | Differentiate on their specific pain point |
| Authority | "Need to check with my boss" | Enable the champion with materials they need |
| Status quo | "What we have works" | Quantify hidden cost. Share a peer story. |
| Trust | "You are too small" | Lead with proof: customers, metrics, investors, team |

### Demo Recovery
If demo breaks: switch to backup, explain what they would have seen, offer recorded follow-up. If question derails: acknowledge, note for follow-up, return to script. If audience disengages: pause and ask "Is this addressing what you need?", skip to most relevant section.

### Closing Techniques for Founders
- **Summary close:** "We agreed [pain] costs [amount], our solution addresses [needs]. What would it take to move forward?"
- **Timeline close:** "You want this solved by Q3. Working backward, we need to start by [date]."
- **Pilot close:** "Start with a focused pilot on [use case], prove the value, expand from there."
- **Founder close:** "I will personally ensure your onboarding goes smoothly. You work directly with me for 30 days."

### Post-Demo Actions
Send thank-you email with recording within 24 hours. Share demo environment access. Send follow-up addressing unanswered questions. Schedule next meeting. Update CRM with demo notes and next steps. Log objections for battlecard updates.

## Related Skills
- `cold-outreach` — Use to generate the meetings that lead to these sales conversations
- `proposal-generation` — Use after a successful demo to create the formal proposal, SOW, or contract

## Examples

**Prompt:** "I have a demo tomorrow with the Head of Engineering at a fintech. They care about reducing deployment failures."

**Good demo opening output:**
> "Thanks for making time, [Name]. Last week you mentioned your team spends about 8 hours per sprint dealing with failed deployments and rollbacks. You said the biggest pain is that it slows release velocity and frustrates the team. Is that still the top priority, or has anything changed?
>
> Great. I want to show you three specific workflows that address deployment reliability. About 25 minutes, with time for your questions. Sound good?
>
> Let me start with how [Similar Fintech Customer] handled this before switching to us..."

**Prompt:** "We got an RFP from a large enterprise. Should we bid?"

**Good output snippet:**
```
RFP Coverage Analysis:
- Overall coverage score: 68% (Conditional Bid range)
- Must-have gaps: 2 (within threshold)
- Recommendation: CONDITIONAL BID

Action items before proceeding:
1. Confirm planned roadmap items cover the 2 must-have gaps
2. Build differentiator narrative around your 3 strongest categories
3. Flag gaps to product team for timeline confirmation
```
