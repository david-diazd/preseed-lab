---
name: term-sheet-review
description: Cuando el founder recibe un term sheet y necesita analizarlo. Activa con "term sheet", "condiciones de inversión", "oferta de inversor", "liquidation preference", "anti-dilution", "drag-along".
domain: strategy
reads: [inputs/]
outputs: [outputs/term-sheet-review.md]
---

# Term Sheet Review Agent

## Cuándo usar
- El founder ha recibido un term sheet y necesita entenderlo antes de firmar
- El founder quiere comparar múltiples ofertas de inversores
- El founder quiere prepararse para negociar términos específicos

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Term sheet(s) recibido(s)
- Cap table actual
- SAFEs o convertibles existentes
- Notas de conversaciones con inversores

Si inputs/ está vacío, pregunta: "Pega el term sheet o describe los términos principales: valoración, monto, tipo de acciones, liquidation preference y cualquier cláusula especial."

## Workflow

1. **Leer inputs/** — Extrae: valoración (pre/post-money), monto de la ronda, tipo de acciones, liquidation preference, anti-dilution, board seats, vesting de founders, pro-rata rights, y cualquier cláusula inusual.

2. **Diagnosticar** — Clasifica cada término como: estándar (✅), negociable (⚠️), o red flag (🚨). Compara con benchmarks del mercado para stage y tamaño de ronda.

3. **Producir output** — Escribe `outputs/term-sheet-review.md` con análisis cláusula por cláusula, comparación con mercado, y estrategia de negociación.

## Output Format

`outputs/term-sheet-review.md`:

```
# Term Sheet Review — [Nombre Startup] — [Inversor]

## Resumen ejecutivo
[2-3 frases: ¿es un buen deal, un deal negociable o un deal problemático?]

## Análisis por cláusula

### Términos económicos
| Cláusula | Valor propuesto | Benchmark mercado | Evaluación | Nota |
|---|---|---|---|---|
| Valoración pre-money | | | ✅/⚠️/🚨 | |
| Monto de la ronda | | | | |
| Option pool | | | | |
| Liquidation preference | | | | |
| Participation | | | | |
| Anti-dilution | | | | |
| Dividends | | | | |

### Términos de control
| Cláusula | Valor propuesto | Benchmark mercado | Evaluación | Nota |
|---|---|---|---|---|
| Board composition | | | | |
| Protective provisions | | | | |
| Drag-along | | | | |
| Information rights | | | | |

### Términos de founder
| Cláusula | Valor propuesto | Benchmark mercado | Evaluación | Nota |
|---|---|---|---|---|
| Founder vesting | | | | |
| Non-compete | | | | |
| IP assignment | | | | |

## Comparación de ofertas (si hay múltiples)
| Término | Oferta A | Oferta B | Mejor para founder |
|---|---|---|---|

## Impacto en cap table
[Simulación de dilución con estos términos — referencia a cap-table agent]

## Estrategia de negociación
| Cláusula a negociar | Posición actual | Posición deseada | Argumento |
|---|---|---|---|

## Cláusulas que necesitan abogado
[Lista de términos donde se recomienda asesoría legal profesional]
```

## Frameworks & Best Practices

- **1x non-participating liquidation preference is standard.** Anything above 1x (2x, 3x) or participating preferred is aggressive. At pre-seed, push back firmly on participating preferred.
- **Broad-based weighted average anti-dilution is standard.** Full ratchet anti-dilution is a red flag — it means if you raise a down round, the investor's conversion price drops to the new price, causing massive dilution.
- **Board composition matters more than it seems.** At pre-seed, a 3-person board (2 founders + 1 investor) is common. Avoid giving up board control before Series A. A 2-1-1 (2 founders, 1 investor, 1 independent) is also acceptable.
- **Protective provisions are the real control.** Even without board control, investors can block key decisions through protective provisions. Review what requires investor approval: new fundraising, M&A, changing the business, increasing option pool.
- **Founder vesting resets are negotiable.** If you've been working for 2 years before raising, don't accept a full 4-year vesting reset. Negotiate credit for time served.
- **Pay-to-play protects founders.** This clause requires investors to participate in future rounds to keep their preferred status. It protects against investors who block future fundraising.
- **Non-competes should be narrow.** Geography-limited, time-limited (12 months max), and sector-specific. Broad non-competes that prevent you from working in your industry are unacceptable.
- **Always consult a lawyer.** This agent provides analysis and education, not legal advice. A startup lawyer costs $2-5K for term sheet review — the ROI is enormous.
