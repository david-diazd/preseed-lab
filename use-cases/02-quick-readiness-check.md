# Use case: Quick Readiness Check

A fast, structured pass to know where you stand before talking to investors.

**When to use:** You have a pitch deck and basic financials and want a clear yes/no on whether you're ready to raise — without running every agent.

**Time:** ~5 min · **Profile recommended:** Brutal VC.

---

## Run the checklist

```
@VC-agent/agents/checklist-evaluator.md

Evaluate my startup's Pre-Seed readiness using all documents in inputs/
and save the result to outputs/checklist_readiness.md
```

## Get the score

```
@VC-agent/agents/global-scorer.md

@outputs/checklist_readiness.md

Calculate the global score based on the checklist and save to outputs/global_score.md
```

---

**Read the output:** The checklist gives you a ✅ / ⚠ / ❌ for each of the 10 Pre-Seed criteria plus a verdict and the 3 most urgent things to fix. The global score adds deal-breaker detection — if any hard blockers appear, it tells you to stop and fix them before meeting investors.

**Outputs generated:** `checklist_readiness.md` · `global_score.md`
