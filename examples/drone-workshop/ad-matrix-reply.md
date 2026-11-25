# Example: an ad matrix for a first-time advertiser on a small budget

Invented test product. Output of the `ad-matrix` skill, blind test 4 (2026-11-25). Files it wrote: [ad-matrix.csv](ad-matrix.csv),
[ad-brief.md](ad-brief.md). The CSV uses the earlier `wave` column; the current skill calls it `stage` (live / held / idea).

## Request
> Make me ads for the next batch of my drone workshop. I want bookings on WhatsApp. Budget is ₹500 a day on Instagram for two weeks. I
> can film on my phone and I have day-2 flying footage, the first take-off clip with kids cheering, and photos of the build tables. One
> parent from last batch said I can use her message. I can make about 8 ads this week, some can be image ads made in Canva. Next batch is
> 13-14 December, 9am-4pm both days, each child builds and keeps their own drone, no soldering (it's a snap-fit kit), I give a
> participation certificate, class 6 is fine if a parent stays. No advanced batch yet. I've never run ads before.

## Response

I've planned 8 ads you can make this week: 5 short videos from footage you mostly already have, and 3 Canva images. Six go live on day 1
and two are held back as swaps. Check one thing first: **13-14 December 2026 is a Sunday and a Monday**, not a Saturday and Sunday. I've
kept "weekend" out of every ad until you confirm the dates.

The plan rests on your earlier audience notes, which come from only 10 WhatsApp messages, so treat it as a first test.

**The four ideas being tested**
- **C1, Flies on day two:** ₹2,999 feels like a lot until you see what happens on day 2.
- **C2, Theirs to keep:** each child builds their own drone and takes it home.
- **C3, Still talking about it:** the first take-off, the cheering, and the parent's words.
- **C4, Parents' questions answered:** no soldering, certificate, class 6 with a parent, timings.

**Live from day 1**

| Ad | What it is | What it tests |
|---|---|---|
| C1-H01-B1-A1 | Flying footage opening on "₹2,999 for 2 days?" | Price-doubt opening |
| C1-H02-B1-A1 | Same video opening on "Day 1: parts on a table. Day 2: this." | Before/after opening on the same video |
| C3-H04-B2-A1 | Take-off clip, "They built this yesterday. Will it fly?", then the parent's message | The excitement idea |
| C4-H07-B3-A2 | You on your phone, snapping the kit together and answering the soldering question | The answers idea, with you on camera |
| C2-H10-B4-A1 | Canva image of a build-table photo: "Your child builds this drone. Then takes it home." | The keep-it idea; image against video |
| C4-H13-B5-A2 | Canva notes-style list of what parents ask | Plain text answers against photo and video |

**Made this week, held back**
- C3-H05-B2-A1: the take-off clip opening on the parent's words. Swap it in on day 5.
- C2-H12-B4-A1: a date card, "13-14 December. 12 seats." Use it in the last week.

**How to run it on ₹500 a day (₹7,000 in total)**
- Put all six in one campaign set to bring WhatsApp messages. A clicks or views goal buys clicks and views, not enquiries.
- Leave it alone for days 1-4.
- On day 5, pause any ad that has spent ₹400 or more with no WhatsApp chat, or that costs more than double the best ad per chat. Put the
  two held ads in their place.
- Judge by paid seats. Three bookings bring in more than the ad spend, before your kit and venue costs.
- Note which ad each enquiry came from and whether they booked.

The day-5 numbers are starting guesses, not tested figures.

**I need these from you before anything goes live**
1. Are the dates right, given they fall on Sunday and Monday?
2. Is this batch still ₹2,999 and 12 seats? Both figures come from the earlier batch.
3. Which message did the parent allow, and is she fine with it in a paid ad?
4. Do you have the other parents' OK to show their children's faces in ads? If not, use shots where faces aren't clear.
5. What is the venue?

## What this run changed in the skill
Seven gaps, including: "make / live / held" as three separate numbers, campaign setup declared out of scope, a derived cut rule and
break-even, tying chat sales back to ads, and consent for people (children) in footage. See `lab/skill-tests.md`, test 4.
