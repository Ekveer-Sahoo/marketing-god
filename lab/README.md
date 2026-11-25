# The Lab — learning loop

Every framework we learn gets tested against real products (target: 100+). Mistakes get logged,
tagged, counted, and turned into rules. The error rate per category should go down over time;
if it doesn't, the skill is wrong.

## The loop (one run = one product × one task)

1. **Brief** — product goes in `products/<slug>.md` (use `products/_template.md`).
2. **Generate** — run the plugin skill(s) on it (positioning, hooks, ad angles, script, video...).
3. **Score** — grade the output against `rubric.md`. Be harsh. Judge vs. what a top marketer would ship.
4. **Diagnose** — every miss gets an error tag from `error-taxonomy.md` (add new tags when needed).
5. **Log** — write `runs/NNNN-<slug>-<task>.md` (use `runs/_template.md`) and append a row to `scoreboard.csv`.
6. **Promote** — when an error tag shows up **3+ times across different products**, it becomes a rule
   in `learnings.md`, then gets written into the relevant skill. Note the run IDs as evidence.
7. **Re-test** — re-run the earlier failing products with the updated skill. Fixed? Keep the rule.
   Not fixed or broke something else? Revise or drop it.

## Files

| File | Purpose |
|---|---|
| `products/` | One brief per product |
| `runs/` | One file per test run: output, score, errors, fix |
| `rubric.md` | Scoring criteria (grows as we learn each topic) |
| `error-taxonomy.md` | Named, reusable error categories |
| `scoreboard.csv` | Machine-readable log for tracking error rates over time |
| `learnings.md` | Promoted rules with evidence, and where they went in the plugin |

## Principles

- **Real outcomes beat our opinion.** When a product has real data (CTR, hook rate, ROAS, sales),
  that overrides rubric scores.
- **Variety in products.** Mix B2C/B2B, cheap/expensive, impulse/considered, new/crowded markets,
  so rules generalize instead of overfitting to one niche.
- **No rule without evidence.** Every line in a skill should trace back to the curriculum or the lab.
