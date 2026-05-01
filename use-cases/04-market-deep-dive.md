# Use case: Market Deep Dive

Validate your market claims from multiple angles — sizing, competition, and external fact-checking.

**When to use:** Your TAM/SAM/SOM story feels weak, or you want to make sure your market claims hold up to investor scrutiny.

**Time:** ~10 min · **Requires:** Web search enabled in Claude Code.

---

## Step 1 — Internal market analysis

```
@VC-agent/agents/market-analyst.md @VC-agent/profiles/brutal-vc.md

Analyze the market using all documents in inputs/ and save the result to outputs/market_analysis.md
```

## Step 2 — Competitive intelligence (live web research)

```
@VC-agent/agents/competitive-intelligence.md

Research the competitive landscape for my startup using inputs/ as context.
Save the result to outputs/competitive_analysis.md
```

## Step 3 — Market validation (fact-check against external sources)

```
@VC-agent/agents/market-validator.md

Fact-check the market claims in inputs/ and outputs/market_analysis.md against external sources.
Save the result to outputs/market_validation.md
```

---

**What to look for:** The Market Analyst evaluates your TAM methodology and segmentation. The Competitive Intelligence agent goes online to find actual competitors, their funding, traction, and positioning — including ones you may have missed. The Market Validator cross-checks your numbers against real sources and flags anything that won't survive investor due diligence.

**Outputs generated:** `market_analysis.md` · `competitive_analysis.md` · `market_validation.md`
