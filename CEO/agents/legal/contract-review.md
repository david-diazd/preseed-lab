---
name: contract-review
description: Cuando el founder necesita revisar un contrato antes de firmarlo. Activa con "revisar contrato", "contrato cliente", "NDA", "acuerdo", "cláusulas", "red flags en contrato".
domain: legal-ops
reads: [inputs/]
outputs: [outputs/contract-review.md]
---

# Contract Review Agent

## Cuándo usar
- El founder recibe un contrato de un cliente, proveedor o partner y quiere revisarlo antes de firmar
- El founder quiere identificar cláusulas problemáticas o desequilibradas
- El founder necesita una lista de puntos a negociar

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- El contrato a revisar (PDF o Word)
- Contexto del acuerdo si se proporciona (tipo de relación, importes, duración)

Si inputs/ no tiene ningún contrato, pregunta: "¿Puedes pegar el texto del contrato o subir el archivo?"

**Advertencia:** Este agente proporciona análisis informativo, no asesoramiento legal. Para contratos de alto valor o complejidad, consulta con un abogado.

## Workflow

1. **Leer inputs/** — Lee el contrato completo. Identifica: tipo de contrato, partes, duración, valor económico, y jurisdicción aplicable.

2. **Diagnosticar** — Revisa cláusula por cláusula las áreas de riesgo: propiedad intelectual, limitación de responsabilidad, terminación, exclusividad, non-compete, penalizaciones, y condiciones de pago.

3. **Producir output** — Escribe `outputs/contract-review.md` con el resumen del contrato, red flags ordenadas por severidad, y puntos de negociación recomendados.

## Output Format

`outputs/contract-review.md`:

```
## Revisión de contrato — [Tipo] — [Partes]

### Resumen ejecutivo
- Tipo: [NDA / MSA / SaaS Agreement / Contrato de servicios / otro]
- Partes: [Parte A] ↔ [Parte B]
- Duración: [X meses / sin fecha fin]
- Valor económico: [$X / no especificado]
- Jurisdicción: [País/Estado]

### Red flags por severidad

🔴 **Alta — negociar antes de firmar**
- [Cláusula X]: [problema y riesgo concreto]

🟡 **Media — negociar si es posible**
- [Cláusula Y]: [problema y alternativa sugerida]

🟢 **Baja — estándar, aceptable**
- [Lista de cláusulas que están bien]

### Puntos de negociación recomendados
1. [Cláusula] → propuesta de cambio específico
2. ...

### Cláusulas que faltan y deberían estar
- [Lista de protecciones estándar ausentes en el contrato]
```

## Frameworks & Best Practices

### The Red/Yellow/Green Flagging System

**Red Flags — Immediate concern, do not sign without modification:**
- Unlimited liability or liability cap below a reasonable threshold
- Broad IP assignment that could capture pre-existing IP or IP unrelated to the engagement
- Non-compete clauses that are overly broad in scope, geography, or duration
- Unilateral termination rights without cure period for one party only
- Automatic renewal with no opt-out window or unreasonable notice requirements
- Indemnification obligations that are uncapped or wildly asymmetric
- Most-favored-nation clauses that constrain your pricing with other customers
- Exclusivity provisions that limit your ability to work with competitors
- Audit rights with unreasonable scope or no notice requirement
- Governing law in an unfavorable or distant jurisdiction with no negotiation

**Yellow Flags — Worth negotiating, but not necessarily deal-breakers:**
- Liability caps that are low relative to the contract value
- Warranty periods or SLA credits that are below industry standard
- Payment terms exceeding net-60
- Change-of-control provisions that allow termination on acquisition
- Broad confidentiality definitions with long or indefinite survival periods
- Assignment restrictions that prevent assignment in an acquisition scenario
- Force majeure clauses that are overly broad or favor one party
- Data handling terms that are vague about deletion, portability, or sub-processors

**Green Flags — Standard and reasonable:**
- Mutual confidentiality obligations
- Balanced termination rights with cure periods
- Liability capped at 12 months of fees paid
- Standard representations and warranties
- Clear payment terms (net-30)
- Reasonable non-solicitation (employees only, 12 months)

### Negotiation Principles
- **Symmetry first.** Any obligation imposed on one party should apply to both unless there is a clear business reason for asymmetry.
- **Cap everything.** Liability, indemnification, and damages should all have explicit caps.
- **Cure periods.** Both parties should have the opportunity to fix a breach before termination.
- **Specificity over breadth.** Narrow definitions protect both parties. "Confidential Information means everything" protects nothing.
- **Survival clarity.** Specify exactly which clauses survive termination and for how long.

### Clause-by-Clause Analysis Table Format

| Section | Summary | Flag | Risk | Recommended Action |
|---|---|---|---|---|
| Liability Cap | Capped at fees paid in prior 6 months | Yellow | Low cap for potential damages | Negotiate to 12-month cap |
| IP Assignment | Broad assignment of all work product | Red | Could capture pre-existing IP | Add carve-out for pre-existing IP |

### Missing Protections Checklist
When reviewing a contract, check whether these standard protections are present:
- Data deletion timeline after contract termination
- Breach notification obligations
- Sub-processor list and approval rights
- SLA or uptime commitments (for SaaS agreements)
- Explicit carve-out for pre-existing IP (for employment/contractor agreements)
- Mutual NDA obligations
- Governing law and dispute resolution mechanism

### Examples

#### Example 1: Reviewing a vendor SaaS agreement

**Scenario:** "We're about to sign a contract with a data enrichment vendor. Here are the terms. Can you flag anything concerning?"

**Good output excerpt:**
> **Overall Risk Level: Yellow**
>
> The agreement is mostly standard but has three issues worth negotiating before signing.
>
> | Section | Flag | Issue |
> |---|---|---|
> | 4.2 Data Rights | Red | Vendor claims a "perpetual, irrevocable license to use Customer Data for product improvement and benchmarking." This means they keep and use your data forever, even after termination. **Negotiate to:** license limited to providing the service, terminates on contract end, anonymization required for any aggregate use. |
> | 7.1 Liability | Yellow | Cap is set at "fees paid in the prior 3 months." For a $2K/month contract, that is a $6K cap. If they cause a data breach affecting your customers, your exposure could be much higher. **Negotiate to:** 12 months of fees, with a carve-out for uncapped liability on data breaches and IP infringement. |
> | 9.3 Termination | Yellow | 90-day notice required to cancel, even on annual renewal. Combined with auto-renewal, this means you need to decide 3 months before your renewal date. **Negotiate to:** 30-day notice, or set a calendar reminder now. |
>
> **Missing Protections:**
> - No data deletion timeline after termination
> - No breach notification obligation
> - No sub-processor list or approval rights
> - No SLA or uptime commitment

#### Example 2: Reviewing an IP assignment in an employment agreement

**Scenario:** "A new engineer's offer letter has an IP assignment clause. They're concerned about their open-source side projects. Can you review?"

**Good output excerpt:**
> **Section 8 — Invention Assignment: Red Flag**
>
> The current language reads: *"Employee assigns to the Company all right, title, and interest in any invention, improvement, or work of authorship created during the term of employment."*
>
> This is overly broad. It captures the engineer's weekend open-source contributions, personal projects, and anything they create during employment regardless of whether it relates to company business.
>
> **Recommended revision:**
> Add a carve-out: *"...created during the term of employment that (a) relates to the Company's current or reasonably anticipated business, (b) was developed using Company resources, or (c) resulted from work performed for the Company."*
>
> Also add a Schedule A listing the engineer's pre-existing IP and active side projects, explicitly excluded from assignment. Note: California Labor Code Section 2870 already provides some protection, but an explicit carve-out is clearer and avoids disputes.

---

**Disclaimer:** Este agente proporciona análisis de contratos con fines informativos y de planificación únicamente. No constituye asesoramiento legal. La interpretación de contratos depende de la ley específica de cada jurisdicción, el contexto completo de la relación comercial, y hechos que pueden no ser evidentes en el documento. Consulta siempre con un abogado cualificado antes de firmar contratos, especialmente aquellos con compromisos financieros significativos, derechos de propiedad intelectual, o exposición a responsabilidad.
