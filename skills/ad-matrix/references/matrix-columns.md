# Matrix file: `ad-matrix.csv`

One row per planned ad (live, held, and ideas for later rounds). Quote any cell containing a comma. Leave result columns empty.

## ID scheme
`C<concept>-H<hook>-B<body>-A<cta>`, e.g. `C2-H05-B3-A1`. Keep a key of what each C, H, B and A number means in `ad-brief.md`.
Use the same ID as the ad's name in the ad platform so exported results can be matched back.

## Columns
| Column | What goes in it |
|---|---|
| `ad_id` | The ID |
| `stage` | live (launch set) / held (made, swapped in later) / idea (not being made this round) |
| `concept` | Short concept name |
| `awareness` | unaware / problem / solution / product |
| `media` | video or static |
| `format` | Body format or static family (e.g. demonstration; native-UI: notes app) |
| `hook_type` | Type from the hooks skill |
| `hook_score` | Score out of 12 from the hooks skill's rubric |
| `hook_visual` | Frame one (video) or the image (static) |
| `hook_text` | On-screen text or headline |
| `hook_spoken` | First spoken line (video) or blank |
| `body` | One-line summary of the body; full outline lives in the brief |
| `cta` | The exact CTA wording |
| `destination` | Where it sends people |
| `tests` | What this ad tells us versus its neighbours (e.g. "price-objection hook vs desire hook on the same body") |
| `needs` | Asset, permission or fact still required before it can be made |
| `status` | idea / ready to make / made / live / paused / winner / cut |
| `launched` | Date it went live |
| `spend` · `impressions` · `hook_rate` · `ctr` · `conversations` · `results` · `cost_per_result` · `revenue` | Filled in by the user: delivery numbers from the platform; `results` and `revenue` from their own tally when sales happen in chat or offline |
| `notes` | What was learned |

`hook_rate` = 3-second views ÷ impressions (video only).

## Example row
```
C1-H02-B1-A1,live,It flies on day two,product,video,demonstration,price objection,10,Kids flying drones outdoors,"₹2,999 for 2 days?","₹2,999 for two days sounds like a lot. This is day two.",Build day 1 → fly day 2 → drone goes home; 12 per batch,Book my child's seat on WhatsApp,WhatsApp chat,Price-objection hook vs anticipation hook on the same demo body,Parents' OK for children's faces in the footage,ready to make,,,,,,,,,,
```
