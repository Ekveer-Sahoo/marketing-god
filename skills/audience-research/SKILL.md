---
name: audience-research
description: Build or update the audience research file for a product: who buys, their problems, frustrations, desired outcomes, questions, mistakes, objections, the emotions underneath and the exact words they use, each tagged with where it came from. Use before writing any hooks, ad copy, scripts, landing pages or positioning for a product that has no audience file yet; when the user asks "who is my customer", "what are my customer's pain points", for an ICP, persona, customer avatar, voice-of-customer or review mining; when they paste reviews, DMs, comments or survey answers and want them made sense of; and when copy keeps coming out generic.
---

# Audience research

Copy fails most often because it was written before anyone looked at the buyer. The fix is to research first and write second: collect what
buyers actually say, sort it, and only then choose a problem and an angle. Every other marketing-god skill reads the file this skill
produces, so the file matters more than the chat reply.

This method has not yet been validated on many products. If the user has their own research process, follow theirs and keep this file format.

## What you produce
A single file, `audience.md`, in the user's working folder at `marketing/<product-slug>/audience.md` (if the project already keeps product
files somewhere, such as `lab/products/`, save it there as `<slug>-audience.md`). Use `references/audience-template.md` as the structure.
If the file already exists, update it: add new evidence, upgrade assumptions that are now confirmed, and note what changed at the bottom.

## Tag every line with where it came from
| Tag | Meaning | Trust |
|---|---|---|
| `[own]` | Said by the user's own customers or prospects: reviews, DMs, comments, support questions, sales calls, survey answers, order data. Add `buyer` when it's from someone who actually purchased. | Highest; buyers above enquirers |
| `[public: source]` | Said by other people's customers in the same category: competitor and marketplace reviews, Reddit, forums, comment threads | Medium |
| `[inferred: from …]` | Your interpretation of a specific piece of `[own]` or `[public]` evidence (name it) | A reasoned guess |
| `[assumed]` | Your reasoning with no source | A hypothesis to check |

The tags exist because a confident persona made of assumptions looks identical to a researched one unless every line shows its source.
Never present an inference or assumption as a finding.

**Quotation marks are for verbatim text only.** Everything in parts 1-7 is your paraphrase, written without quote marks; real quotes live in
part 8 and are referenced from elsewhere. Never invent a quote.

## Steps

### 1. Get the basics (one short message, only what's missing)
**About buyers:** who buys and who uses it (these differ for gifts, B2B, parents) · what they use today instead · any material the user
has: reviews, DM screenshots, comments, FAQs, sales notes, order data.
**About the seller** (angles and "product fit" depend on these): the one outcome it gives · exactly what the buyer gets for the price ·
price · where and how it's sold · when they get it (delivery time, or dates, timings and venue for a service or event) · who it's for
and any eligibility limits · payment options · returns, refunds or guarantee · the safety or risk questions buyers raise · for
products, how it holds up over time and bulk or custom terms.

Ask for their own customer material before anything else; ten real DMs beat a hundred assumptions. If the user can't or doesn't answer
something, don't stall: carry on and record it under "Seller facts → unknown" in the file.

### 2. Collect
- **Own material first.** Read everything provided. Pull out problems, questions, objections and exact phrases. Keep quotes word for word,
  including spelling, slang and mixed language (Hinglish stays Hinglish). Note which came from buyers and which from enquirers.
- **Public voice of customer, if a search tool is available.** Look where buyers of this category talk: reviews of the closest competitors
  (3-star and 1-star reviews carry objections; 5-star reviews carry the desired outcome), marketplace Q&A, Reddit and forum threads,
  comments on popular posts about the category. Record the source. A handful of rich threads is enough.
- **Inferences and assumptions last**, only to fill gaps.

Count your **source items** as you go: one DM, one review or one thread = one item. This count, not the number of lines in the file, is the
evidence mix you report.

### 3. Sort into the eight parts
Give each finding **one home**, the part it fits best; don't restate it in three places. Write as many lines as the evidence supports and
no more. A short honest file is better than a padded one, and padding makes thin research look thorough.
1. **Problems** they have that this product touches.
2. **Frustrations** with the current way of solving it (including competitors).
3. **Desired outcomes**, in their terms, including the social or emotional one ("she asks where I got it").
4. **Repeated questions** before buying.
5. **Common mistakes** they make around the problem.
6. **Objections and limiting beliefs**: why they don't buy.
7. **Emotional reasons** underneath: what it means to them, what they fear, what they want to feel. (Usually `[inferred]`.)
8. **Their words**: verbatim quotes.

Then the context: **segments** with buyer vs user and the **trigger or occasion** that starts the search · **alternatives** they compare
against (including doing nothing) · **awareness** (do they know the problem, the kind of solution, this product?) · **where their
attention is**.

### 4. Decide
Research that doesn't end in a choice doesn't get used. Write these last:
- **Best first segment**: one specific person in one specific situation, and who it's not for.
- **The three strongest problems or objections**: whatever most stands between this buyer and buying. Pre-sale enquiries give you
  objections, buyer reviews give you problems and outcomes; say which kind each one is. Rank by how much it hurts, how often it shows up
  in the evidence, and how well this product solves it.
  "Hurts" and "fit" are your judgement, so label them as such; write "unknown" for fit when a seller fact is missing.
- **Angles**: three to five, each = one problem or desire + the outcome + the proof or mechanism that makes it believable. Include at
  least one built on a desired outcome, not only on answering doubts. If an angle would use a customer's message as proof, note that it
  needs their permission.
- **What we don't know yet**, with the cheapest way to find out: up to five questions for real customers, or data to pull.

**Thin evidence.** With fewer than about 30 source items, nothing is a pattern yet. Still make the choices, because the user needs a place
to start, but call them provisional, give counts ("2 of 10 messages"), and put the draft notice at the top of the file.

### 5. Save, then tell the user briefly
Write the file. In chat give: the best first segment, the top three problems with counts, the angles, the evidence mix by source items
(own / public) and roughly how much of the file is inferred or assumed, and the questions to ask customers. Don't paste the whole file.

## Rules
- **Specific over demographic.** "Engineering student buying a first gift for a girlfriend on a ₹500 budget" is useful; "18-30, urban" is
  not. Rules of thumb about what a generation or class wants are priors, not findings.
- **Verbatim stays verbatim.** Don't polish quotes; the roughness is the value.
- **Count before concluding.** One loud review is not a pattern.
- **Negative evidence counts.** Record who the product is not for.
- **Privacy.** Strip names, handles, phone numbers and order details from quotes before saving. This is about patterns, not individuals.
- **It's a living file.** When ads or posts produce results, come back and mark which problems and angles were confirmed or killed.

## Reference files
- `references/audience-template.md` — the file structure to fill. Read before writing the file.

## Worked examples
- A file built from ten customer messages where the buyer and user differ: `examples/drone-workshop/audience.md` (repository root).
- Flowchart of this process: `docs/PROCESS.md`.

## Three lenses to apply when sorting (round 2)
Added from the round 2 study (`curriculum/06-round2-synthesis.md`). Untested in the lab.
- **Three layers of each problem:** the practical problem, the emotional one, and the belief underneath ("people like me can't…").
  Record all three for the top problems; copy that answers only the practical layer leaves price as the deciding factor.
- **Driver, trigger, barrier:** why they buy, the moment the problem hits, and what stops them. Put the trigger in the segment table and
  the barrier under objections.
- **Belief shift:** for the best first segment, write what they believe now and what they would need to believe to buy.
- **When they leave:** for anything bought repeatedly, ask when customers stop (which week, which order), before guessing why.
