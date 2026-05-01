# Use case: Pitch Deck Review

Deep focus on narrative, storytelling, and first impression — then stress-test it with a simulated investor.

**When to use:** You have a pitch deck ready (or almost ready) and want to pressure-test it before sending to real VCs.

**Time:** ~8 min · **Profile recommended:** Brutal VC.

---

## Step 1 — Narrative analysis

```
@VC-agent/agents/pitch-deck-analyst.md @VC-agent/profiles/brutal-vc.md

Analyze my pitch deck at inputs/pitch_deck.pdf and all supporting documents in inputs/
Save the result to outputs/pitch_analysis.md
```

## Step 2 — Investor simulation

```
@VC-agent/agents/vc-partner.md @VC-agent/profiles/brutal-vc.md

Simulate an investment decision based on inputs/pitch_deck.pdf and all documents in inputs/
Save the result to outputs/vc_analysis.md
```

## Step 3 — Q&A prep

```
@VC-agent/agents/vc-qa-simulator.md

Run a Q&A simulation based on inputs/ and outputs/pitch_analysis.md and outputs/vc_analysis.md
Save the result to outputs/qa_simulation.md
```

---

**What to look for:** The Pitch Deck Analyst focuses on structure, clarity, and storytelling. The VC Partner adds an investment lens — deal-breakers, missing signals, and likelihood of passing the first filter. The Q&A Simulator surfaces the 10 hardest questions an investor would ask based on your specific materials.

**Outputs generated:** `pitch_analysis.md` · `vc_analysis.md` · `qa_simulation.md`
