# Example: hooks for electroplated custom keychains

Invented test product. Output of the `hooks` skill, blind test 1 (2026-11-25).

## Request (write mode)
> Give me hooks for an Instagram reel. I sell 3D-printed keychains with a real metal electroplated finish (copper, nickel, gold-tone),
> custom name or logo, ₹499, made to order in India, ships in 5 days. Buyers are mostly 18-30, buying gifts for a partner or friend.
> Goal: sales via DM. I have process footage of the plating tank and before/after shots. No sales numbers yet.

## Response

**Audience assumptions (no research file, so these are guesses; correct any that are wrong):**
- **Problems and frustrations:** gifts under ₹500 look generic (mug, teddy, printed acrylic); "customised" items arrive looking cheap or
  late; the partner says "I don't want anything".
- **Wants, questions and objections:** something that looks expensive and personal; "price?", "kitne din mein aayega?", "can you do my
  logo?", "will the colour fade?"; "it's just plastic", "₹499 for a keychain?".
- **Mistakes and their words:** ordering too late for the date; "gift for bf/bestie", "under 500", "customised", "aesthetic".

```
1. Proof contrast — 10/12
   Visual: Dull grey printed name-keychain on a hook drops into the plating tank; hard cut to the same piece lifting out bright copper.
   Text:   Plastic in. Real copper finish out.
   Says:   "This went into the tank as plastic. This is the same piece coming out."
   Why it should work: the change happens in frame one with sound off, and people stay to see how.
   Sets up: 5 seconds of real tank footage, then the finished keychain with a name on it and "₹499, DM your name".

2. Objection — 10/12
   Visual: Raw print in one hand, gold-tone finished one in the other; the raw one gets tossed toward the tank.
   Text:   "₹499 for a keychain?"
   Says:   "₹499 for a keychain? Fair. Watch what it goes through first."
   Why it should work: says the buyer's own doubt before they do, and promises the answer.
   Sets up: print, then plating, then polish, shown fast, so the price feels earned by the end.

3. Call-out — 10/12
   Visual: Gold-tone name keychain drops into an open palm, close-up, light catching the letters.
   Text:   Partner says "kuch nahi chahiye"?
   Says:   "Partner bolta hai 'kuch nahi chahiye'? ₹499 mein unka naam, real copper finish mein."
   Why it should work: names the exact gifting situation in the words they use, with the price up front.
   Sets up: the before/after of one real name being made, then "DM the name, ships in 5 days".

4. Stakes (deadline) — 9/12
   Visual: Phone calendar with a date circled; a finished keychain lands on top of it.
   Text:   Birthday next week? Order today.
   Says:   "If their birthday is next week, today is the last day you can order this."
   Why it should work: turns the 5-day lead time into a reason to DM now.
   Sets up: only honest if "5 days" means delivered; if it means dispatched, change the line to match.

5. Ego / quiz — 9/12
   Visual: Finished nickel keychain dropped on a table, spun under light, extreme close-up.
   Text:   Guess what's under the metal.
   Says:   "Guess what this is made of. You'll get it wrong."
   Why it should work: a guess people want to check, and the answer (a 3D print) is the surprise.
   Sets up: the reveal of the raw print within 5 seconds, then the tank.
```

Test 1 against 3 first. Hook 1 leads with the process and hook 3 leads with the buyer's situation, so the result tells you whether the
tank or the gifting moment sells.

## Request (score mode)
> Rate this hook: "Check out our amazing new custom keychains, they are a total game-changer for gifting!"

## Response
`Specific 0 · Viewer 0 · Loop 0 · Clear 2 · Muted 1 · Unswappable 0 = 3/12 — tags: about-us, generic, empty-intensifier, no-loop, no-visual`

- **It's about you, not them.** "Check out our… new" is an announcement.
- **Any keychain seller could post it unchanged.** Nothing says electroplated, a name, or ₹499.
- **"Amazing" and "total game-changer" carry no information.**
- **Nothing is left to find out**, so there's no reason to watch second two.
- **No frame-one visual.**

Rewrites:
1. **Proof contrast.** "This went into the tank as plastic. This is the same piece coming out."
2. **Objection.** "₹499 for a keychain? Fair. Watch what it goes through first."
3. **Call-out.** "If your partner says 'I don't want anything', put their name in a real copper finish for ₹499."

## What this run changed in the skill
Eight gaps, including: the rubric penalised demo hooks (a transformation now counts as "for the viewer"), the goal was collected but unused
(now a goal table), and three different banned-opener lists (now one). See `lab/skill-tests.md`, test 1.
