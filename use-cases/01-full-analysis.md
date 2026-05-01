# Use case: Full Pre-Seed Analysis

Run all specialized agents in sequence for a comprehensive diagnosis of your startup.

**When to use:** First time running preseed-lab, or when you've made significant changes to your materials.

**Time:** ~15–20 min · **Profile recommended:** Friendly Mentor first, Brutal VC after.

---

## Step 1 — Pitch deck

```
@VC-agent/agents/pitch-deck-analyst.md @VC-agent/profiles/friendly-mentor.md

Analyze my pitch deck and all documents in inputs/ and save the result to outputs/pitch_analysis.md
```

## Step 2 — Market

```
@VC-agent/agents/market-analyst.md @VC-agent/profiles/friendly-mentor.md

Analyze the market using all documents in inputs/ and save the result to outputs/market_analysis.md
```

## Step 3 — Financials

```
@VC-agent/agents/financial-analyst.md @VC-agent/profiles/friendly-mentor.md

Analyze the financials using all documents in inputs/ and save the result to outputs/financial_analysis.md
```

## Step 4 — VC perspective

```
@VC-agent/agents/vc-partner.md @VC-agent/profiles/brutal-vc.md

Simulate an investment decision using all documents in inputs/ and save the result to outputs/vc_analysis.md
```

## Step 5 — Growth & GTM

```
@VC-agent/agents/growth-expert.md @VC-agent/profiles/friendly-mentor.md

Analyze the go-to-market and growth strategy using all documents in inputs/ and save the result to outputs/growth_analysis.md
```

## Step 6 — Team validation

```
@VC-agent/agents/founder-validator.md

Validate the founding team using inputs/team.md and save the result to outputs/founder_validation.md
```

## Step 7 — Readiness checklist

```
@VC-agent/agents/checklist-evaluator.md

Evaluate my startup's Pre-Seed readiness using all documents in inputs/
and save the result to outputs/checklist_readiness.md
```

## Step 8 — Global score

```
@VC-agent/agents/global-scorer.md

@outputs/pitch_analysis.md @outputs/market_analysis.md
@outputs/financial_analysis.md @outputs/vc_analysis.md
@outputs/growth_analysis.md @outputs/founder_validation.md
@outputs/checklist_readiness.md

Calculate the global score and save to outputs/global_score.md
```

## Step 9 — Investor Q&A

```
@VC-agent/agents/vc-qa-simulator.md

Run a Q&A simulation using inputs/ and outputs/ and save to outputs/qa_simulation.md
```

---

**Outputs generated:** `pitch_analysis.md` · `market_analysis.md` · `financial_analysis.md` · `vc_analysis.md` · `growth_analysis.md` · `founder_validation.md` · `checklist_readiness.md` · `global_score.md` · `qa_simulation.md`
