# Use case: Investor Meeting Prep

Validate your credibility as a founder and practice the hardest questions before you're in the room.

**When to use:** You have a first meeting with a VC in the next few days and want to go in prepared.

**Time:** ~8 min · **Requires:** `inputs/team.md` filled out + web search enabled for founder validation.

---

## Step 1 — Founder validation (live web research)

```
@VC-agent/agents/founder-validator.md

Validate the founding team using inputs/team.md and search online for additional context.
Save the result to outputs/founder_validation.md
```

## Step 2 — Investor Q&A simulation

```
@VC-agent/agents/vc-qa-simulator.md @VC-agent/profiles/brutal-vc.md

Run a Q&A simulation using all documents in inputs/ and outputs/founder_validation.md
Save the result to outputs/qa_simulation.md
```

---

**What to look for:** The Founder Validator searches online (LinkedIn, news, previous companies) to assess how you'll come across in investor due diligence — not just what you claim in the deck. The Q&A Simulator generates the 10 hardest investor questions specific to your startup, your answers, and feedback on how to improve them.

**Pro tip:** Run the Q&A Simulator twice — once with Friendly Mentor to understand what to say, once with Brutal VC to stress-test whether your answers hold up.

**Outputs generated:** `founder_validation.md` · `qa_simulation.md`
