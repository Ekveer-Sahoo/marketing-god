"""Generate assets/banner.svg.

Design rules borrowed from two open skills (read, not installed):
- stack-diagram (caru-ini): near-white paper with a 24 px graph grid, white rounded tiles with a hairline
  border and faint shadow, name in a semibold sans with the role in small muted mono, one tinted group
  box with its label top-left, orthogonal arrows in a single accent colour with mono edge labels on a
  paper-coloured halo, dashed line for the secondary flow, icons instead of emoji.
- pixelfx (patch-gg): pixel icons on a hard grid, small palettes with hard ramp steps, one clean ink
  line, no smooth gradients or anti-aliasing, no lone noise pixels.
Sizes are scaled up about 1.3x from stack-diagram's because this is a README banner, not a full diagram.
Run: python assets/make_banner.py
"""
from pathlib import Path

W, H = 1000, 470
PAPER, GRID, INK, MUTED, HAIR = "#f7f8fa", "#e8ebf1", "#1b1f2a", "#667085", "#dde2ea"
ACCENT = "#2f6bef"
GROUP_FILL, GROUP_LINE, GROUP_TEXT = "#fff5ea", "#f0b17a", "#a8590f"
SANS = "Geist,'Segoe UI',-apple-system,Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono','SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"

TILE, PX = 76, 4          # tile size; one icon pixel = 4 px (12 x 12 grid = 48 px)
TOP = 236                 # tile top
XS = [85, 255, 425, 595, 765, 915]  # tile centres: input, 4 skills, output

ICONS = {
    "input": ("""
............
.KKKKKKKKKK.
.KWWWWWWWWK.
.KWBBBBBBWK.
.KWWWWWWWWK.
.KWBBBBWWWK.
.KWWWWWWWWK.
.KKKKKKKKKK.
...KK.......
...K........
............
............""", {"K": INK, "W": "#ffffff", "B": "#9db8f5"}),
    "audience": ("""
....KKKK....
..KKBBBBKK..
.KBBWWBBBBK.
.KBWBBBBBBK.
KBBWBBBBBBBK
KBBBBBBBBBBK
KBBBBBBBBBBK
.KBBBBBBBBK.
.KBBBBBBBBK.
..KKBBBBKKK.
....KKKK.KHK
..........KK""", {"K": INK, "B": "#bcd0fa", "W": "#ffffff", "H": "#c9772b"}),
    "hooks": ("""
.....KKKK...
.....KOOK...
.....KKKK...
......KSK...
......KSK...
......KSK...
.K....KSK...
KSK...KSK...
KSSK..KSK...
KSSSKKSSK...
.KSSSSSK....
..KKKKK.....""", {"K": INK, "S": "#aab4c5", "O": "#f08a3c"}),
    "matrix": ("""
............
.KKKKKKKKKK.
.KAAKAAKAAK.
.KAAKAAKAAK.
.KKKKKKKKKK.
.KAAKGGKAAK.
.KAAKGGKAAK.
.KKKKKKKKKK.
.KAAKAAKAAK.
.KAAKAAKAAK.
.KKKKKKKKKK.
............""", {"K": INK, "A": "#dbe6fd", "G": "#f08a3c"}),
    "video": ("""
............
.KKKKKKKKKK.
.KWKWKWKWKK.
.KKWKWKWKWK.
.KKKKKKKKKK.
.KDDDDDDDDK.
.KDDDRDDDDK.
.KDDDRRDDDK.
.KDDDRRRDDK.
.KDDDRRDDDK.
.KDDDRDDDDK.
.KKKKKKKKKK.""", {"K": INK, "W": "#ffffff", "D": "#39445a", "R": "#f08a3c"}),
    "output": ("""
...KKKKKK...
...KDDDDK...
...KDDDDK...
...KDRDDK...
...KDRRDK...
...KDRRRK...
...KDRRDK...
...KDRDDK...
...KDDDDK...
...KDDDDK...
...KKWWKK...
...KKKKKK...""", {"K": INK, "D": "#39445a", "R": "#f08a3c", "W": "#ffffff"}),
}

NODES = [
    ("input", "Your product", "+ customer messages"),
    ("audience", "audience-research", "who buys, why not"),
    ("hooks", "hooks", "first 3 seconds"),
    ("matrix", "ad-matrix", "a batch to test"),
    ("video", "video-ads", "real proof, then AI"),
    ("output", "Reel or ad", "ready to run"),
]
EDGES = ["", "audience.md", "scored hooks", "ad-matrix.csv", ""]


def icon(name, cx):
    rows, pal = ICONS[name]
    rows = [r for r in rows.strip("\n").split("\n")]
    x0, y0 = cx - 6 * PX, TOP + (TILE - 12 * PX) // 2
    out = []
    for r, row in enumerate(rows):
        c = 0
        while c < len(row):          # merge runs so the file stays small
            ch = row[c]
            n = 1
            while c + n < len(row) and row[c + n] == ch:
                n += 1
            if ch in pal:
                out.append(f'<rect x="{x0 + c * PX}" y="{y0 + r * PX}" width="{n * PX}" height="{PX}" fill="{pal[ch]}"/>')
            c += n
    return "".join(out)


