---
name: privacy-policy
description: Cuando el founder necesita crear o revisar su política de privacidad. Activa con "política de privacidad", "privacy policy", "GDPR", "protección de datos", "LOPD", "tratamiento de datos".
domain: legal-ops
reads: [inputs/]
outputs: [outputs/privacy-policy.md]
---

# Privacy Policy Agent

## Cuándo usar
- El founder va a lanzar su producto y necesita política de privacidad (obligatoria si recopila datos)
- El founder opera en la UE y necesita cumplir con el GDPR
- El founder quiere revisar si su política actual cubre todos los tratamientos de datos que hace

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Política de privacidad actual (si existe)
- Descripción del producto y qué datos recoge
- Lista de terceros que procesan datos (analytics, CRM, emails, pagos)
- Jurisdicción y mercados objetivo

Si inputs/ está vacío, pregunta: "¿Qué datos recoge tu producto (email, nombre, datos de uso, datos de pago)? ¿Operas en la UE?"

**Advertencia:** Este agente genera un borrador. Para productos que tratan datos sensibles o en jurisdicciones específicas, valida con un abogado especializado en protección de datos.

## Workflow

1. **Leer inputs/** — Extrae: qué datos se recopilan, para qué propósito, con qué terceros se comparten, cuánto tiempo se retienen, y en qué jurisdicciones opera el producto.

2. **Diagnosticar** — Evalúa si el tratamiento de datos tiene base legal suficiente (consentimiento, interés legítimo, contrato), si faltan categorías de datos en la política actual, y si hay transferencias internacionales de datos que necesitan cobertura.

3. **Producir output** — Escribe `outputs/privacy-policy.md` con la política completa adaptada al producto y jurisdicción.

## Output Format

`outputs/privacy-policy.md` con estas secciones:

```
# Política de Privacidad — [Empresa]
*Última actualización: [fecha]*

## 1. Responsable del tratamiento
## 2. Datos que recopilamos
## 3. Finalidad y base legal del tratamiento
## 4. Terceros con quienes compartimos datos
## 5. Transferencias internacionales [si aplica]
## 6. Período de retención
## 7. Derechos del usuario (acceso, rectificación, supresión, portabilidad)
## 8. Cookies [si aplica]
## 9. Seguridad de los datos
## 10. Menores de edad [si aplica]
## 11. Modificaciones de esta política
## 12. Contacto y DPO [si aplica]
```

## Frameworks & Best Practices

### GDPR Core Requirements
- Lawful basis required for each processing activity (Art. 6).
- Data Protection Impact Assessment for high-risk processing (Art. 35).
- 72-hour breach notification to supervisory authority (Art. 33).
- Data Processing Agreements with all processors (Art. 28).
- Right to erasure with defined exceptions (Art. 17).
- Privacy by design and by default (Art. 25).

### CCPA/CPRA Core Requirements
- "Do Not Sell or Share My Personal Information" link required if applicable.
- Right to know, delete, correct, and opt out of sale/sharing.
- 12-month lookback for data collection disclosures.
- Sensitive personal information: right to limit use (CPRA addition).
- Service provider vs. contractor vs. third party distinctions matter.

### Plain Language Principles
- Write at an 8th-grade reading level with short sentences.
- Use concrete examples instead of abstract categories.
- Avoid "may" when you mean "do." Be specific about actual practices.
- The policy must match what your product actually does -- no over-disclosure and no under-disclosure.

### Pre-Publication Checklist
- [ ] Attorney review completed
- [ ] Policy matches actual data practices
- [ ] User privacy request processes are accessible and functional
- [ ] Technical security measures implemented
- [ ] Data Processing Agreements in place with all third parties
- [ ] Legal basis documented for each processing activity
- [ ] Cookie consent mechanism implemented (EU users)
- [ ] User notification system for material policy changes

### Common Startup Pitfalls
- Copying another company's privacy policy (their data practices are not yours).
- Missing analytics and advertising SDKs in disclosures (Google Analytics, Mixpanel, Facebook Pixel all collect personal data).
- No mechanism to actually fulfill deletion requests in the codebase.
- Assuming B2B means no privacy obligations (you still process individual user data).
- Listing data categories you do not actually collect (over-disclosure invites scrutiny).

### Output Structure (15 sections)
1. **Preamble** -- Who you are, what this policy covers, effective date, contact methods.
2. **Information We Collect** -- Categories: personal info, usage data, device information, location, payment info, communications, sensitive data.
3. **How We Collect Information** -- Methods: direct entry, automatic tracking, third parties.
4. **How We Use Information** -- Purposes: service provision, support, improvements, analytics, marketing, security, legal compliance.
5. **Legal Basis for Processing** -- Consent, contract performance, legal obligation, vital interests, legitimate interests (GDPR-focused).
6. **Data Sharing and Third Parties** -- Service providers, partners, legal authorities, with specifics on who and why.
7. **International Data Transfer** -- Cross-border transfer mechanisms (SCCs, adequacy decisions), storage locations.
8. **Data Retention** -- Specific timeframes for account data, logs, deleted content.
9. **User Rights** -- Access, deletion, correction, restrict processing, portability, opt-out, complaint procedures -- organized by jurisdiction.
10. **Cookies and Tracking** -- Tools used, purposes, management options, consent requirements.
11. **Security** -- Encryption, access controls, audits, incident response, limitations.
12. **Children's Privacy** -- Parental consent, age gates, COPPA/UK Children's Code compliance.
13. **Contact and Rights Requests** -- Privacy email, address, response timeframes, DPO info.
14. **Policy Changes** -- Notice period, notification methods, user opt-out options.
15. **Additional Provisions** -- Data sale disclosure, third-party link disclaimers, governing law, effective date.

---

**Disclaimer:** Este agente genera borradores de política de privacidad con fines de planificación. No constituye asesoramiento legal. Consulta siempre con un abogado cualificado en tu jurisdicción antes de publicar. El incumplimiento del GDPR puede acarrear multas de hasta el 4% de la facturación anual global.
