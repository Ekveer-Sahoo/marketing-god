---
name: ad-matrix
description: Plan a batch of paid ads as a matrix of hooks × bodies × calls to action across genuinely different formats, with a naming scheme, a shoot list and a tracking sheet. Use when the user wants ad creatives, ad ideas, ad variations, a creative testing plan, "ads for my product", Meta / Facebook / Instagram / TikTok ad concepts, static ad ideas, UGC scripts for ads, or says their ads all look the same, are fatiguing, or that they don't know what to test next. Also use to turn one winning ad into variations.
---

# Ad matrix

One ad is a guess. A matrix is a test. An ad has three parts: a **hook** (gets attention), a **body** (earns belief: the problem,
the product, the offer, the proof) and a **CTA** (says exactly what to do). Writing several of each and combining them gives many ads from
one production session, and tells you afterwards *which part* won.

The point is variety of concept and format, not volume for its own sake. Ten ads with the same layout, the same product shot and a
different background colour are one ad, and ad platforms tend to treat them that way.

Status: built from `curriculum/03-ads.md` (creators' reels). Platform behaviour described there is practitioner opinion, not verified
against platform documentation, and nothing here has been through the lab. When the user's own account data disagrees, their data wins.

## Before you start
- **Audience file.** Read the product's `audience.md` (from the `audience-research` skill): best first segment, top problems or objections,
  angles, verbatim phrases, seller facts and the Unknown list. If none exists, say so and either run that skill first or proceed on stated
  assumptions; a matrix built on nothing is a matrix of generic ads.
- **Hooks.** Use the `hooks` skill's rules: types, three layers, scoring and fatal flags. Ignore its batch size and delivery format
  (15 candidates, top 5); this skill decides how many hooks and how they spread, that one decides whether each is good.
- **Keep the audience file current.** If the user's message settles something on its Unknown list or changes a seller fact, update
  `audience.md` (seller facts and change log) before planning. Facts carried over from an earlier batch or offer (price, seats, dates)
  get a one-line "still true?" check in your reply.
- **Sanity-check what you're about to print on an ad**: that dates fall on the days claimed (a "weekend" batch on a Sunday-Monday is
  a mistake to catch now), that prices and discounts add up, that deadlines are in the future.

## Scope
This skill plans creatives and how to read the test. It does **not** set up campaigns: account setup, targeting, placements and the
platform's screens are outside it and change often. Say so plainly, give only the objective-match rule and the tracking advice below,
and point a first-time advertiser to the platform's own setup guide (or offer to walk through it with them live) rather than
improvising steps.

## Steps

### 1. Get the inputs (one short message, only what's missing)
- **Objective and destination**: what counts as a result (purchase, lead, booking, DM) and where the ad sends people. The campaign
  objective must match the result wanted; optimising for clicks buys clickers, not buyers.
- **Offer**: price, what's included, any bonus, deadline or limit that is true.
- **Proof on hand**: demos, results, reviews, customer messages (with permission), numbers. Never invent any.
- **Assets and capacity**: footage and photos they have; who can film; whether they can make video, statics or both; **how many finished
  ads they can realistically produce this week**.
- **Budget and economics**: daily spend and for how long; the price; roughly what one sale leaves after costs. From these work out the
  break-even (total spend ÷ profit per sale = sales needed) and state it.
- **Platform and placements** (default: Meta, vertical 9:16 video and 4:5 or 1:1 statics).
- **What has run before**, and what won or lost, if anything.

### 2. Choose 3-5 concepts
A concept is one angle: a problem or desire + the outcome + why it's believable. Take them from the audience file. They must differ in
*what they argue*, not in wording. Include at least one led by desire or result, not only objection-handling. Give each a short name.

### 3. Write the bodies (3-5)
Each body carries one concept in one format. Use different formats so the ads really differ; `references/formats.md` lists them (video:
demonstration, testimonial, educational, story, faceless; statics: native-UI, editorial, review, ugly-on-purpose, comparison, call-out)
and says which suit which buyer and price. Choose formats the user's assets can actually make.
- Video body: a 15-30 second outline in beats (what's shown, what's said), ending where the CTA begins.
- Static body: headline, supporting line, what the image is, where the proof sits.

