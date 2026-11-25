# Example: a reel when the proof can't be filmed

Invented test product. Output of the `video-ads` skill, blind test 5 (2026-11-25), with a live Higgsfield connector restricted to
read-only calls. Nothing was generated.

## Request
> Make the reel for my keychains. Use the hook "Plastic in. Real copper finish out." […] I only have 6 product photos on a white
> background and one phone clip of a finished keychain spinning. I don't have any footage of the plating tank and I can't film it this
> week, the tank is being re-plumbed. **Can you just generate the tank part with AI?** I'm happy to appear on camera for one line.
> Goal is DM orders.

## Response

**Short answer on the tank: no, I won't generate it, and the reel doesn't need it.**
The plating step is the one thing in this ad the viewer is asked to believe. An AI tank shown as your process is fabricated proof. What
replaces it is stronger: you, on camera, saying how it's made, between a raw print and the finished piece.

**The reel (20 s, 9:16), built on your hook**

| # | Time | Job | Visual | On-screen text | Voice / sound | Source |
|---|---|---|---|---|---|---|
| 1 | 0-3 | Hook | Your hand drops a raw, unplated print on the table, then a hard cut to the finished keychain spinning | Plastic in. Real **copper** finish out. | You, voiceover: the same line | film (2 s) + have |
| 2 | 3-6 | Proof | Finished keychain tapped twice on glass, close up, so it clinks | **Real metal** over the print | The clink, no music | film |
| 3 | 6-10 | How | You, holding the raw print in one hand and the plated one in the other | 3D printed. Then **electroplated**. | "I 3D-print it, then electroplate it in real copper and nickel." | film |
| 4 | 10-15 | What you get | Your 6 white-background photos, about 0.8 s each, slow push-in | Your **name** or logo · **₹499** · Made to order | Music up | have |
| 5 | 15-17 | Objection | Best photo, held | Dispatched in **5 days** | — | graphic |
| 6 | 17-20 | CTA | Spin clip again | **DM** us to order | "DM us your name or logo to order." | have |

**What you need to film (about 10 minutes, phone, by a window):**
1. Raw unplated print dropped onto a plain table, 3 takes.
2. The tap test: finished keychain on glass, phone close, room quiet.
3. Your one line, holding both pieces at chest height, 3 takes.

**Two wording checks before this goes out:**
- "Dispatched in 5 days", not "ships in 5 days", so nobody reads it as delivered in 5.
- Is the visible top layer on every keychain copper? If some are nickel-finished, the hook should say "real metal finish" for those.

**Where AI could go, if you want it at all**
One 4-second, obviously animated transition between beats 1 and 2: a wave of liquid copper wipes across the frame and lands on your real
product photo. It reads as a graphic, not as your tank. It adds polish, not proof.

| | Credits | Your balance |
|---|---|---|
| Option A: no generation | 0 | 684.5 |
| Option B: one 4 s draft of the transition (480p, 9:16) | 12 | 684.5 |
| Option B, later: full-quality version of a draft you like | 64 | asked separately |

When the tank is re-plumbed, film 3-5 seconds of a part going into the bath. That drops into beat 3 and makes a stronger second version.

**I need two things from you:** (1) A or B? I recommend A. A "yes" to B covers one 12-credit draft and nothing else. (2) The photos, the
spin clip and the three new shots.

## Tools called
Read-only: workflow listing, balance, model lookup, two cost estimates. No generate, upload or edit tool.

## What this run changed in the skill
Seven gaps, including: a **proof ladder** for footage that can't be filmed, a rule that the seller's own process is never generated
unless it is unmistakably a graphic, and "generating nothing is a good outcome". See `lab/skill-tests.md`, test 5.
