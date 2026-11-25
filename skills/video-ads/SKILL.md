---
name: video-ads
description: Turn a hook, script or ad idea into a finished short marketing video (reel, short, TikTok or paid video ad): beat sheet, what to film versus what to generate with AI, which Higgsfield workflow or model to use, cost approval, draft review and finishing. Use when the user wants a reel or video ad made, an AI-generated ad or product video, UGC-style video, b-roll or a hook clip generated, a storefront or product photo turned into video, a video planned shot by shot, or asks which Higgsfield tool to use for a marketing video. Use it even when they only say "make the video" after hooks or an ad matrix exist.
---

# Video ads

This skill is the marketing layer on top of video generation. It decides **what the video must do and show**, splits it into real and
generated footage, and hands each generated piece to the right tool. It does not replace prompt-craft guidance: when a `higgsfield-expert`
skill is available, take **only model choice and prompt wording** from it; this skill's plan, rules and money gate govern, so don't
run that skill's own multi-step procedure unless the user asks for it. When the Higgsfield connector's own workflows cover the
deliverable, load and follow them inside the same rules.

Status: recipes come from `curriculum/` (creators' reels) and have not been through the lab. Tool and workflow names below were read from
the Higgsfield connector on 2026-11-25 and change over time: always list what's available first and trust the live list over this file.

## Rules that come before everything
1. **Generation costs the user's credits. Never generate without an explicit yes to a quoted cost.** Planning, listing workflows, checking
   the balance and getting quotes are free and need no permission.
2. **Real for proof, generated for attention.** Anything the viewer is asked to believe (the product, the result, a customer, a number)
   must be real footage, real photos or true on-screen text. Generate only what can't practically be filmed: an attention-getting opener,
   b-roll, transitions, stylised or animated scenes, a setting. **The seller's own process is proof**: don't generate a depiction of
   how the product is made, even stylised, unless it is unmistakably a graphic (an abstract wipe, a diagram) that nobody could take
   for footage. When the user asks for generated proof ("just AI the factory part"), say no, say why in one line, and offer the
   ladder in step 2.
3. **Never fabricate evidence.** No AI "customers" or testimonials presented as real, no generated before/after or results footage, no
   invented reviews on screen, no real person's face or voice without their consent. A generated product shot must show the product as
   it really looks; if the model changes its shape, colour, logo or finish, that take is unusable.
4. **Say what's AI when it matters.** Platforms have rules and a label for realistic AI-made content, and they change; don't quote the
   rule from memory. Tell the user which parts are generated and to check the platform's current labelling setting before posting.
5. **No one else's IP**: no named shows, characters, studios, brands or celebrity likenesses as a style. **Inspect every source image at
   full size before using it**: a stock or third-party photo of a branded product carries that brand into the video, and a camera move
   toward it can make a logo readable that wasn't noticeable in the still. "No logos" in the prompt does not remove a mark that is in
   the reference. Use the user's own product photos; a stock stand-in is for pipeline tests only and never for a published ad.

## Steps

### 1. Start from a hook and a goal
Take the ad from the `ad-matrix` file or the hook from the `hooks` skill. If neither exists, get the basics (what's sold, to whom, the
goal, where it runs, the proof and footage on hand) and write the hook first using the `hooks` skill's rules. Read the product's
`audience.md` if it exists, including seller facts and the Unknown list.

A hook the user supplies gets the same treatment as one you wrote: score it once with the `hooks` rubric, and check every claim in
it and in the planned on-screen text against what the user has told you ("ships in 5 days": dispatched or delivered? "copper
finish": on every variant?). Fix wording or flag it before planning shots. Pin down what the CTA physically asks for (for a DM goal:
what should they send?).

Ask what they already have: phone footage, product photos, customer clips, a logo, a voice they want, whether anyone will appear on camera.

### 2. Write the beat sheet
A table, one row per beat, 15-30 seconds total unless the user needs longer:

| # | Time | Job | Visual | On-screen text | Voice / sound | Source |
|---|---|---|---|---|---|---|

- **Jobs in order**: hook (0-3 s) → proof or demo → what it is and what you get → objection answered (if needed) → CTA.
- **Source** is one of: `have` (existing footage or photo), `film` (shoot on phone; give the shot instruction), `generate`, `screen`
  (screen recording), `graphic` (text card or still).
- Change the picture every 2-3 seconds. Captions word by word with one keyword highlighted. First frame must work muted.
- Use the structure recipes in `references/recipes.md` where one fits (transformation, anticipation cut, ad break, question-answer skit,
  photo-to-reveal and others).

**When a proof beat can't be filmed right now**, don't generate it; go down this ladder and take the first that's possible:
1. A real substitute for the same claim: the maker on camera holding the raw and the finished piece and saying how it's made; a
   physical test the viewer can hear or see (tap, weight, scratch, magnet, water); a raw-versus-finished match cut.
2. Other real evidence: older photos or clips, a customer's reaction or message (with permission), an order or review count.
3. Make this version without that beat, and plan a second version once the footage exists. Say what to film when it's possible.

**A plan that generates nothing is a good outcome**, not a gap to fill. If real footage, photos and text cards cover every beat, say
so, skip step 3's routing and the generation quote, and go to finishing. Offer a generated extra only when it clearly adds something,
and mark it optional.

### 3. Decide how each generated beat gets made
List the connector's workflows first (its workflow-listing tool with no argument), then route. Typical routes, by deliverable:

| Need | Route |
|---|---|
| One generated shot: hook clip, b-roll, product-in-scene, photo brought to life | Single video generation (image-to-video from the real photo where possible); model and prompt per `higgsfield-expert` |
| Creator-style video: talking review, unboxing, tutorial, try-on, product-only voiceover | The UGC video workflow |
| Narrated faceless explainer or story | The faceless video workflow |
| Many versions of one finished ad, or the same ad for another market | The ad multiplier workflow |
| Static ad images with copy | The ads studio workflow (quote first) |
| A whole product ad generated in one go (e.g. a marketing studio preset) | Only if the user asks for a fully generated ad; feed it the real product photos, and check the result against rule 3 before it's used. Don't pick it just because the connector recommends it. |
| Product stills, packshots, lifestyle photos for use as frames | The product photoshoot workflow |
| A recurring character for skits | The character sheet workflow, then reuse the character |
| Joining clips, captions, soundtrack | The video montage workflow; sound effects via the sound design workflow |
| The same video in other languages | The creator dub workflow |

If a workflow says it loads only from its own slash command, tell the user the command instead of forcing it. If no Higgsfield connector
is present, deliver the beat sheet, the shot instructions and ready-to-paste generation prompts, and say generation wasn't possible here.

### 4. The money gate
Before any generation: ask for the files the generation will use (photos, clips) so the quote reflects the real request; check the
balance; get a quote for exactly what you plan to run (the connector has cost-estimate tools for video, image and audio, and a quote
tool for ads studio). If a quote had to be made without the real inputs, say it may change and re-quote once they're uploaded.
Finishing steps (assembly, captions, sound) may also cost credits and may have no quote tool: say they're unpriced and get the cost
before running them, or give the user the edit list to do in their own editor for free. Then show the user:
- what will be generated (beats, count, length, format 9:16),
- the quoted credits against their balance,
- the cheapest sensible first step: **one short draft of the riskiest generated beat** before anything else.

Wait for a clear yes. A yes covers only what was quoted; ask again for retries beyond it, for more variants, and for the final-quality pass.

### 5. Draft, check, then finish
Review every draft before showing it as usable:
- **Honesty**: does the product look like the real one? Any invented text, logo, face or claim?
- **Artifacts**: hands, faces, garbled lettering, warped product geometry, physics that looks wrong, flicker between frames.
- **Hook**: score the opening with the `hooks` rubric; would frame one stop a muted scroll?
- **Fit**: right length, 9:16, key content inside the safe area (clear of the top bar, caption and button zones).

Say how you reviewed it: a frame sheet catches structure, branding and wrong motion, but not flicker or fine artifacts, so tell the
user to watch the clip itself before it's used.

Prompting lessons from the lab (see `lab/video-tests/`):
- Describe **one continuous move with a stated end frame** (or supply an end image). Exits such as "passes overhead" or "flies out of
  frame" are unreliable; the model tends to bring the subject back.
- For a hook clip, **put the motion in the first second**. Don't spend the opening on a held or hovering shot.

Fix by changing the prompt or the reference image, not by hoping. After two failed tries on one beat, stop and offer the fallback
(film it, use a still with motion, or restructure the beat). Never burn credits in a loop.

Finishing: assemble, add captions and sound, end on the CTA said and shown. Generated text inside video is unreliable, so add text
in the edit, not in the prompt.

### 6. Check and record
- If the connector offers a virality or performance predictor, offer it; present its score as a prediction to compare drafts, not as proof.
- Record what was made (asset link, credits spent, what was generated versus real): in the ad matrix row if a matrix exists, otherwise
  in a short `video-log.md` next to the product's other marketing files.
- Tell the user plainly what was made, what it cost, what's still theirs to do (film a beat, get a permission, add the AI label).

## Reference files
- `references/recipes.md` — named structure and shot recipes, what each needs and when it fits. Read at step 2.

## Worked examples
- A reel when the proof can't be filmed: `examples/keychain/video-plan.md`; a film-only reel for a real product: `lab/products/magsafe-wallet-reel-01.md`; the first generated draft and its review: `lab/video-tests/0001-drone-draft/notes.md` (repository root).
- Flowchart of this process: `docs/PROCESS.md`.
