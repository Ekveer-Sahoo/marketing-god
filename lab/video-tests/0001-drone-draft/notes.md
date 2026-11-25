# Video test 0001 — drone draft (pipeline test, not an ad)

- **Date:** 2026-11-25
- **Purpose:** first run of the `video-ads` skill past the money gate. No real product; a free-licence stock photo stood in.
- **Source photo:** Pexels "Close-up of a Flying Drone" (photo 16556196), imported by URL. Licence page for this photo not read.
- **Tool:** Higgsfield, Seedance 2.5, omni_reference with the photo as start image, 4 s, 9:16, draft (480p), no audio.
- **Cost:** quoted 12 credits before and after attaching the photo; approved by the user for one draft. Balance before: 684.5.
- **Files:** `draft.mp4`, `sheet.jpg` (8 frames at 2 fps), kept locally and not published because a third-party logo is visible.

## Prompt
The drone from the first frame hovers low over the empty road, rotors spinning, body swaying slightly in the wind. After one second it tilts
forward and accelerates straight toward the camera, growing large in frame and passing just overhead. Static low camera, shallow depth of
field, soft overcast light, muted colour. The drone keeps exactly the same shape, colour and details as in the first frame. No text, no logos.

## Review (from the frame sheet; the clip was not watched at full speed or with a human eye)
| Check | Result |
|---|---|
| Product fidelity | Pass. Shape, colour and proportions match the start photo through the move. |
| Artifacts | None visible at sheet size (270 px wide frames). Not checked at full resolution. |
| Motion vs prompt | **Partly wrong.** Hover (0-1.5 s) and approach to extreme close-up (~2.5 s) are right. It then does not pass overhead: by 3-3.5 s the drone is small and distant again, as if it reset or backed away. |
| Brand / honesty | **Fail for any real use.** A legible "DJI" logo appears on the drone in the close-up. The stock photo is of a real commercial drone, and zooming in made the mark readable despite "no logos" in the prompt. |
| Hook strength | Weak as an opener: the first 1.5 s is a near-static hover. The interesting part starts at 2 s. |
| Format | 480x854, 24 fps, 4.04 s. Correct shape; draft resolution. |

**Verdict:** the pipeline works end to end (import → quote → approve → generate → download → review). The clip itself is not usable.
No retry was run; the approval covered one draft.

## What this taught the skill
1. A stock or third-party photo of a branded product carries the brand into the video, and a camera move toward it can make a logo
   readable that wasn't in the still. Inspect the source at full size for marks first; "no logos" in the prompt does not remove them.
2. Exits like "passes overhead" are unreliable; the model brought the subject back. Describe one continuous move with a stated end frame,
   or supply an end image.
3. For a hook, put the motion in the first second; don't spend the opening on a hover.
4. Review from a frame sheet catches structure and branding, not flicker or fine artifacts. Say which checks were done.
- **Balance after:** 672.5 (12 credits spent, as quoted).
