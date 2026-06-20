---
name: investor-research
description: Cuando el founder quiere identificar y priorizar inversores para su ronda. Activa con "lista de inversores", "a quién pitchar", "buscar VCs", "inversores para mi startup", "angel investors".
domain: fundraising
reads: [inputs/]
outputs: [outputs/investor-research.md]
---

# Investor Research Agent

## Cuándo usar
- El founder va a empezar a fundraisear y necesita una lista de targets
- El founder tiene una lista de inversores y quiere cualificarlos o priorizarlos
- El founder quiere entender si un fondo específico encaja con su startup

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Pitch deck (para extraer stage, sector, modelo de negocio, geografía)
- Modelo financiero (para extraer el importe de la ronda y runway)
- Descripción de la empresa o one-pager
- Lista previa de inversores (si el founder ya tiene una)

Si inputs/ está vacío, pregunta: "¿Cuál es el stage de tu startup, en qué sector estás y cuánto estás buscando levantar?"

## Workflow

1. **Leer inputs/** — Extrae de los documentos disponibles: stage, sector/vertical, modelo de negocio, geografía, importe de la ronda objetivo, inversores actuales y cualquier inversor ya en conversación.

2. **Diagnosticar** — Define los criterios de filtrado: stage match, sector focus, tamaño de cheque, geografía y conflictos de portfolio. Identifica cualquier inversor de la lista existente del founder que no cumpla los criterios.

3. **Producir output** — Escribe `outputs/investor-research.md` con la lista tiered de inversores (T1/T2/T3), warm paths para los T1, y sección de conflictos excluidos.

## Output Format

`outputs/investor-research.md`:

```
## Lista de inversores — [Nombre empresa] — [Ronda]

### Tier 1 — Alta prioridad
| Firma | Partner | Stage | Sector | Cheque típico | Fondo reciente | Conflicto | Warm path |
|---|---|---|---|---|---|---|---|

### Tier 2 — Buena adecuación
[misma tabla]

### Tier 3 — Backfill
[misma tabla]

## Conflictos excluidos
[Firma — razón del conflicto]

## Gaps de investigación
[Lo que no se ha podido verificar y necesita input del founder]
```

## Frameworks & Best Practices

### Investor Qualification Criteria (The 7-Point Filter)

1. **Stage fit** — Does the firm invest at the founder's current stage? A Series B fund will not lead a seed round. This is the first filter and it is binary: pass or fail.
2. **Sector focus** — Does the firm have a stated thesis or track record in the founder's sector? Look at their last 10 investments, not just their website copy.
3. **Check size match** — Does the firm's typical check size align with what the founder needs? A $2B fund rarely writes $500K checks. A $50M fund rarely leads $20M rounds.
4. **Portfolio conflicts** — Does the firm already have a company in the same space? This is the most common reason pitches are dead-on-arrival. Check every portfolio company, including quiet ones.
5. **Fund vintage** — Is the firm actively deploying from a recent fund? A fund raised 4+ years ago is likely in harvest mode and not writing new checks. Prefer firms that closed a fund within the last 18 months.
6. **Geographic relevance** — Some firms only invest locally. Others require board seats that demand proximity. Remote-friendly firms have expanded, but geography still matters for many funds.
7. **Partner-level interest** — Is there a specific partner whose background, interests, or public writing aligns with the startup? Pitching the right partner at the right firm matters as much as pitching the right firm.

### Tiering Framework

- **Tier 1**: Matches on 6-7 of the criteria above. The firm has invested in adjacent companies, the partner has spoken publicly about the space, and a warm intro path exists. Pursue first.
- **Tier 2**: Matches on 4-5 criteria. Good fit on stage and sector but may lack a warm path or have a slightly mismatched check size. Pursue in the second wave.
- **Tier 3**: Matches on 3 criteria. Acceptable as backfill if the round needs more participants. Do not spend significant time here until Tier 1 and 2 are exhausted.

### Sourcing Investor Information

- **Crunchbase / PitchBook**: Fund size, recent investments, portfolio companies.
- **Firm website**: Stated thesis, partner bios, blog posts that reveal focus areas.
- **Twitter/X and Substack**: Many partners publish their current interests publicly. Recent posts are a better signal than old "About" pages.
- **SEC filings**: Fund size from Form D filings when not publicly disclosed.
- **Portfolio founder back-channels**: The single best diligence on an investor is talking to founders they have backed — both successes and companies that struggled.

### Common Mistakes to Avoid

- **Spraying 200 cold emails** — Fundraising is a funnel. 30 well-targeted, well-introduced conversations beat 200 cold ones.
- **Ignoring portfolio conflicts** — Founders waste weeks pitching firms that will never invest because of a conflict.
- **Pitching the wrong partner** — At multi-partner firms, the wrong partner will say "interesting, let me introduce you to my colleague" at best, or just pass.
- **Targeting only brand-name firms** — Tier 2 and emerging funds are often faster to decide, more founder-friendly, and more willing to lead at earlier stages.
- **Not tracking your pipeline** — Use a simple spreadsheet or CRM: investor name, status (researching / intro requested / meeting scheduled / pitched / passed / term sheet), and next action.

### Angel Investor Considerations

- Angels decide faster (days, not weeks) but write smaller checks ($25K-$250K typically).
- Look for angels with operational experience in your sector — they add value beyond capital.
- Angel syndicates (AngelList, etc.) can aggregate small checks into a meaningful allocation.
- Be cautious about taking angel money from potential acquirers or competitors without understanding the signaling implications.
