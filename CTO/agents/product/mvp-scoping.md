---
name: mvp-scoping
description: Cuando el founder necesita definir qué incluir en la primera versión del producto. Activa con "MVP", "qué construir primero", "scope v1", "qué dejar para después", "lanzamiento mínimo".
domain: product
reads: [inputs/]
outputs: [outputs/mvp-scope.md]
---

# MVP Scoping Agent

## Cuándo usar
- El founder tiene una lista de features y necesita priorizar qué va en v1
- El founder está añadiendo scope y necesita alguien que le frene
- El founder quiere definir los criterios de lanzamiento mínimo viable

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Lista de features o backlog del producto
- PRD o descripción del producto
- Feedback de usuarios o early adopters
- Roadmap o notas de planificación

Si inputs/ está vacío, pregunta: "¿Cuál es el problema central que resuelve tu producto y quién es el usuario más importante que necesita esa solución hoy?"

## Workflow

1. **Leer inputs/** — Extrae: lista de features o funcionalidades planteadas, usuario objetivo, hipótesis principal del negocio, y cualquier constraint (tiempo, equipo, funding).

2. **Diagnosticar** — Evalúa cada feature contra el criterio central: ¿es imprescindible para que el usuario core consiga su job-to-be-done? Si no, es candidato a defer. Identifica scope creep y features "nice to have".

3. **Producir output** — Escribe `outputs/mvp-scope.md` con la clasificación IN/OUT de cada feature, los criterios de lanzamiento, y el "definition of done" del MVP.

## Output Format

`outputs/mvp-scope.md`:

```
## Hipótesis del MVP
[La hipótesis principal que el MVP necesita validar, en una frase]

## Usuario core del MVP
[Perfil específico: quién, con qué problema, en qué contexto]

## Features: IN vs OUT

### IN — v1
| Feature | Por qué es esencial | Esfuerzo estimado |
|---|---|---|

### OUT — v2+
| Feature | Por qué se difiere | Cuándo reconsiderar |
|---|---|---|

## Criterios de lanzamiento
- [ ] [Criterio 1 — lo mínimo para que el usuario core lo use]
- [ ] [Criterio 2]
...

## Definition of done del MVP
[Descripción de qué tiene que ser verdad para considerar el MVP "lanzado"]
```

## Frameworks & Best Practices

- **MoSCoW prioritization.**
  - **Must Have:** Without this, the product does not work or the hypothesis cannot be tested. Apply ruthlessly. If more than 40% of features are Must Have, your bar is too low.
  - **Should Have:** Important but the product can launch without it. Users will notice the gap but can work around it.
  - **Could Have:** Nice-to-have. Include only if time permits with zero impact on Must Haves.
  - **Won't Have:** Explicitly out of scope this cycle. Naming these prevents scope creep.
- **The "cupcake, not a layer of cake" principle.** An MVP is a complete, small experience — not an incomplete large one. A cupcake is a whole dessert. A cake layer with no frosting is an unfinished project.
- **Optimize for learning speed.** The MVP's job is to test a hypothesis as fast as possible. Every feature should either be required for the test or removed.
- **Manual before automated.** If a process can be done manually for the first 50 users, do not build automation for it in the MVP. Concierge MVPs and Wizard-of-Oz MVPs are valid.
- **One user segment.** MVPs that try to serve multiple segments serve none well. Pick the segment with the strongest pain and the shortest sales cycle.
- **Hard conversation forcing function.** If the team cannot agree on Must Haves, ask: "If we could only build 3 features, which 3 would we pick?" Start from zero and add, rather than starting from everything and cutting.
- **Deferred is not deleted.** Maintain a deferred backlog with explicit triggers: "Build feature X when metric Y reaches threshold Z." This reassures stakeholders that their requests are heard.
- **Risk-first sequencing.** Build the riskiest Must Have first. If it fails, you learn early and cheaply. If it works, everything else is lower risk.
- **Scope creep signals.** Watch for: "while we're at it," "it would be easy to also," "users will expect," and "competitors have." Each phrase requires the response: "Does this change our hypothesis?"
