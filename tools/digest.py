"""Compact study digest for many ingested reels (cheap to read in bulk).

Usage: .venv\\Scripts\\python tools\\digest.py [--start N] [--count M] [--board]
Prints, per reel folder (sorted by name, or by order in curriculum/sources/_order.txt if present):
  code | uploader | likes/comments | duration | lang, caption (trimmed), transcript (no timestamps, trimmed)
--board also writes curriculum/sources/_boards/board-<start>.jpg: one row per reel, frames at 0.2 s / 1.5 s / 3 s / mid.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from reel import OUT_ROOT, exe, duration  # noqa: E402


def folders():
    order = OUT_ROOT / "_order.txt"
    if order.exists():
        codes = [c.strip() for c in order.read_text(encoding="utf-8").splitlines() if c.strip()]
        return [OUT_ROOT / f"instagram-{c}" for c in codes if (OUT_ROOT / f"instagram-{c}" / "report.md").exists()]
    return sorted(p for p in OUT_ROOT.glob("instagram-*") if (p / "report.md").exists())


def board(fs, start):
    out_dir = OUT_ROOT / "_boards"
    out_dir.mkdir(exist_ok=True)
    ff = exe("ffmpeg")
    cmd = [ff, "-y", "-v", "error"]
    filt, n = [], 0
    for f in fs:
        v = f / "video.mp4"
        d = duration(v)
        for t in (0.2, 1.5, 3.0, d / 2):
            cmd += ["-ss", f"{min(t, max(d - 0.2, 0)):.2f}", "-i", str(v)]
            filt.append(f"[{n}:v]scale=200:356:force_original_aspect_ratio=decrease,pad=200:356:(ow-iw)/2:(oh-ih)/2,setsar=1[v{n}]")
            n += 1
    layout = "|".join(f"{(i % 4) * 200}_{(i // 4) * 356}" for i in range(n))
    filt.append("".join(f"[v{i}]" for i in range(n)) + f"xstack=inputs={n}:layout={layout}[o]")
    dst = out_dir / f"board-{fs[0].name[10:]}.jpg"
    cmd += ["-filter_complex", ";".join(filt), "-map", "[o]", "-frames:v", "1", "-update", "1", "-q:v", "5", str(dst)]
    subprocess.run(cmd, check=True)
    return dst


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--count", type=int, default=8)
    ap.add_argument("--board", action="store_true")
    ap.add_argument("--todo", action="store_true", help="only reels not yet mentioned in reels-ledger.md")
    ap.add_argument("--chars", type=int, default=1400)
    a = ap.parse_args()
    fs = folders()
    if a.todo:
        led = "".join(f.read_text(encoding="utf-8") for f in sorted(OUT_ROOT.parent.glob("reels-ledger*.md")))
        fs = [f for f in fs if f.name[10:] not in led]
        print(f"TODO remaining: {len(fs)}")
    fs = fs[a.start:a.start + a.count]
    for i, f in enumerate(fs, a.start):
        info = json.loads((f / "info.json").read_text(encoding="utf-8"))
        rep = (f / "report.md").read_text(encoding="utf-8")
        lang = re.search(r"spoken language:\*\* (\S+)", rep)
        dur = re.search(r"duration:\*\* (\S+)", rep)
        tr = " ".join(re.sub(r"^\[.*?\]\s*", "", l) for l in (f / "transcript.txt").read_text(encoding="utf-8").splitlines())
        cap = re.sub(r"\s+", " ", (info.get("description") or ""))
        cap = re.sub(r"(#\w+\s*)+$", "", cap)[:260]
        print(f"### {i} {f.name[10:]} | @{info.get('channel')} | likes {info.get('like_count')} cmts {info.get('comment_count')} "
              f"| {dur.group(1) if dur else '?'} | {lang.group(1) if lang else '?'}")
        print(f"CAP: {cap}")
        print(f"SAY: {tr[:a.chars]}{' …' if len(tr) > a.chars else ''}\n")
    if a.board and fs:
        print("BOARD", board(fs, a.start), "(rows = reels in order above; cols = 0.2s, 1.5s, 3s, mid)")


if __name__ == "__main__":
    main()
