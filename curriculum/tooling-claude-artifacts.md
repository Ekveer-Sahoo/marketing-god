# Tooling: Claude Artifacts as marketing-plan outputs

Source: reel `sources/instagram-DfoJY0rAqzU` (Griffin Wooldridge, 2026-11-12) + verified on our account
(2026-11-17): Whiteboard, Sheets, Data, Docs, Slides, Design, Design System types all available.

## Core idea
A marketing plan is not one document. It's three jobs, and each fits a different artifact:

| Job | Artifact | What the plugin should put in it |
|---|---|---|
| **Think / plan** | Whiteboard | Campaign map: audience → awareness level → angle → hook → format → channel. Launch timeline. Funnel stages. Things people rearrange together. |
| **Execute / track** | Sheets | Content calendar, ad test matrix (angle × hook × format), creative tracker, budget, lab scoreboard. Formulas for CPA/ROAS. |
| **Measure / learn** | Data | Results dashboard: hook rate, CTR, CPA, ROAS per creative; "what won and why" story. |
| Write-up / brief | Docs | Positioning doc, creative brief, campaign brief for a team. |
| Pitch | Slides | Strategy deck for a client or stakeholder. |
| Make assets | Design | Static ads, landing page mockups, social posts. |

The reel's own example is the whole loop: "plan a launch, track the tasks, make sense of the results."
That maps 1:1 to our lab loop (brief → run → score → learn).

## Why it matters for the plugin
- Output a marketing plan as a **connected set** (board + tracker + dashboard), not a wall of chat text.
- Plans stay editable by a team, so the plugin's work survives beyond the chat.
- The Data dashboard is the feedback loop: real numbers decide which angles/hooks we keep.

## Open questions (to learn properly before writing the skill)
- What actually goes in a marketing plan? (We still need a real source on plan structure:
  objectives, ICP, positioning, offer, channels, budget, KPIs, timeline.)
- How the three artifacts link to each other in practice (reel's own open question).
