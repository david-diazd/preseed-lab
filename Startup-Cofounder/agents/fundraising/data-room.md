---
name: data-room
description: Cuando el founder quiere preparar el data room para due diligence. Activa con "data room", "due diligence", "DD", "documentos para inversores", "qué documentos necesito".
domain: fundraising
reads: [inputs/]
outputs: [outputs/data-room.md]
---

# Data Room Agent

## Cuándo usar
- Un inversor ha pedido materiales adicionales tras el pitch
- El founder quiere preparar el data room de forma proactiva antes de iniciar outreach
- El founder ha recibido un term sheet y necesita preparar due diligence confirmatorio

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Documentos corporativos (estatutos, actas de junta, pactos de socios)
- Cap table (Carta, Excel, o cualquier documento de equity)
- Documentos financieros (P&L, balance, cash flow, extractos bancarios)
- Contratos con clientes o proveedores clave
- Documentos legales (SAFEs, convertibles, contratos de empleados)
- Pitch deck o one-pager

Si inputs/ está vacío, pregunta: "¿En qué fase de due diligence estás — preparación previa, post-primera reunión, o post-term sheet?"

## Workflow

1. **Leer inputs/** — Escanea todos los archivos en inputs/. Identifica qué documentos corporativos, financieros y legales ya existen. Detecta cuáles están desactualizados (financieros >1 mes, 409A >12 meses) o incompletos.

2. **Diagnosticar** — Evalúa el estado de cada categoría del master DD checklist. Clasifica cada ítem como: Existe ✓ / Necesita actualización ⚠️ / Falta ✗ / No aplica —.

3. **Producir output** — Escribe `outputs/data-room.md` con el checklist completo por categoría, estado de cada documento, estructura de carpetas recomendada y drafts o templates para los documentos que faltan.

## Output Format

`outputs/data-room.md`:

```
## Data Room Checklist — [Nombre empresa] — [Ronda]

### 1. Documentos corporativos
- [✓/⚠️/✗/—] Escritura de constitución — [estado]
- [✓/⚠️/✗/—] Estatutos sociales — [estado]
...

### 2. Cap table & equity
...

[Una sección por cada categoría del master checklist]

## Estructura de carpetas recomendada
[Árbol de carpetas para organizar el data room]

## Documentos que faltan — drafts/templates
[Para cada documento marcado como ✗, incluir un template o borrador]
```

## Frameworks & Best Practices

### Master Due Diligence Checklist

**1. Documentos corporativos**: Escritura de constitución (y modificaciones), estatutos sociales, actas de junta de los últimos 12 meses, consentimiento del consejo para la ronda, pactos de socios, documentos de elegibilidad QSBS, registros estatales, litigios pendientes.

**2. Cap table & equity**: Cap table fully diluted (exportado de Carta/Pulley, no una hoja manual), plan de opciones y registro de concesiones, SAFEs/convertibles con sus condiciones, cap table pro forma post-ronda, valoración 409A vigente (<12 meses), historial de ventas secundarias.

**3. Financieros**: P&L, balance y cash flow — reales, últimos 12 meses (mensual). Saldo bancario y burn rate. Proyecciones a 18-36 meses con supuestos explícitos. Desglose de ingresos por cliente/cohorte. Unit economics (CAC, LTV, gross margin, payback). Aging de cuentas a cobrar/pagar. Deuda pendiente.

**4. Métricas & KPIs**: Dashboard mensual de KPIs (MRR/ARR, crecimiento, churn, NRR, DAU/MAU). Retención por cohorte. Pipeline de ventas (B2B) o embudo de conversión (B2C/PLG).

**5. Producto & tecnología**: Roadmap de producto (6-12 meses), resumen de arquitectura, confirmación de propiedad intelectual, patentes, auditoría de licencias open source, resumen SOC 2 o de seguridad.

**6. Contratos & clientes**: Contratos de los 10 principales clientes, análisis de concentración de clientes (<20% por cliente es ideal), contratos clave con proveedores y partners, cláusulas de exclusividad o no competencia, registro de churn.

**7. Equipo & RRHH**: Organigrama, bios de fundadores y empleados clave, contratos de trabajo (confirmar cesión de IP), contratos de freelances, resumen de concesión de opciones, disputas de RRHH, resumen de beneficios.

**8. Legal & compliance**: Política de privacidad y estado GDPR/LOPD, licencias regulatorias, marcas registradas, términos de servicio, seguros (D&O, E&O, ciberseguridad).

### Scoping por etapa

- **Pre-seed / Seed**: Foco en secciones 1, 2, 3 (más ligero — 3-6 meses de financieros) y 7 (equipo). Producto y legal pueden ser más superficiales. No tener 409A todavía es aceptable.
- **Serie A**: Todas las secciones esperadas. Financieros mensuales 12+ meses. Dashboard de métricas sólido. Cesión de IP en regla. 409A vigente obligatoria.
- **DD confirmatorio (post-term sheet)**: Todo lo anterior, más los documentos que solicite específicamente el abogado del inversor líder. La gobernanza corporativa se escrutará con más detalle.

### Estructura de carpetas recomendada

```
/01-Corporativo              /05-Producto-Tecnologia
/02-Cap-Table-Equity         /06-Contratos-Clientes
/03-Financieros              /07-Equipo-RRHH
/04-Metricas-KPIs            /08-Legal-Compliance
                             /09-Materiales-Pitch
```

### Control de acceso

- **Pre-term sheet**: Comparte materiales de pitch, dashboard de métricas, resumen financiero y bios del equipo. Retén contratos, cap table completo y documentos legales.
- **Post-term sheet**: Abre el data room completo. Exige NDA antes de compartir contratos con clientes o financieros detallados.
- Añade marca de agua a los PDFs con el nombre del inversor. Usa analíticas de enlace (DocSend) para rastrear qué se abre.

### Red flags que matan deals

- Inconsistencias en el cap table entre la tabla y los documentos firmados.
- Contratos de cesión de IP faltantes para freelances que construyeron el producto core.
- 409A desactualizada o ausente cuando se han concedido opciones.
- Estados financieros que no cuadran con los extractos bancarios.
- Vesting no estándar de los fundadores sin documentación de aprobación del consejo.
