# 05 · AI marketing workflow and what our plugin should do

Sources: reels ledger, esp. @aashrayy0, @jayantcreates.ai, @yapsbykhushi, @beingavii10, @harikesh.code, @will_debause, @doomy.ai,
@brainbiteshqq, @marketingwithnevaehh, @marketing.yatra, @raginirunsgrowth. Status: ideas, nothing built.

## The main lesson: research the audience before writing anything (@aashrayy0, 85k comments)
"90% of AI scripts" flop because people type idea + niche and ask for a script. Instead, make the model do audience research first:
- 10 common problems · 10 frustrations · 10 desired outcomes · 10 repeated questions · 10 common mistakes · 10 objections or limiting beliefs
- the emotional reasons behind those problems
- the phrases and language the audience actually uses

Then: pick the strongest problem → pick the best angle → rebuild the script around it → one CTA matched to the goal.
Inputs the prompt needs: niche, target audience (who, what they want, experience level, biggest struggles), raw idea, reel goal
(followers / comments / saves / shares / leads / authority / sales), length.

**For our plugin: every content or ad skill starts from a saved audience-research file for the product. No research file, no copy.**

## What others have already packaged (study these before building)
| Product (as described in the reel) | What it does | What to take |
|---|---|---|
| 3 Claude skills for reels (@jayantcreates.ai) | Hooks (rejects generic openers, "no tension in first 3 s", "doesn't filter your ideal client") · Script audit (Hook → Problem → Solution → Proof → CTA) · Voice (trained on your own writing) | The three-part split; voice is "the most important one" |
| "Hook Doctor" (@yapsbykhushi) | Scores a hook out of 10 with reasons ("no result", "no curiosity"), rewrites to 9/10 | A hook scorer with named failure reasons = our error taxonomy, live |
| 4-agent Meta ads squad (@beingavii10) | Scout (competitor ads) · Looter (3 new hooks per ad) · Sniper (message per segment) · Medic (kill losers, fund winners) | Agent roles |
| Claude Ads skill (@harikesh.code) | Audits Google/Meta/YouTube ad exports: wasted spend, competitor ads, new copy | Ads-audit skill fed by exported reports |
| Open-source marketing teardown (@will_debause) | One link → report on a company's ads, pixels, SEO, funnel, with evidence per claim | Competitor-teardown skill; "evidence behind every claim" |
| Vamos (@doomy.ai) | Watches reels in your niche, finds why your best one worked, drafts the next, learns from each post | The feedback loop from real results |
| Content Skills, 54 specialists (@brainbiteshqq) | Strategist, hook writer, scripter, editor, comment manager that DMs leads | Breadth; check for quality vs quantity |
| Ad-spy sites (@marketingwithnevaehh and others) | Any brand → its live Meta/TikTok ads, top hooks, angles, best organic posts | Research inputs; Meta Ad Library is the free version |

None of the reels showed proof these tools produce results; they're lead magnets. Our edge is the lab: rules that survived testing on 100+
products.

## Feature list this suggests (candidates, in build order)
1. `audience-research` — the 8-part research above, saved per product.
2. `hook-writer` + `hook-scorer` — generate from the swipe templates in `01-hooks.md`, score against the rubric, name the failure reason.
3. `script-audit` — Hook → Problem → Solution → Proof → CTA, plus one CTA matched to the goal.
4. `ad-matrix` — Hormozi's 50 hooks × 3-5 meats × 1-3 CTAs, across genuinely different formats from `03-ads.md`.
5. `competitor-teardown` — ads (Meta Ad Library), hooks, angles, funnel, with evidence.
6. `content-plan` — ideas tagged by job (reach / followers / leads), output as Whiteboard + Sheet (see `tooling-claude-artifacts.md`).
7. `video-recipes` — named prompt recipes for Higgsfield, in the spirit of @marketing.yatra's "codes" (storefront photo → fly-through reveal;
   assemble-from-pieces), plus the AI ad styles list.
8. `ads-audit` and `results-review` — read exported ad data, apply "judge by revenue", feed winners back into 2-4.
9. `voice` — learn the brand's own writing so output doesn't sound like AI.

## Video generation notes (for the Higgsfield module)
- A real photo of the real shop/product as the first frame makes AI video local and believable.
- Give recipes names; people remember "city FPV to storefront".
- Borrowed-suspense openers and "ad break" structure (see `01-hooks.md`) work with generated clips too.
- Skits with recurring 3D characters carried several of the best-performing reels; a consistent character is an asset.

## Tool notes for us
- `tools/reel.py` + `tools/digest.py` handle bulk study. Whisper (large-v3-turbo) is unreliable on Hindi/Hinglish: it dropped 30 s windows
  and garbled names. On-screen text and captions were the dependable source. To fix later: try the full large-v3 model for Hindi, or add OCR
  of frames.
- Image carousels can't be downloaded by yt-dlp; captions were read through the browser and slides by zooming.
