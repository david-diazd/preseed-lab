<p align="center">
  <img src="VC-agent/public/logo.png" alt="preseed-lab" width="300" />
</p>

<h1 align="center">preseed-lab</h1>

<p align="center">
  AI-powered toolkit to help founders build, launch, and fundraise their Pre-Seed startup.<br/>
  62 specialized agents across CEO, CTO, and CMO roles — plus 11 VC simulation agents that give you honest investor feedback before you're in the room.
</p>

<p align="center">
  <a href="#quick-start">Get started</a> ·
  <a href="#agents-by-role">See all agents</a> ·
  <a href="VC-agent/templates/pitch-deck-template.md">Pitch deck template</a> ·
  <a href="VC-agent/templates/financial-model-template.md">Financial model</a>
</p>

<p align="center">
  Part of <strong>Startup Canarias</strong> — boosting the entrepreneurial ecosystem in the Canary Islands.
</p>

---

## What is this?

**preseed-lab** is a clonable repo that runs specialized AI agents (via Claude Code) to help you with every aspect of building a Pre-Seed startup — from strategy and product to marketing and fundraising.

Three role-based suites (**CEO**, **CTO**, **CMO**) cover the operational side, while **VC-agent** simulates the feedback a real investor would give you — before you're actually in the room.

No servers. No accounts. Just `git clone` and `claude`.

---

## Agents by role

### CEO — Strategy, Fundraising, Legal & Market (24 agents)

| Domain | Agents | What they do |
|---|---|---|
| **Fundraising** (9) | pitch-deck, financial-model, data-room, investor-research, fundraising-email, accelerator-application, board-update, market-research, competitive-analysis | Build your deck, model, data room, investor pipeline, and outreach |
| **Legal** (5) | contract-review, terms-of-service, privacy-policy, process-docs, proposal-generation | Contracts, ToS, privacy policies, SOPs, and commercial proposals |
| **Strategy** (6) | vision-mission, okr-planning, business-model-canvas, hiring-plan, cap-table, term-sheet-review | Vision, OKRs, business model, hiring, cap table, and term sheets |
| **Market** (4) | market-sizing, industry-analysis, customer-discovery, market-entry | TAM/SAM/SOM, industry analysis, customer discovery, market entry |

### CTO — Product, Engineering & Technology (13 agents)

| Domain | Agents | What they do |
|---|---|---|
| **Product** (5) | prd-writing, mvp-scoping, roadmap-planning, user-research-synthesis, feedback-synthesis | PRDs, MVP scoping, roadmaps, user research, and feedback analysis |
| **Engineering** (8) | architecture-review, tech-stack-evaluation, technical-debt, api-design, security-checklist, devops-setup, scalability-plan, technical-due-diligence | Architecture, stack evaluation, APIs, security, DevOps, and scalability |

### CMO — Marketing, Growth & Brand (14 agents)

| Domain | Agents | What they do |
|---|---|---|
| **Marketing** (7) | content-strategy, launch-strategy, landing-page, cold-outreach, sales-script, social-content, seo-technical | Content, launch plans, landing pages, outreach, sales scripts, SEO |
| **Growth** (4) | growth-model, analytics-setup, pricing-strategy, partnership-strategy | Growth loops, analytics, pricing, and partnerships |
| **Brand** (3) | brand-positioning, messaging-framework, paid-ads-plan | Positioning, messaging, and paid acquisition |

### VC-agent — Investor Simulation (11 agents)

| Agent | Analyzes | Data source |
|---|---|---|
| **Pitch Deck Analyst** | Narrative, structure, clarity, storytelling | Your documents |
| **Market Analyst** | TAM/SAM/SOM, competition, timing | Your documents |
| **Financial Analyst** | Unit economics, projections, burn rate | Your documents |
| **VC Partner** | Investment decision simulation, deal-breakers | Your documents |
| **Growth Expert** | GTM strategy, traction, growth levers | Your documents |
| **Founder Validator** | Team authority, track record, credibility | Web search |
| **Competitive Intelligence** | Real competitor landscape, funding, traction | Web search |
| **Market Validator** | Fact-checks your market claims against real data | Web search |
| **Checklist Evaluator** | Pre-Seed readiness across 10 criteria | Your documents |
| **Global Scorer** | Weighted global score + deal-breaker detection | Agent outputs |
| **VC Q&A Simulator** | Interactive investor meeting simulation | Your documents + agent outputs |

---

## Skills

Reusable workflows that chain multiple agents or provide structured outputs:

| Scope | Skills |
|---|---|
| **Shared** (5) | weekly-report, swot-analysis, decision-framework, meeting-notes, competitor-monitor |
| **CEO** (4) | fundraising-pipeline, board-meeting-prep, investor-update, strategic-review |
| **CTO** (4) | sprint-planning, incident-postmortem, tech-radar, architecture-decision-record |
| **CMO** (4) | campaign-launch, content-calendar, performance-report, ab-test-analysis |

---

## Feedback profiles

Each VC-agent adapts its tone to the profile you choose:

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
git clone https://github.com/david-diazd/preseed-lab.git
cd preseed-lab
```

### 2. Add your documents

`inputs/` already has example files showing the expected format. Replace them with your own:

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

Then reference the agent you want to use:

**CEO — Improve your pitch deck:**
```
@CEO/agents/fundraising/pitch-deck.md

Review my pitch deck using inputs/ and save to outputs/pitch_deck_review.md
```

**CTO — Scope your MVP:**
```
@CTO/agents/product/mvp-scoping.md

Help me scope our MVP using inputs/ and save to outputs/mvp_scope.md
```

**CMO — Plan your launch:**
```
@CMO/agents/marketing/launch-strategy.md

Create a launch strategy using inputs/ and save to outputs/launch_plan.md
```

**VC — Simulate an investor meeting:**
```
@VC-agent/agents/vc-qa-simulator.md @VC-agent/profiles/brutal-vc.md

Run a Q&A simulation using inputs/ and outputs/ and save to outputs/qa_simulation.md
```

See all available workflows in [`/use-cases`](use-cases/).

### 4. Review results

Each output includes structured analysis with diagnosis, key findings, recommendations, and scores where applicable.

The VC-agent **Global Scorer** adds deal-breaker detection — if any hard blockers are found, it tells you exactly what to fix before talking to investors.

### Tips

- **Building?** Start with CTO agents (MVP scoping → architecture → roadmap).
- **Fundraising?** Start with CEO agents (market sizing → pitch deck → financial model → data room).
- **Launching?** Start with CMO agents (brand positioning → messaging → launch strategy).
- **Meeting investors?** Run VC-agent agents, then Global Scorer, then Q&A Simulator last.
- Use **Brutal VC** profile when you feel ready; start with **Friendly Mentor** for your first pass.
- Re-run agents after making changes to track improvement over time.

---

## Repository structure

```
/inputs        → Add your documents here (examples included)
/outputs       → Analysis results saved here (gitignored)
/CEO           → 24 agents + 4 skills (strategy, fundraising, legal, market)
/CTO           → 13 agents + 4 skills (product, engineering)
/CMO           → 14 agents + 4 skills (marketing, growth, brand)
/skills        → 5 shared skills (weekly report, SWOT, decisions, meetings, competitors)
/VC-agent      → 11 investor simulation agents + 3 feedback profiles + templates
/use-cases     → Ready-to-use prompt workflows
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
