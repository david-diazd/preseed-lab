# preseed-lab — Claude Code Fundraising Assistant (Pre-Seed)

Herramienta para ayudar a founders a preparar su ronda Pre-Seed mediante agentes especializados en Claude Code.

---

## Estructura del repositorio

```
/inputs        → Documentos del usuario (ejemplos incluidos; PDFs y XLSXs gitignored)
/outputs       → Resultados generados por los agentes (gitignored)
/use-cases     → Flujos de prompts listos para usar
/VC-agent      → Motor de agentes
  /agents      → 11 agentes especializados
  /profiles    → 3 perfiles de feedback (Friendly Mentor, Brutal VC, Operator)
  /templates   → Plantillas de pitch deck, modelo financiero y preguntas de inversores
  /related-info → Investigación, recursos y referencias
README.md      → Documentación principal
```

El usuario corre `claude` desde la raíz del repo. Las referencias a agentes usan `@VC-agent/agents/...` y `@VC-agent/profiles/...`. Los paths `inputs/` y `outputs/` resuelven desde la raíz.

---

## Agentes disponibles

| Archivo | Función |
|---|---|
| `agents/pitch-deck-analyst.md` | Narrativa, estructura, storytelling |
| `agents/market-analyst.md` | TAM/SAM/SOM, competencia, timing |
| `agents/financial-analyst.md` | Unit economics, proyecciones, burn rate |
| `agents/vc-partner.md` | Simulación de decisión inversora |
| `agents/growth-expert.md` | GTM, tracción, estrategias de crecimiento |
| `agents/founder-validator.md` | Validación del equipo (web search) |
| `agents/competitive-intelligence.md` | Landscape competitivo real (web search) |
| `agents/market-validator.md` | Fact-check de claims de mercado (web search) |
| `agents/checklist-evaluator.md` | Checklist de readiness Pre-Seed (10 criterios) |
| `agents/global-scorer.md` | Score global ponderado + detección de deal-breakers |
| `agents/vc-qa-simulator.md` | Simulación de reunión con inversor |

---

## Flujo de uso

1. El usuario sube sus documentos a `VC-agent/inputs/`
2. Abre Claude Code desde `VC-agent/`
3. Ejecuta los agentes con `@agents/<nombre>.md`
4. Los resultados se guardan en `VC-agent/outputs/`

---

## Contexto

Parte de **Startup Canarias** — iniciativa para impulsar el ecosistema emprendedor en Canarias.
