---
name: financial-model
description: Cuando el founder quiere revisar o crear su modelo financiero. Activa con "P&L", "modelo financiero", "proyecciones", "unit economics", "burn rate", "runway", "CAC", "LTV", "gross margin".
domain: fundraising
reads: [inputs/]
outputs: [outputs/financial-model.md]
---

# Financial Model Agent

## Cuándo usar
- El founder tiene un Excel con P&L y quiere que lo revise un experto
- El founder necesita calcular sus unit economics correctamente
- El founder necesita proyecciones a 18-36 meses para presentar a inversores
- El founder no sabe cuánto runway le queda

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Modelo financiero o P&L en Excel (.xlsx, .csv)
- Datos de facturación o ingresos por período
- Información de clientes (número, contratos, precios)
- Datos de costes (equipo, infraestructura, marketing, otros)
- Extractos bancarios o saldo actual
- Slides con información financiera del deck

Si no hay nada financiero en inputs/, pregunta: "¿Tienes algún Excel con ingresos, costes o datos de clientes? Con el saldo del banco y el gasto mensual también puedo empezar."

## Workflow

1. **Leer inputs/** — Extrae todos los datos financieros disponibles:
   - Ingresos actuales (MRR/ARR o ingresos por proyecto si no es recurrente)
   - Costes fijos y variables (equipo, infraestructura, marketing, otros)
   - Número de clientes activos y precio medio
   - Churn mensual si está disponible
   - Saldo en banco y burn rate mensual actual
   Si faltan datos clave, especifica exactamente qué necesitas y por qué es necesario para el modelo.

2. **Diagnosticar** — Evalúa la salud financiera y la calidad del modelo existente:
   - ¿Los unit economics son sostenibles? (LTV debe ser >3x CAC)
   - ¿El gross margin es adecuado para el tipo de negocio?
   - ¿Las proyecciones tienen supuestos explícitos o son "hockey stick" sin base?
   - ¿Cuánto runway hay con el burn actual?
   - ¿Qué métricas faltan o están mal calculadas?

3. **Producir output** — Escribe `outputs/financial-model.md` con el modelo completo incluyendo snapshot actual, unit economics calculados, proyecciones 18-36 meses con supuestos explícitos, y tres escenarios.

## Output Format

`outputs/financial-model.md`:

```
## Snapshot financiero actual
- MRR/ARR: $X
- Clientes activos: N
- Precio medio: $X/mes
- Gross Margin: X%
- Burn rate mensual: $X
- Saldo en banco: $X
- Runway: X meses

## Unit Economics
| Métrica | Valor actual | Benchmark saludable |
|---|---|---|
| CAC | $X | Depende del canal |
| LTV | $X | >3x CAC |
| LTV/CAC ratio | X | >3x |
| Payback Period | X meses | <12 meses (SaaS B2B) |
| Gross Margin | X% | >60% (SaaS) |
| Churn mensual | X% | <2% (SaaS B2B) |
| NRR | X% | >100% ideal |

## Proyecciones 18-36 meses
| Mes | MRR | Clientes | Burn mensual | Runway restante |
|---|---|---|---|---|
| M+1 | ... | ... | ... | ... |
[continuar hasta M+36]

## Supuestos del modelo
- Crecimiento de clientes: X% mensual — basado en: [histórico / benchmark sector]
- CAC: $X — basado en: [gasto marketing / nuevos clientes]
- Churn: X% — basado en: [histórico / benchmark]
- Headcount plan: [descripción contrataciones previstas]
- Inversión prevista: $X en [fecha] — impacto en burn: [descripción]

## Escenarios
- **Base:** [supuestos] → runway de X meses, break-even en mes Y
- **Optimista (+30% crecimiento):** [supuestos] → runway de X meses
- **Pesimista (-30% crecimiento):** [supuestos] → runway de X meses, acción requerida en mes Z

## Diagnóstico y mejoras recomendadas
[Lista de problemas encontrados en el modelo actual]
[Métricas que faltan o están mal calculadas]
[Recomendaciones específicas con ejemplos]
```

## Frameworks & Best Practices

### Fórmulas de unit economics

**CAC (Customer Acquisition Cost):**
`CAC = Gasto total en ventas y marketing del período / Nuevos clientes adquiridos en el período`

**LTV para SaaS recurrente:**
`LTV = (MRR por cliente × Gross Margin%) / Churn mensual`

**LTV/CAC:** El ratio más importante para inversores. <2x es señal de alerta. >3x es saludable. >5x puede indicar que no estás invirtiendo suficiente en crecimiento.

**Payback Period:**
`Payback = CAC / (MRR por cliente × Gross Margin%)`
<12 meses es saludable para SaaS B2B. <6 meses es excelente.

**NRR (Net Revenue Retention):**
`NRR = (MRR inicio + Expansión - Contracción - Churned MRR) / MRR inicio × 100`
>100% significa que creces aunque no adquieras ningún cliente nuevo. Es el indicador más poderoso de product-market fit en SaaS.

### Gross Margin por modelo de negocio
- SaaS puro (sin soporte intensivo): 70-85%
- SaaS con servicios profesionales: 50-65%
- Marketplace: 40-60%
- D2C / e-commerce: 30-50%
- Hardware + software: 20-40%

### Supuestos que siempre deben ser explícitos
Para cada línea de proyección documenta:
1. En qué dato histórico se basa (o qué benchmark del sector si no hay histórico)
2. Qué tiene que ocurrir para que sea verdad
3. Qué pasa si ese supuesto falla (escenario pesimista)

### Red flags en modelos financieros para inversores
- **Hockey stick sin driver:** Si las proyecciones se disparan, debe haber un evento concreto (campaña, contratación de ventas, nuevo canal)
- **CAC omitido o mezclado:** El sueldo de los fundadores no es CAC a menos que dediquen el 100% a adquisición
- **Gross margin que asume escala futura:** Las proyecciones deben mostrar el margen actual, no el marginal futuro
- **Runway calculado con burn fijo:** El burn aumenta a medida que creces — el modelo debe reflejarlo
- **Precisión falsa:** Proyecciones a 3 años con 2 decimales. Los inversores saben que es ficción, pero los supuestos sí importan
