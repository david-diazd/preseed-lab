# Template: Pre-Seed Financial Model

Guide to building a credible financial model at Pre-Seed stage. Includes the key metrics and how to calculate them.

---

## 1. Unit Economics

The most important metrics for any investor. Calculate these first.

### CAC — Customer Acquisition Cost
```
CAC = Total sales & marketing spend / Number of new customers acquired
```
- Includes: sales salaries, tools, advertising, events
- Calculate per channel if you have multiple
- SaaS B2B benchmark: $200-$2,000 depending on ticket size

### LTV — Lifetime Value
```
LTV = Monthly ARPU × Gross margin × (1 / Monthly churn)
```
- ARPU: average revenue per user/month
- Gross margin: typically 70-85% in SaaS
- Churn: % of customers who cancel each month

### LTV:CAC Ratio
```
LTV:CAC = LTV / CAC
```
- >3x: healthy
- 1x-3x: concerning, review
- <1x: the business destroys value

### Payback Period
```
Payback = CAC / (ARPU × Gross margin)
```
- <12 months: good for early stage
- >18 months: hard to finance without external capital

### Monthly churn
```
Monthly churn = Customers lost in the month / Customers at the start of the month
```
- <1%: excellent
- 1-2%: good
- 2-5%: acceptable at early stage
- >5%: red flag — product or fit problem

---

## 2. Revenue projection (36 months)

### Base assumptions (fill these in)
| Assumption | Month 1 | Month 6 | Month 12 | Month 24 | Month 36 |
|---|---|---|---|---|---|
| New customers/month | | | | | |
| Average price ($/month) | | | | | |
| Monthly churn (%) | | | | | |
| Total active customers | | | | | |
| MRR ($) | | | | | |
| ARR ($) | | | | | |

### Active customers formula
```
Customers month N = Customers month N-1 + New customers - (Customers month N-1 × Churn)
```

---

## 3. Cost structure

### Headcount (largest line item)
| Role | Gross salary/month | Start | Total cost year 1 |
|---|---|---|---|
| CEO (founder) | $0 / $X post-round | Month 1 | |
| CTO (founder) | $0 / $X post-round | Month 1 | |
| [Next hire] | | Month X | |

### Other fixed costs/month
| Category | $/month |
|---|---|
| Infrastructure (AWS, etc.) | |
| SaaS tools | |
| Office / coworking | |
| Legal and accounting | |
| **Total fixed** | |

### Variable costs (scale with customers)
| Category | $/customer/month |
|---|---|
| Variable infrastructure | |
| Support | |
| **Total variable** | |

---

## 4. Burn rate and runway

```
Monthly burn rate = Total costs - Revenue
Runway (months) = Available cash / Monthly burn rate
```

### Burn table (fill in)
| Month | Revenue | Costs | Net burn | Cumulative cash |
|---|---|---|---|---|
| 0 (pre-round) | | | | |
| 1 | | | | |
| 3 | | | | |
| 6 | | | | |
| 12 | | | | |
| 18 | | | | |

---

## 5. Use of capital

Describe how you will use the round you are raising:

| Category | % of total | $ |
|---|---|---|
| Team (hires) | | |
| Product / technology | | |
| Marketing and sales | | |
| Operations | | |
| Buffer / contingency | | |
| **Total** | 100% | |

---

## 6. Milestone with the round

Define what you will achieve with this capital before needing the next round:

- **Primary milestone:** [e.g. "reach $XX MRR with YY active customers"]
- **Target date:** [month/year]
- **Why this milestone unlocks the next round:** [explanation]

---

## Notes for founders

1. **Investors don't believe projections** — they use them to understand your assumptions and business logic.
2. **Show the reasoning**, not just the numbers. A justified assumption is worth more than a big figure.
3. **Be conservative** on revenue and aggressive on costs to show discipline.
4. **Update the model monthly** — investors ask for the latest model, not the one from the initial pitch.
5. **Build three scenarios:** base, optimistic, and pessimistic. Show that you've thought about the risks.
