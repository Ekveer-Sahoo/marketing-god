# marketing-god — working rules

A Claude Code plugin that makes Claude a top-tier marketer. Built by learning each topic properly,
then encoding it, then battle-testing it on 100+ products.

## Layout
- `.claude-plugin/plugin.json` — manifest
- `skills/` — one folder per skill (`skills/<name>/SKILL.md`), only after a topic is learned and tested
- `agents/` — subagents (e.g. creative director / critic)
- `commands/` — slash commands
- `curriculum/` — teaching notes per topic, the "textbook" (raw source → distilled understanding)
- `lab/` — product testing + error-minimization loop (see `lab/README.md`)

## Workflow per topic
1. User sends source material → save distilled notes to `curriculum/NN-<topic>.md`:
   core principle, why it works (psychology), when it fails, real examples, common mistakes.
2. Teach it back: explain, quiz, apply to a sample product.
3. Add rubric criteria for the topic to `lab/rubric.md` and seed error tags.
4. Write/update the skill in `skills/`.
5. Run it through the lab; promote recurring errors to rules (`lab/learnings.md`) and back into the skill.

## Studying reels / videos
`.venv\Scripts\python tools\reel.py <url> [<url> ...]` → `curriculum/sources/<site>-<id>/` with
`report.md` (metadata, caption, timestamped transcript), `hook.jpg` (first 3 s, 3 fps), `sheet.jpg`
(whole video, ≤24 frames). Read report + both images, then fill the Breakdown section.
Instagram/TikTok may need login: add `--cookies-from-browser firefox` (Chrome cookie access is often
blocked on Windows). Whisper runs on GPU (large-v3-turbo), falls back to CPU small.

Bulk study: `tools\reel.py --file urls.txt` (skips done ones, logs failures), then
`tools\digest.py --todo --count 14 --board` prints compact digests of reels not yet in `curriculum/reels-ledger.md`
and writes a hook board image (rows = reels; frames at 0.2 s, 1.5 s, 3 s, mid). Set `PYTHONIOENCODING=utf-8`.
Known limits: Whisper drops chunks of Hindi/Hinglish audio (trust on-screen text and captions); image carousels and
login-gated reels need the browser. Every reel studied gets a ledger entry; lessons go into the numbered topic files.

## Rules
- No skill content without a source in `curriculum/` or evidence in `lab/`.
- Skills hold distilled, actionable rules + good/bad examples, not textbook dumps.
- Video generation uses the Higgsfield MCP; build on the existing `higgsfield-expert` skill, don't duplicate it.
- Otto integration: TBD (user will explain later).
