<p align="center">
  <img src="VC-agent/public/logo.png" alt="preseed-lab" width="300" />
</p>

<h1 align="center">preseed-lab</h1>

<p align="center">
  AI-powered toolkit to help founders prepare and nail their Pre-Seed fundraising round.<br/>
  Specialized agents analyze your pitch deck, financials, market, team, and strategy — and give you honest, actionable feedback.
</p>

<p align="center">
  <a href="#quick-start">Get started</a> ·
  <a href="VC-agent/templates/pitch-deck-template.md">Pitch deck template</a> ·
  <a href="VC-agent/templates/financial-model-template.md">Financial model</a> ·
  <a href="VC-agent/templates/inputs">See examples</a>
</p>

<p align="center">
  Part of <strong>Startup Canarias</strong> — boosting the entrepreneurial ecosystem in the Canary Islands.
</p>

---

## What is this?

**preseed-lab** is a clonable repo that runs specialized AI agents (via Claude Code) to simulate the feedback a real investor would give you — before you're actually in the room.

Drop your pitch deck, financials, and team info. Run the agents. Get structured, honest feedback that helps you find and fix weaknesses before they cost you a deal.

No servers. No accounts. Just `git clone` and `claude`.

---

## Agents

Eleven specialized agents, each focused on a specific part of your startup:

| Agent | Analyzes | Data source |
|---|---|---|
| **Pitch Deck Analyst** | Narrative, structure, clarity, storytelling | Your documents |
| **Market Analyst** | TAM/SAM/SOM, competition, timing | Your documents |
| **Financial Analyst** | Unit economics, projections, burn rate | Your documents |
| **VC Partner** | Investment decision simulation, deal-breakers | Your documents |
| **Growth Expert** | GTM strategy, traction, growth levers | Your documents |
| **Founder Validator** | Team authority, track record, credibility | Web search (LinkedIn, X) |
| **Competitive Intelligence** | Real competitor landscape, funding, traction | Web search |
| **Market Validator** | Fact-checks your market claims against external sources | Web search |
| **Checklist Evaluator** | Pre-Seed readiness across 10 structured criteria | Your documents |
| **Global Scorer** | Weighted global score with automatic deal-breaker detection | Agent outputs |
| **VC Q&A Simulator** | Interactive investor meeting simulation with feedback | Your documents + agent outputs |

---

## Feedback profiles

Each agent adapts its tone to the profile you choose:

| Profile | Style |
|---|---|
| **Friendly Mentor** | Constructive, motivating, improvement-focused |
| **Brutal VC** | Direct, critical, no filters — like a real partner meeting |
| **Operator** | Practical, execution-focused, action-oriented |

---

## Quick start

### Prerequisites

- [Claude Code](https://docs.anthropic.com/claude-code) installed (`npm install -g @anthropic-ai/claude-code`)
- An Anthropic API key set as `ANTHROPIC_API_KEY`

### 1. Clone the repo

```bash
git clone https://github.com/your-username/preseed-lab.git
cd preseed-lab
```

### 2. Add your documents

`inputs/` already has example files showing the expected format for each document. Replace them with your own:

```
inputs/
  pitch_deck.md    ← or pitch_deck.pdf / .pptx
  financials.md    ← or financials.xlsx
  memo.md          ← investment memo
  team.md          ← team info for Founder Validator
  competitors.md   ← known competitors (optional)
```

### 3. Run an agent

```bash
claude
```

The [`/use-cases`](use-cases/) folder has ready-to-use prompts for every scenario. Copy and paste directly into Claude Code. For example:

**Quick readiness check:**
```
@VC-agent/agents/checklist-evaluator.md

Evaluate my startup's Pre-Seed readiness using all documents in inputs/
and save the result to outputs/checklist_readiness.md
```

**Simulate an investor meeting:**
```
@VC-agent/agents/vc-qa-simulator.md @VC-agent/profiles/brutal-vc.md

Run a Q&A simulation using inputs/ and outputs/ and save to outputs/qa_simulation.md
```

See all available workflows → [`/use-cases`](use-cases/)

### 4. Review results

Each output includes: diagnosis · main problems · recommendations · readiness score (1–10).

The **Global Scorer** adds deal-breaker detection — if any hard blockers are found, it stops and tells you exactly what to fix before talking to investors.

### Tips

- Run the specialized agents first, then **Global Scorer** for the full picture.
- Use **Brutal VC** profile when you feel ready; start with **Friendly Mentor** if it's your first pass.
- Run **VC Q&A Simulator** last — it's the closest thing to a real investor meeting.
- Re-run agents after making changes to track your improvement over time.
- The scoring is relative — use it to compare versions of your materials, not as an absolute measure.

---

## Use cases

Not sure where to start? Pick the workflow that fits your situation:

| Use case | When to use | Time |
|---|---|---|
| [Full analysis](VC-agent/use-cases/01-full-analysis.md) | First run or after major changes to your materials | ~20 min |
| [Quick readiness check](VC-agent/use-cases/02-quick-readiness-check.md) | Fast yes/no before talking to investors | ~5 min |
| [Pitch deck review](VC-agent/use-cases/03-pitch-deck-review.md) | Pressure-test your deck before sending to VCs | ~8 min |
| [Market deep dive](VC-agent/use-cases/04-market-deep-dive.md) | Validate TAM, competition, and market claims | ~10 min |
| [Investor meeting prep](VC-agent/use-cases/05-investor-meeting-prep.md) | Practice Q&A the day before a VC meeting | ~8 min |

---

## Repository structure

```
/inputs        → Add your documents here (examples included)
/outputs       → Analysis results saved here
/use-cases     → Ready-to-use prompt workflows — start here
/VC-agent      → Agent engine (no need to touch this)
  /agents      → 11 specialized agent prompts
  /profiles    → 3 feedback style profiles
  /templates   → Pitch deck, financial model, and investor question templates
  /related-info → Research, insights, and resources
README.md      → You are here
```

---

## Privacy

Binary files in `/inputs` (PDF, XLSX, DOCX...) and all files in `/outputs` are gitignored — your documents never leave your machine.

---

## Resources

Built using research from:
[Paul Graham](https://paulgraham.com/fr.html) · [Y Combinator](https://www.ycombinator.com/library) · [First Round Review](https://review.firstround.com) · [a16z](https://a16z.com) · [Venture Deals](https://www.amazon.com/dp/1119594820)

---

## License

MIT — clone it, fork it, adapt it.
