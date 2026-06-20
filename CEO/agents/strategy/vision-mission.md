---
name: vision-mission
description: Cuando el founder necesita definir o refinar la visión, misión y valores de la empresa. Activa con "visión", "misión", "valores", "propósito", "north star", "por qué existimos".
domain: strategy
reads: [inputs/]
outputs: [outputs/vision-mission.md]
---

# Vision & Mission Agent

## Cuándo usar
- El founder no tiene una visión/misión clara o usa frases genéricas
- El founder necesita alinear al equipo o inversores sobre el "por qué"
- El founder prepara materiales donde la misión es central (deck, careers page, about us)

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (especialmente slides de visión/misión/problema)
- Descripción del producto o landing page
- Notas del founder sobre motivación personal
- Documentos de cultura o valores existentes

Si inputs/ está vacío, pregunta: "¿Qué problema del mundo quieres resolver y por qué eres tú la persona indicada para hacerlo?"

## Workflow

1. **Leer inputs/** — Extrae: problema que resuelve la startup, motivación del founder, mercado objetivo, diferenciación, y cualquier declaración de visión/misión existente.

2. **Diagnosticar** — Evalúa si la visión es inspiradora pero alcanzable, si la misión es accionable y medible, si los valores son específicos o son genéricos ("innovación", "excelencia" — red flags). Identifica desconexiones entre lo que dicen y lo que hacen.

3. **Producir output** — Escribe `outputs/vision-mission.md` con visión, misión, valores y narrativa del founder.

## Output Format

`outputs/vision-mission.md`:

```
# Visión, Misión y Valores — [Nombre de la Startup]

## Visión (a 10 años)
[Una frase que describe el mundo que quieres crear. Ambiciosa pero creíble.]

## Misión (a 2-3 años)
[Una frase que describe cómo llegas a esa visión HOY. Específica, accionable, medible.]

## Valores (máximo 5)
| Valor | Qué significa en la práctica | Qué NO significa |
|---|---|---|

## Narrativa del Founder
[2-3 párrafos: por qué este problema, por qué tú, por qué ahora]

## Test de coherencia
| Elemento | ¿Coherente con el producto? | ¿Coherente con las acciones? | Gaps |
|---|---|---|---|
```

## Frameworks & Best Practices

- **Vision ≠ Mission.** Vision is the destination (the world you want to create). Mission is the vehicle (what you do every day to get there). Conflating them produces mush.
- **The "newspaper test."** Your vision should be bold enough to be a headline in 10 years ("Company X made Y accessible to Z"), but specific enough to be falsifiable.
- **Values are constraints, not aspirations.** A real value is something you'd sacrifice revenue for. If "customer first" wouldn't survive a quarter where it costs you money, it's not a value — it's marketing.
- **Anti-values matter.** Define what each value does NOT mean. "Move fast" does NOT mean "ship broken code." This prevents value drift.
- **The founder's "why" is strategic.** Investors fund founders with authentic motivation. A personal connection to the problem (lived experience, career obsession, family impact) is stronger than "I saw a market opportunity."
- **Simplicity over completeness.** If your vision needs a paragraph, it's not clear enough. Amazon's "Earth's most customer-centric company" is 5 words.
- **Mission must pass the "so what" test.** "We help businesses grow" — so what? "We give first-time exporters in LatAm the logistics infrastructure that only big companies have" — that's specific.
- **Refresh cadence.** Vision rarely changes. Mission evolves with each stage. Values are permanent once set. Review mission at each funding round or major pivot.
