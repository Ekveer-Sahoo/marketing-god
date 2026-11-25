"""Ingest a reel/short/video so Claude can study it.

Usage:
  .venv\\Scripts\\python tools\\reel.py <url> [<url> ...] [--cookies-from-browser firefox] [--model large-v3-turbo]

For each URL, writes to curriculum/sources/<extractor>-<id>/:
  video.mp4      the video (gitignored)
  hook.jpg       first 3 s at 3 fps, timestamped (the scroll-stop window)
  sheet.jpg      whole video, up to 24 timestamped frames
  transcript.txt timestamped speech transcript (auto language detect)
  report.md      metadata (caption, views, likes...) + transcript + image refs
"""
import argparse
import json
import math
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_ROOT = ROOT / "curriculum" / "sources"
LINKS = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Links"
os.environ["PATH"] = str(LINKS) + os.pathsep + os.environ.get("PATH", "")  # deno/ffmpeg for yt-dlp
# Biases Whisper toward spelling niche names right (it heard "Claude" as "Cloud").
VOCAB = ("Claude, Anthropic, ChatGPT, OpenAI, Higgsfield, Instagram, TikTok, Reels, Meta ads, "
         "ROAS, CTR, CPA, CPM, UGC, hook, funnel, landing page, Hormozi")
FONT ="C\\:/Windows/Fonts/arial.ttf"
STAMP = f"drawtext=fontfile='{FONT}':text='%{{pts\\:hms}}':x=8:y=8:fontsize=36:fontcolor=white:box=1:boxcolor=black@0.6"


def exe(name):
    found = shutil.which(name) or (LINKS / f"{name}.exe")
    if not Path(found).exists():  # winget sometimes skips the Links alias; look in Packages
        hits = sorted((LINKS.parent / "Packages").glob(f"**/{name}.exe"))
        found = hits[-1] if hits else found
    if not Path(found).exists():
        sys.exit(f"{name} not found. Install it (winget) or open a new shell so PATH updates.")
    return str(found)


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, text=True, encoding="utf-8", errors="replace", **kw)


def download(url, cookies_browser):
    ytdlp = exe("yt-dlp")
    cmd = [ytdlp, "--no-playlist", "-J", url]
    if cookies_browser:
        cmd[1:1] = ["--cookies-from-browser", cookies_browser]
    info = json.loads(run(cmd, capture_output=True).stdout)
    out = OUT_ROOT / f"{info.get('extractor_key', 'video').lower()}-{info['id']}"
    out.mkdir(parents=True, exist_ok=True)
    dl = [ytdlp, "--no-playlist", "--no-progress", "-f", "bv*[height<=1080]+ba/b", "--merge-output-format", "mp4",
          "--ffmpeg-location", str(Path(exe("ffmpeg")).parent), "-o", str(out / "video.%(ext)s"), url]
    if cookies_browser:
        dl[1:1] = ["--cookies-from-browser", cookies_browser]
    if not (out / "video.mp4").exists():
        run(dl)
    (out / "info.json").write_text(json.dumps(info, indent=2, ensure_ascii=False), encoding="utf-8")
    return out, info


