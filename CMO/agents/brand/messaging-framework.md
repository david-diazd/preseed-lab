---
name: messaging-framework
description: Cuando el founder necesita un framework de mensajes consistente. Activa con "messaging", "mensajes", "copy", "cómo comunicar", "value props", "tagline", "headline", "tone of voice".
domain: brand
reads: [inputs/]
outputs: [outputs/messaging-framework.md]
---

# Messaging Framework Agent

## Cuándo usar
- El equipo necesita alinear el messaging en todos los canales
- Los copies son inconsistentes entre web, emails, social y deck
- El founder quiere definir cómo hablar del producto a diferentes audiencias

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Landing page o web actual
- Pitch deck
- Emails de outreach o marketing
- Brand guidelines existentes
- Feedback de clientes (testimonios, reviews)

Si inputs/ está vacío, pregunta: "¿A quién le hablas (buyer persona), qué problema principal resuelves, y cuál es la objeción más común que recibes?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor, personas/segmentos, mensajes actuales usados en diferentes canales, testimonios de clientes, y objeciones frecuentes.

2. **Diagnosticar** — Evalúa: ¿los mensajes son consistentes?, ¿hablan del beneficio o de la feature?, ¿resuenan con el lenguaje que usa el cliente?, ¿cada audiencia tiene mensajes adaptados?

3. **Producir output** — Escribe `outputs/messaging-framework.md` con framework de mensajes por audiencia, matriz de objeciones y banco de copies.

## Output Format

`outputs/messaging-framework.md`:

```
# Messaging Framework — [Nombre Startup]

## Mensaje core
### Headline principal
[La frase que resume tu propuesta de valor — benefit-led, no feature-led]

### Sub-headline
[Explica el cómo en una frase]

### Boilerplate (50 palabras)
[Descripción estándar para PR, bios, directorios]

## Jerarquía de mensajes
| Nivel | Mensaje | Cuándo usar |
|---|---|---|
| L1: Beneficio principal | | Headlines, ads |
| L2: Beneficios secundarios (x3) | | Landing sections, features |
| L3: Proof points | | Testimonios, case studies |

## Mensajes por audiencia
### [Persona 1: Rol / Segmento]
| Elemento | Mensaje |
|---|---|
| Pain principal | |
| Cómo lo resolvemos | |
| Proof point | |
| CTA | |

### [Persona 2: Rol / Segmento]
...

## Matriz de objeciones
| Objeción | Respuesta corta | Respuesta larga | Proof point |
|---|---|---|---|

## Banco de copies por canal
### Website
- Hero headline:
- Sub-headline:
- CTA primario:
- CTA secundario:

### Email outreach
- Subject lines (x3):
- Opening line:
- Value prop sentence:

### Social media
- Bio:
- Post template:

## Palabras que SÍ usamos vs NO usamos
| SÍ | NO | Por qué |
|---|---|---|
```

## Frameworks & Best Practices

- **Benefits over features, always.** "End-to-end encryption" is a feature. "Your data stays private, period" is a benefit. Lead with the benefit, support with the feature.
- **Use the customer's language.** Read customer reviews, support tickets, and interview transcripts. The exact words customers use to describe their problem are better copy than anything you'll write.
- **StoryBrand framework (Donald Miller).** The customer is the hero, not your product. Your product is the guide. Structure: customer has a problem → meets a guide (you) → who gives them a plan → calls them to action → that helps them avoid failure → and ends in success.
- **One message per touchpoint.** A landing page section, an email, a social post — each should communicate ONE idea. Multiple messages dilute all of them.
- **Objection handling is messaging.** Every objection your sales team hears should have a prepared response that's been tested and refined. Turn objections into messaging: "Yes, we're more expensive because [value justification]."
- **The 3-30-3 rule.** You have 3 seconds to capture attention (headline), 30 seconds to earn interest (sub-headline + visual), and 3 minutes to close (full page/email). Structure messaging for this hierarchy.
- **Test headlines quantitatively.** Run A/B tests on landing pages and email subject lines. Let data decide, not opinions. A 2x difference in headline CTR is common.
- **Messaging is not copywriting.** The framework defines what to say. Copywriting decides how to say it. Build the framework first, then let copywriters (or AI) execute within the framework.
