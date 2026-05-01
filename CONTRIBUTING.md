# Contributing to preseed-lab

Thanks for your interest! preseed-lab is a community project built to help founders prepare better for Pre-Seed fundraising. Every improvement helps real people walking into investor meetings.

---

## Ways to contribute

**Report a bug** — If an agent produces wrong, inconsistent, or misleading output, open an [Issue](https://github.com/david-diazd/preseed-lab/issues) and describe which agent you ran, what input you used (without sharing confidential data), and what you expected vs. what you got.

**Suggest an improvement** — Have an idea for a new agent, a better prompt, or a missing use case? Open an Issue with the label `enhancement` and explain the use case before building it.

**Submit a Pull Request** — See the steps below.

---

## Where things live

```
/VC-agent/agents      → Agent prompts — the core of the project
/VC-agent/profiles    → Feedback style profiles (Friendly Mentor, Brutal VC, Operator)
/VC-agent/templates   → Pitch deck, financial model, and investor question templates
/use-cases            → Step-by-step prompt workflows for common scenarios
/inputs               → Example input files (team.md, memo.md, etc.)
```

Most contributions will touch `agents/`, `use-cases/`, or `templates/`.

---

## How to submit a Pull Request

1. **Fork** this repo and clone your fork locally
2. **Create a branch** with a descriptive name:
   ```bash
   git checkout -b improve-vc-partner-agent
   ```
3. **Make your changes** — see the guidelines below
4. **Test your changes** before submitting (see Testing section)
5. **Commit** with a clear message:
   ```bash
   git commit -m "Improve VC Partner agent: add deal-breaker detection for missing moat"
   ```
6. **Push** to your fork and open a PR against `main`

All PRs are reviewed before merging. You'll receive feedback within a few days.

---

## What kinds of PRs are welcome

**Yes, please:**
- Improving existing agent prompts — better questions, more realistic VC logic, clearer output format
- Adding new use-case workflows (`use-cases/`)
- Adding or improving feedback profiles
- Fixing errors or outdated info in templates
- Adding example input files that show founders what good looks like
- Improving the README or documentation

**Not a good fit:**
- Real pitch decks, financials, or any identifying company data in examples
- Changes that require a server or third-party account to run
- Features outside the Pre-Seed fundraising scope
- Anything that breaks the local, privacy-first execution model

---

## Testing your changes

If you're modifying an agent, test it against one of the example inputs before submitting:

```bash
cd preseed-lab
claude
```

Then run the agent against `inputs/`:

```
@VC-agent/agents/<your-agent>.md

Analyze the documents in inputs/ and save the result to outputs/test_output.md
```

Check that the output follows the expected format defined at the bottom of the agent file. If you're adding a new use case, verify that every prompt in the workflow runs end-to-end without errors.

---

## Guidelines

- **Keep it founder-focused.** Every change should make the tool more useful for someone preparing a pitch.
- **No real company data.** Never include actual pitch decks, financials, or identifying information.
- **One thing per PR.** Smaller, focused PRs are easier to review and merge faster.
- **Be specific in your PR description.** Explain what you changed, why, and how you tested it.
- **Don't break existing use cases.** If you change an agent's output format, update the relevant use-case files too.

---

## Questions?

Open an [Issue](https://github.com/david-diazd/preseed-lab/issues) or start a Discussion. Happy to talk through ideas before you build them.

---

Part of **Startup Canarias** — boosting the entrepreneurial ecosystem in the Canary Islands.
