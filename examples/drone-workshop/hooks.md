# Example: hooks that read an audience file

Invented test product (weekend drone-building workshop, classes 7-10, ₹2,999). Output of the `hooks` skill in blind test 3
(2026-11-25), run straight after `audience-research` produced [audience.md](audience.md).

## Request (write mode)
> Now give me hooks for an Instagram reel to get bookings for the next batch. I have footage of kids flying their drones on day 2 and a
> clip of one drone's first take-off with the kids cheering.

## Response
Working from your audience file (provisional, 10 messages) and aimed at parents, with bookings as the goal. Three things to check before
posting:
- I've written "the drone goes home with them"; change it if a team shares one drone.
- [date] is a placeholder for the next batch.
- Hook 4 quotes a parent's WhatsApp message, so get their OK first.

```
1. Curiosity gap (your own take-off clip) — 11/12
   Visual: The first take-off clip, starting 2 seconds before lift-off: drone on the floor, kids crouched around it.
   Text:   They built this yesterday. Will it fly?
   Says:   "Yesterday this was a box of parts. They built it themselves. Watch."
   Why it should work: the viewer has to see whether it lifts, and the cheer is the payoff.
   Sets up: the take-off and cheering, then "2 days, class 7-10, Bhubaneswar, WhatsApp to book".

2. Price objection — 10/12
   Visual: Day-2 footage, several kids flying at once.
   Text:   ₹2,999 for 2 days?
   Says:   "₹2,999 for two days sounds like a lot. This is day two."
   Why it should work: it says the parent's doubt out loud before they do, over the answer.
   Sets up: what the fee covers: they build it, fly it, and the drone goes home with them. 12 per batch.

3. Question the viewer is already asking (verbatim) — 9/12
   Visual: A kid flying their drone, close on the hands and the drone.
   Text:   "Sir, drone ghar le ja sakte hai kya?"
   Says:   "Ek student ne poochha: sir, drone ghar le ja sakte hai kya? Haan. Jo banaya, woh ghar jaata hai."
   Why it should work: a real question in the kid's own words, and the answer is the best thing about the offer.
   Sets up: build on day 1, fly on day 2, then the booking line for parents.

4. Proof (a past parent's words) — 10/12
   Visual: The take-off clip at the moment of the cheer.
   Text:   "He has not stopped talking about it" — parent, last batch
   Says:   "A parent from our last batch messaged us: he has not stopped talking about it. This is why."
   Why it should work: another parent's words show the result parents want.
   Sets up: the cheer playing out, then the next batch date [date] and 12 seats.

5. Call-out — 9/12
   Visual: Day-2 flying footage, wide shot.
   Text:   Bhubaneswar · Class 7-10 · 12 seats
   Says:   "If your child is in class 7 to 10 in Bhubaneswar, this is what one weekend can look like."
   Why it should work: the right parent recognises themselves in the first second.
   Sets up: build, fly, take home, ₹2,999, WhatsApp to book for [date].
```

Test 1 against 2 first. One sells the moment and the other answers the price doubt, so the result tells you whether parents need desire
or reassurance.

## Request (score mode)
> Rate this one: "Is your child wasting weekends on the phone? Enrol in our drone workshop today!"

## Response
Assumed: the spoken or on-screen line of an Instagram reel with no visual described.

`Specific 1 · Viewer 2 · Loop 0 · Clear 2 · Muted 0 · Unswappable 0 = 4/12 — tags: generic, no-loop, no-visual, wrong-audience-words`

- **Generic:** swap "drone" for "coding" or "abacus" and any class could run it.
- **No loop:** the question is answered by the pitch in the same breath.
- **No visual:** nothing happens in frame one. The take-off clip isn't being used.
- **Wrong words:** none of the 10 parent messages mention phones; they ask about price, safety, certificate and taking the drone home.
  The phone line also mildly scolds the parent.

Rewrites:
1. Curiosity gap: "They built this yesterday. Watch what happens when they switch it on."
2. Price objection: "₹2,999 for two days? Fair question. This is day two."
3. Numbers: "One weekend. Day 1 they build it, day 2 it flies, then it goes home with them."

## What this run changed in the skills
Hook 3 drifted into the child's Hinglish for a parent-facing reel, which led to the rule "write to the buyer, in the buyer's language".
Six other gaps were fixed too: see `lab/skill-tests.md`, test 3.