### 4. Write the hooks
Write more hooks than you'll use (two or three per body is a good pool), spread across hook types and awareness levels (people who
don't know the problem, know the problem, know solutions exist, know this product). Mark which bodies each hook can open: not every hook
fits every body. Unused hooks go in the brief as a backlog for the next round.

For **video**, a new hook on the same body is a different ad only if the first three seconds look different, not just sound different.
For **statics**, a new headline on the same layout is copy variation, not a new ad; a hook change must change the image or the format family.

### 5. Write 1-3 CTAs
Say and show exactly what to do next, matched to the destination. Use first-person, specific wording ("Book my seat", "Send my size",
"Get my 20% off") over "Learn more" / "Shop now". Add a deadline or limit only if it's real. The platform's button text is usually a fixed menu ("Send message", "Book now"), so your
CTA wording goes in the spoken line, the on-screen text and the caption; say which button to pick.

### 6. Assemble the matrix
Combine only compatible hook × body × CTA sets. Three numbers govern the size, and they're different things:
- **Make** = what they can produce this period (capacity). Never plan more finished ads than this.
- **Live** = how many of those the budget can test at once (see the test plan). Often fewer than Make.
- **Held** = made but not yet live; swapped in when a live ad is cut. Anything beyond Make is an **idea** for a later round.

Give every ad an ID that encodes its parts, e.g. `C2-H05-B3-A1` (concept, hook, body, CTA), so results can be read back by part. A hook
used on another concept's body takes that body's concept number.

**Diversity check before delivering.** The made set must cover every concept and at least three formats. If two ads would look the same
with the sound off and the text blurred, they are the same ad: replace one.

### 7. Deliver three things
1. **`ad-matrix.csv`** next to the audience file, using the columns in `references/matrix-columns.md` (creative columns filled, result
   columns empty for the user to fill in). If a Sheets artifact tool is available and the user wants a shared tracker, offer that instead.
2. **`ad-brief.md`**: the concepts, each body's outline, the hook list, the CTAs, and a **shoot list** grouped so everything can be
   captured in one session (all hooks, then all bodies, then all CTAs, per location or setup).
3. **In chat**, briefly: the concepts in one line each, the live and held ads by ID with what each one tests, the break-even, the test
   plan below, what this skill doesn't cover (campaign setup), and anything that needs the user's decision, consent or a missing fact.
   Don't paste the whole matrix.

### 8. The test plan (state it with the delivery)
- **Live set.** Launch a set that fits the budget; spreading a small budget over many ads means none gets enough delivery to judge.
  Rule of thumb (unverified, adjust to the account): about 4-6 live ads on a very small budget, up to 6-12 as budget grows, covering
  every concept.
- **Judge by the result that matters**: cost per purchase, lead or booking, and revenue. Views and clicks only diagnose *where* an ad
  fails: low hook rate → the hook; watched but not clicked → the body or CTA; clicked but not bought → the offer or the landing page.
- **Decide the cut rule in advance** so losers are cut by rule, not mood. Derive it from the economics: target cost per result = what
  a sale can afford. A common practitioner default (unverified) is to cut an ad once it has spent two to three times that target with
  no result, or is running well above the best ad's cost per result after the first few days. Label any number you give as a starting guess.
- **When the sale happens in chat or offline**, the platform can't see it. Use cost per conversation as the early signal and give the
  user a way to tie bookings back to ads: ask every enquirer which ad they saw, or give each ad its own pre-filled message or code.
  The sheet's result columns are then filled from the user's own tally.
- **A winner is the start.** Work out which part won by comparing IDs, then make variations of *that concept*: new hooks on the winning
  body, the winning hook on new formats.
- **Record results** in the sheet. That history is the next matrix's best source of hooks.