def sparkle(x, y, colour):
    p = PX
    return (f'<rect x="{x}" y="{y - p}" width="{p}" height="{3 * p}" fill="{colour}"/>'
            f'<rect x="{x - p}" y="{y}" width="{3 * p}" height="{p}" fill="{colour}"/>')


s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
     f'aria-label="marketing-god: your product and customer messages flow through audience-research, hooks, '
     f'ad-matrix and video-ads to a reel or ad">',
     '<defs>'
     f'<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="{GRID}" stroke-width="1"/></pattern>'
     f'<marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5L0 10z" fill="{ACCENT}"/></marker>'
     f'<marker id="m" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0L10 5L0 10z" fill="{MUTED}"/></marker>'
     '<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#1b1f2a" flood-opacity="0.08"/></filter>'
     '<clipPath id="r"><rect width="1000" height="470" rx="20"/></clipPath>'
     '</defs>',
     f'<g clip-path="url(#r)"><rect width="{W}" height="{H}" fill="{PAPER}"/><rect width="{W}" height="{H}" fill="url(#grid)"/></g>',
     f'<rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="20" fill="none" stroke="{HAIR}" stroke-width="1.5"/>']

# Title block
s.append(f'<g shape-rendering="crispEdges">{sparkle(52, 62, ACCENT)}{sparkle(72, 46, "#f08a3c")}</g>')
s.append(f'<text x="98" y="78" font-family="{SANS}" font-size="46" font-weight="800" letter-spacing="-1" fill="{INK}">marketing-god</text>')
s.append(f'<text x="48" y="118" font-family="{SANS}" font-size="18" fill="{MUTED}">Four Claude Code skills that take a product from customer research to tested ads and video.</text>')

# Group box around the four skills
gx0, gx1 = XS[1] - 82, XS[4] + 82
s.append(f'<rect x="{gx0}" y="{TOP - 46}" width="{gx1 - gx0}" height="{TILE + 46 + 78}" rx="14" fill="{GROUP_FILL}" stroke="{GROUP_LINE}" stroke-width="1.5"/>')
s.append(f'<text x="{gx0 + 16}" y="{TOP - 22}" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="0.6" fill="{GROUP_TEXT}">THE PLUGIN</text>')

# Edges (orthogonal, accent, mono labels with a paper halo)
cy = TOP + TILE // 2
for i, label in enumerate(EDGES):
    x0, x1 = XS[i] + TILE // 2 + 6, XS[i + 1] - TILE // 2 - 8
    s.append(f'<line x1="{x0}" y1="{cy}" x2="{x1}" y2="{cy}" stroke="{ACCENT}" stroke-width="2" marker-end="url(#a)"/>')
    if label:
        halo = GROUP_FILL
        s.append(f'<text x="{(x0 + x1) // 2 - 1}" y="{cy - 10}" text-anchor="middle" font-family="{MONO}" font-size="10.5" '
                 f'fill="{INK}" stroke="{halo}" stroke-width="4" paint-order="stroke" stroke-linejoin="round">{label}</text>')

# Secondary flow: real results back to research (dashed, neutral, orthogonal)
by = TOP + TILE + 106
s.append(f'<path d="M{XS[5]} {TOP + TILE + 52}V{by}H{XS[1]}V{TOP + TILE + 86}" fill="none" stroke="{MUTED}" stroke-width="1.6" '
         f'stroke-dasharray="6 5" marker-end="url(#m)"/>')
s.append(f'<text x="{(XS[1] + XS[5]) // 2}" y="{by + 4}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{MUTED}" '
         f'stroke="{PAPER}" stroke-width="6" paint-order="stroke" stroke-linejoin="round">real results feed the next round</text>')

# Tiles, pixel icons, names and roles
for (key, name, role), cx in zip(NODES, XS):
    s.append(f'<rect x="{cx - TILE // 2}" y="{TOP}" width="{TILE}" height="{TILE}" rx="15" fill="#ffffff" stroke="{HAIR}" stroke-width="1.2" filter="url(#sh)"/>')
    s.append(f'<g shape-rendering="crispEdges">{icon(key, cx)}</g>')
    s.append(f'<text x="{cx}" y="{TOP + TILE + 26}" text-anchor="middle" font-family="{SANS}" font-size="15.5" font-weight="650" fill="{INK}">{name}</text>')
    s.append(f'<text x="{cx}" y="{TOP + TILE + 44}" text-anchor="middle" font-family="{MONO}" font-size="10.5" fill="{MUTED}">{role}</text>')

s.append("</svg>")
out = Path(__file__).with_name("banner.svg")
out.write_text("\n".join(s) + "\n", encoding="utf-8", newline="\n")
print("wrote", out, len("\n".join(s)), "bytes")
