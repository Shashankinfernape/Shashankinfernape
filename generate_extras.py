import math

# =============================================
# 1. LANGUAGE BAR SVG
# =============================================
langs = [
    ("TypeScript", "#3178C6", 28),
    ("Kotlin",     "#7F52FF", 20),
    ("Dart",       "#00B4AB", 16),
    ("JavaScript", "#F7DF1E", 14),
    ("Rust",       "#CE422B", 12),
    ("Python",     "#3572A5", 10),
]
total = sum(x[2] for x in langs)
W, H = 860, 110
bar_y, bar_h = 44, 12
bar_x = 20
bar_w = W - 40

svg = f'<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg">\n'
svg += f'  <rect width="{W}" height="{H}" rx="14" fill="#000000" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>\n'
svg += f'  <text x="{W//2}" y="22" font-family="\'Google Sans\', Roboto, sans-serif" font-size="10" font-weight="600" fill="rgba(255,255,255,0.35)" text-anchor="middle" letter-spacing="3">MOST USED LANGUAGES</text>\n'

# Clip path for rounded bar
svg += f'  <defs><clipPath id="bar-clip"><rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="6"/></clipPath></defs>\n'
cx = bar_x
for name, color, pct in langs:
    seg_w = int((pct / total) * bar_w)
    svg += f'  <rect x="{cx}" y="{bar_y}" width="{seg_w}" height="{bar_h}" fill="{color}" clip-path="url(#bar-clip)"/>\n'
    cx += seg_w

# Legend
lx = 20
ly = 78
for i, (name, color, pct) in enumerate(langs):
    pct_label = f"{round((pct/total)*100)}%"
    svg += f'  <circle cx="{lx+5}" cy="{ly}" r="4" fill="{color}"/>\n'
    svg += f'  <text x="{lx+14}" y="{ly+4}" font-family="Roboto, sans-serif" font-size="12" fill="#e8e8e8">{name} <tspan fill="#555">{pct_label}</tspan></text>\n'
    lx += 143

svg += '</svg>\n'

with open("logos/lang_visual.svg", "w", encoding="utf-8") as f:
    f.write(svg)
print("lang_visual.svg done")


# =============================================
# 2. DEVELOPER DNA — Bubble Cluster SVG
# =============================================
SW, SH = 860, 320

values = [
    ("Purpose",         "#9D4EDD", 0.95),
    ("Quality",         "#00C4B3", 0.90),
    ("Innovation",      "#E50914", 0.88),
    ("Scalability",     "#3178C6", 0.82),
    ("Productivity",    "#F5A623", 0.80),
    ("Detail-Oriented", "#00A4EF", 0.75),
    ("Consistency",     "#7F52FF", 0.72),
    ("Speed",           "#3ddc84", 0.65),
]

# Circle positions — arranged in a ring around center
cx_c, cy_c = SW // 2, SH // 2
ring_r = 110
angle_step = 2 * math.pi / len(values)
center_r = 52

dna = f'<svg width="{SW}" height="{SH}" xmlns="http://www.w3.org/2000/svg">\n'
dna += f'  <rect width="{SW}" height="{SH}" rx="14" fill="#000000" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>\n'
dna += f'  <text x="{SW//2}" y="22" font-family="\'Google Sans\', Roboto, sans-serif" font-size="10" font-weight="600" fill="rgba(255,255,255,0.35)" text-anchor="middle" letter-spacing="3">DEVELOPER DNA</text>\n'

# Draw connecting lines from center to each bubble first (behind)
for i, (name, color, weight) in enumerate(values):
    angle = i * angle_step - math.pi / 2
    bx = cx_c + ring_r * math.cos(angle)
    by = cy_c + ring_r * math.sin(angle)
    dna += f'  <line x1="{cx_c}" y1="{cy_c}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{color}" stroke-width="1" stroke-opacity="0.15"/>\n'

# Draw outer bubbles
for i, (name, color, weight) in enumerate(values):
    angle = i * angle_step - math.pi / 2
    bx = cx_c + ring_r * math.cos(angle)
    by = cy_c + ring_r * math.sin(angle)
    r = int(28 + weight * 14)  # radius scales with weight
    pct = int(weight * 100)

    dna += f'  <circle cx="{bx:.1f}" cy="{by:.1f}" r="{r}" fill="{color}" fill-opacity="0.12" stroke="{color}" stroke-width="1.5" stroke-opacity="0.6"/>\n'
    dna += f'  <text x="{bx:.1f}" y="{by:.1f}" font-family="\'Google Sans\', Roboto, sans-serif" font-size="9" font-weight="700" fill="{color}" text-anchor="middle" dominant-baseline="middle">{name}</text>\n'
    dna += f'  <text x="{bx:.1f}" y="{by + 11:.1f}" font-family="Roboto, sans-serif" font-size="8" fill="rgba(255,255,255,0.4)" text-anchor="middle">{pct}%</text>\n'

# Center core
dna += f'  <circle cx="{cx_c}" cy="{cy_c}" r="{center_r}" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>\n'
dna += f'  <text x="{cx_c}" y="{cy_c - 8}" font-family="\'Google Sans\', Roboto, sans-serif" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">What Truly</text>\n'
dna += f'  <text x="{cx_c}" y="{cy_c + 7}" font-family="\'Google Sans\', Roboto, sans-serif" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">Matters</text>\n'

dna += '</svg>\n'

with open("logos/dev_dna.svg", "w", encoding="utf-8") as f:
    f.write(dna)
print("dev_dna.svg done")