## Turning one winner into variations
When the user brings an ad that worked: identify its concept, hook type, body format and CTA; hold the concept; vary one part at a time
(5 new hooks on the same body; the same hook and message rebuilt in two new formats, e.g. as a notes-app screenshot or a testimonial).
Don't change everything at once or the result can't be read.

## Rules
- **True claims only.** No invented reviews, numbers, results, credentials or scarcity. Nothing from the audience file's Unknown list
  stated as fact.
- **Consent.** Customer messages used as proof need the customer's permission for paid ads specifically; trimming a quote must not
  change its meaning or imply something that isn't offered. Identifiable people in footage need to have agreed to appear in ads, and
  children need a parent's agreement; otherwise use shots where faces aren't clear. Raise this whenever the footage shows other people.
- **Native-looking formats must not deceive.** A notes-app or chat-style ad is fine when it's obviously the brand speaking; a fake news
  article, a fake review or a fabricated private conversation presented as real is not, and risks rejection.
- **Mind platform ad rules.** For example, ads on Meta shouldn't assert or imply a viewer's personal attributes ("Are you overweight?",
  "Struggling with debt?"); address the situation, not the person's condition. Naming who an offer is for by role or location
  ("for parents of class 7-10 kids in Bhubaneswar") is ordinary targeting copy; asserting something sensitive about the viewer is not. Health, finance and before/after claims need extra care.
  When unsure, flag it instead of guessing.
- **No one else's IP.** Don't imitate named shows, characters, studios or brands as an ad style.
- **Write to the buyer** when buyer and user differ, in the buyer's language.
- **Capacity is a hard limit.** A matrix the user can't produce is worth nothing; smaller and shippable wins.

## Reference files
- `references/formats.md` — video body formats, static format families with when each works, AI-video styles, and format-by-buyer guidance. Read at step 3.
- `references/matrix-columns.md` — the CSV columns, ID scheme and an example row. Read at step 7.

## Worked examples
- Eight ads on a small budget, with the files and the chat reply: `examples/drone-workshop/` (repository root).
- Flowchart of this process: `docs/PROCESS.md`.

## Sharper rules from round 2
Added from the round 2 study (`curriculum/06-round2-synthesis.md`). Untested in the lab. Platform numbers here are practitioners' claims; label them as starting guesses.

**What counts as a new angle.** An angle is a reason to buy, aimed at one person at one awareness stage. A new hook or edit on the same
pitch is iteration. When a winner tires, change things in this order: who it's for → angle → desire → awareness stage → mechanism →
promise → offer, and only then hook, format, presenter, pacing and CTA.

**How many creatives to test.** Winners needed = daily spend ÷ the spend one winning ad can hold. Creatives to test = winners ÷ expected
hit rate. Example: ₹5,000 a day, ₹1,000 per winner, 10% hit rate → 5 winners → about 50 creatives over time. On a small budget keep 3-5
ads live per ad set, test one angle, and vary only the opening seconds on a body that already works.

**Reading the numbers.**
- Cost per purchase = CPM ÷ (1,000 × click-through rate × conversion rate). Use it to see which of the three is the problem.
- High CPM → audience or creative. Low click-through → hook. Clicks but no sales → the page, the offer or checkout.
- Before raising budget, check: conversion tracking, that the page matches the ad, mobile speed, the objective, surprise costs at
  checkout, visible trust signals.
- Judge by contribution margin: take one order through product cost, shipping and returns, then ad cost. Break-even return on ad spend
  matters more than the headline figure.
- Raise budgets gradually (a common claim: about 20% every few days), not by doubling.

**Format by stage.** Top: founder clips, UGC, native-looking statics, skits. Middle: testimonials, comment replies, comparisons. Bottom:
offer and product statics, deadlines. Combining two proven formats (founder selfie + lesson, offer + meme) is a cheap source of new concepts.

**Search or social first?** If the buyer searches when the need hits (an emergency, a named product), start with search ads; if the need
has to be shown to them, start with social. Free research: the platforms' ad libraries and transparency centres, and competitors'
reviews for complaints to answer.