def duration(video):
    r = run([exe("ffprobe"), "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video)],
            capture_output=True)
    return float(r.stdout.strip())


def frames(video, out, dur):
    ff = exe("ffmpeg")
    # Hook window: first 3 s at 3 fps -> 3x3 grid
    run([ff, "-y", "-v", "error", "-t", "3", "-i", str(video), "-vf",
         f"{STAMP},fps=3,scale=360:-2,tile=3x3", "-frames:v", "1", "-update", "1", str(out / "hook.jpg")])
    # Whole video: up to 24 frames, 4 columns
    n = min(24, max(4, math.ceil(dur / 2)))
    rows = math.ceil(n / 4)
    run([ff, "-y", "-v", "error", "-i", str(video), "-vf",
         f"{STAMP},fps={n / dur:.4f},scale=320:-2,tile=4x{rows}", "-frames:v", "1", "-update", "1",
         str(out / "sheet.jpg")])


_MODELS = {}


def transcribe(video, model_name):
    if not _MODELS.get("dll_paths_added"):  # once per process: PATH must not grow with every video
        _MODELS["dll_paths_added"] = True
        for pkg in ("cublas", "cudnn"):
            try:
                import importlib
                mod = importlib.import_module(f"nvidia.{pkg}")
                os.add_dll_directory(str(Path(mod.__path__[0]) / "bin"))
                os.environ["PATH"] = str(Path(mod.__path__[0]) / "bin") + os.pathsep + os.environ["PATH"]
            except Exception:
                pass
    import numpy as np
    from faster_whisper import WhisperModel
    pcm = subprocess.run([exe("ffmpeg"), "-v", "error", "-i", str(video), "-ac", "1", "-ar", "16000",
                          "-f", "f32le", "-"], check=True, capture_output=True).stdout
    audio = np.frombuffer(pcm, dtype=np.float32)
    if audio.size == 0:
        return "none", []
    try:
        if "gpu" not in _MODELS:
            try:
                _MODELS["gpu"] = WhisperModel(model_name, device="cuda", compute_type="float16")
            except ValueError:  # older cards (e.g. Quadro P4000) have no float16
                _MODELS["gpu"] = WhisperModel(model_name, device="cuda", compute_type="float32")
        segs, info = _MODELS["gpu"].transcribe(audio, vad_filter=True, initial_prompt=VOCAB)
        segs = list(segs)
    except Exception as e:
        print(f"GPU transcription failed ({e}); falling back to CPU 'small'.")
        if "cpu" not in _MODELS:
            _MODELS["cpu"] = WhisperModel("small", device="cpu", compute_type="int8")
        segs, info = _MODELS["cpu"].transcribe(audio, vad_filter=True)
        segs = list(segs)
    lines = [f"[{s.start:6.2f}-{s.end:6.2f}] {s.text.strip()}" for s in segs]
    return info.language, lines


def report(out, info, dur, lang, lines):
    keys = ["title", "uploader", "channel", "upload_date", "view_count", "like_count", "comment_count",
            "repost_count", "webpage_url"]
    meta = "\n".join(f"- **{k}:** {info.get(k)}" for k in keys if info.get(k) is not None)
    desc = (info.get("description") or "").strip()
    md = f"""# {info.get('title') or info['id']}

{meta}
- **duration:** {dur:.1f}s
- **spoken language:** {lang}

## Caption
{desc or '_none_'}

## Frames
- Hook (0-3 s): hook.jpg
- Full video: sheet.jpg

## Transcript
```
{chr(10).join(lines) or '(no speech detected)'}
```

## Breakdown
_(to fill: hook type, structure, retention devices, CTA, why it works, what to steal)_
"""
    (out / "report.md").write_text(md, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="*")
    ap.add_argument("--file", help="text file with one URL per line")
    ap.add_argument("--cookies-from-browser", default=None)
    ap.add_argument("--model", default="large-v3-turbo")
    a = ap.parse_args()
    urls = list(a.urls)
    if a.file:
        urls += [u.strip() for u in Path(a.file).read_text(encoding="utf-8").splitlines() if u.strip()]
    failed = []
    for url in urls:
        code = url.rstrip("/").split("/")[-1]
        if (OUT_ROOT / f"instagram-{code}" / "report.md").exists():
            print(f"SKIP {code}", flush=True)
            continue
        try:
            out, info = download(url, a.cookies_from_browser)
            video = out / "video.mp4"
            dur = duration(video)
            frames(video, out, dur)
            lang, lines = transcribe(video, a.model)
            (out / "transcript.txt").write_text("\n".join(lines), encoding="utf-8")
            report(out, info, dur, lang, lines)
            print(f"OK {out.name}", flush=True)
        except Exception as e:
            msg = getattr(e, "stderr", None) or str(e)
            print(f"FAIL {url} :: {str(msg).strip()[-300:]}", flush=True)
            failed.append(url)
    if failed:
        with (OUT_ROOT / "_failed.txt").open("a", encoding="utf-8") as fh:
            fh.write("\n".join(failed) + "\n")


if __name__ == "__main__":
    main()
