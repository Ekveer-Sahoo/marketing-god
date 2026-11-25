# Skill smoke tests

Blind runs: a fresh agent reads only the skill files and uses them on a sample product, then critiques the skill. These check that the
instructions work; they are not lab runs (no real product, no rubric scoring by us, no real results). Sample customer messages were invented.

| # | Date | Skill(s) | Sample product | Output quality | Gaps found | Fixed in |
|---|---|---|---|---|---|---|
| 1 | 2026-11-25 | hooks | Electroplated custom keychains, ₹499, Instagram DMs | Good: "Plastic in. Real copper finish out." | 8 | e446408 |
| 2 | 2026-11-25 | audience-research | Same, with 10 sample DMs | Sensible; honest about 2-of-10 counts | 8 | 624cd83 |
| 3 | 2026-11-25 | audience-research → hooks (chained) | Weekend drone workshop for classes 7-10, ₹2,999, parent buys | Good; none of the 16 earlier gaps recurred | 7 | 44ab8d2 |
| 4 | 2026-11-25 | ad-matrix (reading audience.md + hooks rules) | Same drone workshop; Rs 500/day for two weeks, 8 ads, first-time advertiser | Good: 4 concepts, 6 live + 2 held ads; caught that the batch dates were Sunday-Monday | 7 | bec1a5e |
| 5 | 2026-11-25 | video-ads (with live Higgsfield connector, read-only calls only) | Keychains; seller asks to AI-generate the plating-tank footage they can't film | Good: refused to fake the tank, built a 20 s reel from real pieces, quoted 12 credits for one optional draft, generated nothing | 7 | c8074c4 |

## Gaps by test
**1 (hooks):** audience fallback size contradicted itself · rubric penalised demo hooks · templates skewed to creators · goal collected but
unused · score mode underspecified · three different banned-opener lists · delivery format ambiguous · no rule on product-claim honesty.

**2 (audience-research):** evidence mix counted lines not sources · no tag for inference · paraphrases looked like quotes · same finding
repeated across parts · template and steps disagreed · no thin-sample handling · seller facts never asked · path and draft-notice gaps.

**3 (chained):** seller facts assumed a shipped product · "problems" were really objections, pushing hooks toward objection-handling ·
hooks ignored seller unknowns and the draft notice · no permission rule for reusing customer messages · buyer-vs-user dropped in hooks
(language drifted to the child's register) · no testimonial or own-footage anticipation type · self-scores bunched at 9-11.

**4 (ad-matrix):** capacity vs hook minimum vs "wave" contradicted each other · static hook variants weren't different ads · no campaign-setup
scope statement, so setup steps were improvised · no way to derive a cut rule or break-even · ID scheme and CSV columns had holes · hand-offs
undefined (updating audience.md, stale facts, date checks, which hooks-skill steps to skip) · no consent rule for people (children) in footage.

**5 (video-ads):** no fallback when proof can't be filmed · stylised-process boundary undefined · no "generate nothing" exit · hand-off to
higgsfield-expert unscoped, and the connector's one-click whole-ad option not addressed · quoting gaps (files not collected first, finishing
unpriced) · user-supplied hook and its claims never checked · AI-label rule asserted from memory, a recipe name that didn't exist.

## Still untested
- Either skill with web search on (public voice-of-customer step).
- Either skill loaded as an installed plugin (triggering from the description).
- ad-matrix after its fixes; the "one winner into variations" path; any real ad account data.
- video-ads beyond one draft: a first clip was generated and reviewed (`lab/video-tests/0001-drone-draft/notes.md`, 12 credits,
  unusable: third-party logo became readable, ending wrong), but no retry, final-quality pass, assembly, captions or real product yet.
- Text formats (LinkedIn post, email subject, landing headline) and paid-ad hooks.
- Whether the scoring rubric predicts real performance: needs the lab and real numbers.
