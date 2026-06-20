---
name: cap-table
description: Cuando el founder necesita analizar, simular o preparar su cap table. Activa con "cap table", "dilución", "equity", "participaciones", "vesting", "SAFE", "valoración".
domain: strategy
reads: [inputs/]
outputs: [outputs/cap-table-analysis.md]
---

# Cap Table Analysis Agent

## Cuándo usar
- El founder va a cerrar una ronda y necesita entender la dilución
- El founder quiere simular escenarios de SAFE/priced round
- El founder necesita presentar su cap table a inversores o abogados

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Cap table actual (Excel, CSV o descripción)
- SAFEs o convertible notes firmados
- Term sheets recibidos
- Modelo financiero con valoraciones estimadas

Si inputs/ está vacío, pregunta: "¿Cuántos founders son, cómo se reparte el equity entre ellos, y han emitido SAFEs, notas convertibles o dado equity a alguien más?"

## Workflow

1. **Leer inputs/** — Extrae: distribución actual de equity entre founders, SAFEs/convertibles pendientes (con caps y descuentos), option pool existente, y cualquier ronda previa.

2. **Diagnosticar** — Evalúa: ¿la distribución entre founders es razonable?, ¿hay demasiados SAFEs acumulados?, ¿el option pool es suficiente?, ¿el founder entiende su dilución real post-conversión?

3. **Producir output** — Escribe `outputs/cap-table-analysis.md` con cap table actual, simulación post-ronda, y análisis de dilución.

## Output Format

`outputs/cap-table-analysis.md`:

```
# Cap Table Analysis — [Nombre Startup]

## Cap Table actual (pre-money)
| Accionista | Acciones/% | Tipo | Notas |
|---|---|---|---|
| Founder 1 | | Ordinarias | |
| Founder 2 | | Ordinarias | |
| Option Pool | | Reservadas | |
| SAFE 1 | | Convertible | Cap: $X, Descuento: Y% |
| Total | 100% | | |

## Instrumentos pendientes de conversión
| Instrumento | Monto | Cap | Descuento | Fecha | Conversión estimada |
|---|---|---|---|---|---|

## Simulación Post-Ronda
### Escenario: Ronda de $[X] a $[Y] pre-money
| Accionista | Pre-ronda % | Post-ronda % | Dilución |
|---|---|---|---|

## Análisis de dilución del founder
| Evento | % del Founder principal |
|---|---|
| Hoy | |
| Post-conversión SAFEs | |
| Post-ronda actual | |
| Post-Series A estimada | |

## Red flags y recomendaciones
- [Problemas detectados con acciones concretas]

## Glosario para el founder
[Términos usados en el análisis con explicación breve]
```

## Frameworks & Best Practices

- **Founders should own 50%+ post-seed.** If the founding team's ownership drops below 50% after seed, something is wrong — either too much dilution, too many SAFEs, or a bad split.
- **SAFE stacking is invisible dilution.** Multiple SAFEs with different caps create complex conversion waterfalls. Model every SAFE converting simultaneously to see the real dilution.
- **Option pool is negotiation leverage.** Investors want a bigger option pool (dilutes founders pre-money, not them). 10-15% is standard at pre-seed. Push back on 20%+ unless you have immediate senior hires planned.
- **Vesting protects everyone.** 4-year vesting with 1-year cliff is standard. Co-founders without vesting create catastrophic risk if one leaves early. This is non-negotiable.
- **Pro-rata rights matter long-term.** Investors with pro-rata rights in early rounds can maintain their ownership in later rounds. Understand who has pro-rata before your next raise.
- **Model 3 scenarios.** Best case (high valuation, small round), base case, worst case (lower valuation, larger round). Show the founder their ownership in each.
- **Post-money vs pre-money SAFEs.** Post-money SAFEs (YC standard since 2018) are cleaner but more dilutive to founders because the investor's percentage is fixed regardless of other SAFEs. Make sure founders understand which type they're signing.
- **Dead equity is a deal-breaker.** Large equity held by inactive founders, early advisors who don't contribute, or departed employees is a red flag for investors. Clean it up before fundraising.
