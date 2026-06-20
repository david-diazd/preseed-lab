---
name: customer-discovery
description: Cuando el founder necesita diseñar o sintetizar entrevistas de customer discovery. Activa con "customer discovery", "entrevistas", "hablar con clientes", "validación", "problem interview", "mom test", "descubrimiento de cliente".
domain: market
reads: [inputs/]
outputs: [outputs/customer-discovery.md]
---

# Customer Discovery Agent

## Cuándo usar
- El founder necesita diseñar un guion de entrevistas para validar el problema
- El founder tiene notas de entrevistas y necesita sintetizar insights
- El equipo quiere validar si el problema es real antes de construir

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Notas de entrevistas con clientes o usuarios
- Transcripciones de calls
- Encuestas completadas
- Descripción del problema/hipótesis a validar

Si inputs/ está vacío, pregunta: "¿Cuál es la hipótesis principal que quieres validar, quién es tu cliente target, y cuántas entrevistas has hecho (si alguna)?"

## Workflow

1. **Leer inputs/** — Extrae: hipótesis del founder, cliente target, entrevistas realizadas (si hay), insights previos, y qué preguntas no se han respondido.

2. **Diagnosticar** — Evalúa: ¿las entrevistas siguen los principios de The Mom Test?, ¿hay confirmation bias en las preguntas?, ¿la muestra es suficiente?, ¿se están descubriendo insights o solo confirmando lo que ya creen?

3. **Producir output** — Escribe `outputs/customer-discovery.md` con guion de entrevistas (si no han hecho), síntesis de insights (si ya tienen datos), o ambos.

## Output Format

`outputs/customer-discovery.md`:

```
# Customer Discovery — [Nombre Startup]

## Hipótesis a validar
| # | Hipótesis | Estado | Evidencia |
|---|---|---|---|
| H1 | [El problema existe] | ✅/❌/🔄 | |
| H2 | [El segmento X lo tiene] | | |
| H3 | [Están dispuestos a pagar] | | |

## Guion de entrevistas (Mom Test)

### Apertura (2 min)
[Cómo empezar la conversación sin sesgar]

### Sobre el problema (10 min)
1. [Pregunta abierta sobre su trabajo/vida — no sobre tu producto]
2. [Pregunta sobre la última vez que enfrentaron el problema]
3. [Pregunta sobre qué soluciones han probado]
4. [Pregunta sobre qué no funcionó de esas soluciones]
5. [Pregunta sobre el coste del problema (tiempo, dinero, frustración)]

### Sobre la solución actual (5 min)
6. [Qué usan hoy]
7. [Qué les frustra de lo que usan]
8. [Han intentado cambiar — qué los frenó]

### Cierre (3 min)
9. [Pregunta de compromiso: ¿pagarían? ¿harían beta? ¿presentarían a alguien?]
10. [Pedir referrals]

### Preguntas PROHIBIDAS
- ❌ "¿Te gustaría un producto que...?"
- ❌ "¿Usarías esto?"
- ❌ "¿Cuánto pagarías por...?"
[Explicación de por qué cada una es trampa]

## Síntesis de entrevistas (si hay datos)
### Patrones encontrados
| Patrón | Frecuencia | Cita representativa |
|---|---|---|

### Segmentos emergentes
| Segmento | Problema | Intensidad | Willingness to pay |
|---|---|---|---|

### Insights inesperados
[Cosas que el equipo no esperaba encontrar]

## Próximos pasos
| Acción | Por qué | Deadline |
|---|---|---|
```

## Frameworks & Best Practices

- **The Mom Test (Rob Fitzpatrick).** Never ask "would you use this?" or "do you like this idea?" People lie to be nice. Instead, ask about their past behavior: "How do you handle X today?" "What happened last time you tried to solve X?" "How much time/money does X cost you?"
- **Talk about their life, not your idea.** The best customer discovery interviews feel like conversations about the customer's problems, not pitch sessions for your product.
- **Commitment over compliments.** "That sounds cool!" is a compliment (worthless). "I'd pay $50/month for that" is a commitment (weak). "Here's my credit card" is a commitment (strong). Measure signal by level of commitment.
- **5 interviews reveal the pattern.** After 5 interviews in a segment, patterns emerge. After 10, you hear repetition. If you don't see patterns after 15, your segment is too broad.
- **Interview in pairs.** One person asks questions, one takes notes. The interviewer can focus on follow-up questions; the note-taker captures exact quotes and body language.
- **Record everything (with permission).** "Do you mind if I record this for my notes?" Gets a 95% yes rate. Transcripts are infinitely more useful than scribbled notes.
- **Ask for referrals at the end.** "Who else deals with this problem that I should talk to?" This snowball sampling finds your real target segment faster than LinkedIn outreach.
- **Avoid confirmation bias.** Actively look for evidence that your hypothesis is WRONG. If you only hear what confirms your idea, you're doing it wrong.
