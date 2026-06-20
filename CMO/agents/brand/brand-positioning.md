---
name: brand-positioning
description: Cuando el founder necesita definir el posicionamiento de marca. Activa con "posicionamiento", "brand", "marca", "cómo nos perciben", "identidad", "branding", "diferenciación de marca".
domain: brand
reads: [inputs/]
outputs: [outputs/brand-positioning.md]
---

# Brand Positioning Agent

## Cuándo usar
- El founder lanza un producto y necesita definir cómo posicionarse en el mercado
- El founder siente que su producto no se diferencia lo suficiente
- El equipo necesita alinear toda la comunicación bajo un mismo posicionamiento

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (propuesta de valor, competencia)
- Landing page o web actual
- Análisis de competidores
- Feedback de clientes sobre percepción

Si inputs/ está vacío, pregunta: "¿Qué producto vendes, a quién, y si tuvieras que explicarlo en una frase a alguien en un ascensor, qué dirías?"

## Workflow

1. **Leer inputs/** — Extrae: propuesta de valor, segmentos de clientes, competidores, diferenciación actual, tono de comunicación, y percepción de clientes si existe.

2. **Diagnosticar** — Evalúa: ¿el posicionamiento es claro o genérico?, ¿se diferencia de competidores?, ¿resuena con el ICP?, ¿es consistente en todos los touchpoints?

3. **Producir output** — Escribe `outputs/brand-positioning.md` con positioning statement, mapa perceptual y guía de comunicación.

## Output Format

`outputs/brand-positioning.md`:

```
# Brand Positioning — [Nombre Startup]

## Positioning Statement
Para [segmento de cliente] que [necesidad/problema],
[Nombre] es la [categoría] que [beneficio principal]
a diferencia de [alternativa principal] porque [diferenciación clave].

## Mapa perceptual
[Ejes que importan al cliente — posición de competidores vs tu marca]

## Pilares de marca
| Pilar | Qué significa | Cómo se manifiesta |
|---|---|---|
| [Pilar 1] | | |
| [Pilar 2] | | |
| [Pilar 3] | | |

## Personalidad de marca
| Dimensión | Somos | No somos |
|---|---|---|
| Tono | | |
| Lenguaje | | |
| Visual | | |

## Arquetipos de marca
[Arquetipo primario y secundario con justificación]

## Elevator pitch (3 versiones)
### 10 segundos
[Una frase]

### 30 segundos
[3-4 frases]

### 2 minutos
[Párrafo completo con contexto y diferenciación]

## Consistencia across touchpoints
| Touchpoint | Mensaje actual | Mensaje alineado |
|---|---|---|
| Landing page | | |
| Social media bio | | |
| Email signature | | |
| Pitch deck slide 1 | | |
| Job postings | | |
```

## Frameworks & Best Practices

- **Positioning is not what you say — it's what the customer thinks.** Your positioning statement is a guide for your team, not a tagline for customers. It informs all communication but isn't communicated directly.
- **April Dunford's positioning framework.** Five elements: competitive alternatives (what they'd do without you), unique attributes (what you have that alternatives don't), value (the benefit those attributes enable), target customers (who cares most), and market category (the context that makes your value obvious).
- **Own a category or create one.** If you're "like Salesforce but cheaper," you'll always be compared to Salesforce. If you're "the first revenue intelligence platform for SMB," you own the category.
- **Specificity beats breadth.** "Project management for architects" is stronger than "project management for everyone." The more specific your positioning, the harder it is to compete with you.
- **Test positioning with the "so what?" chain.** "We use AI" → so what? → "To automate data entry" → so what? → "So your team saves 10 hours/week on manual work." Keep going until you reach something the customer viscerally cares about.
- **Positioning evolves with stage.** Pre-seed: position around the problem you solve. Post-PMF: position around your unique advantage. At scale: position around the category you own.
- **Competitive positioning requires honesty.** Don't position against competitors you can't actually beat. Position against the real alternative — which is often "do nothing" or "use a spreadsheet."
- **Consistency is underrated.** The same positioning should appear in your deck, your website, your cold emails, and your job postings. Inconsistency confuses customers and team members.
