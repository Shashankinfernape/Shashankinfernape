import math

SW, SH = 860, 560
cx_m, cy_m = 430, 282
R = 152
OFF = 104

# id, label, cx, cy, highlight_color, main_color, dark_color, label_x, label_y
circles_data = [
    ("purpose",      "Purpose",      cx_m,       cy_m-OFF, "#F1948A", "#CB4335", "#7B241C", cx_m,            cy_m-OFF-int(R*0.5)),
    ("speed",        "Speed",        cx_m-OFF,   cy_m,     "#52BE80", "#1D8348", "#0B5226", cx_m-OFF-int(R*0.5), cy_m),
    ("quality",      "Quality",      cx_m+OFF,   cy_m,     "#BB8FCE", "#7D3C98", "#4A235A", cx_m+OFF+int(R*0.5), cy_m),
    ("productivity", "Productivity", cx_m,       cy_m+OFF, "#5DADE2", "#1A5276", "#0D3349", cx_m,            cy_m+OFF+int(R*0.5)),
]

intersections_data = [
    ("Consistency",     cx_m-62, cy_m-60, 11),
    ("Innovation",      cx_m+62, cy_m-60, 11),
    ("Detail-Oriented", cx_m-58, cy_m+68, 10),
    ("Scalability",     cx_m+62, cy_m+68, 11),
]

svg = f'<svg width="{SW}" height="{SH}" xmlns="http://www.w3.org/2000/svg">\n'
svg += f'  <rect width="{SW}" height="{SH}" rx="14" fill="#000000" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>\n'

# Gradients
svg += '  <defs>\n'
for (cid, label, ccx, ccy, light, main, dark, lx, ly) in circles_data:
    fx = int(ccx - R * 0.28)
    fy = int(ccy - R * 0.34)
    svg += f'    <radialGradient id="g_{cid}" cx="{ccx}" cy="{ccy}" r="{R}" fx="{fx}" fy="{fy}" gradientUnits="userSpaceOnUse">\n'
    svg += f'      <stop offset="0%" stop-color="{light}"/>\n'
    svg += f'      <stop offset="42%" stop-color="{main}"/>\n'
    svg += f'      <stop offset="100%" stop-color="{dark}"/>\n'
    svg += f'    </radialGradient>\n'
svg += '  </defs>\n'

# Circles
for (cid, label, ccx, ccy, light, main, dark, lx, ly) in circles_data:
    svg += f'  <circle cx="{ccx}" cy="{ccy}" r="{R}" fill="url(#g_{cid})" fill-opacity="0.80" stroke="{dark}" stroke-width="1.5"/>\n'

# Glossy specular highlights
for (cid, label, ccx, ccy, light, main, dark, lx, ly) in circles_data:
    hx = int(ccx - R * 0.18)
    hy = int(ccy - R * 0.33)
    svg += f'  <ellipse cx="{hx}" cy="{hy}" rx="{int(R*0.37)}" ry="{int(R*0.2)}" fill="white" fill-opacity="0.18"/>\n'

# Center core
svg += f'  <circle cx="{cx_m}" cy="{cy_m}" r="50" fill="#080808" fill-opacity="0.72" stroke="rgba(255,255,255,0.18)" stroke-width="1.2"/>\n'

# Intersection labels
for (name, ix, iy, fs) in intersections_data:
    svg += f'  <text x="{ix}" y="{iy}" font-family="\'Google Sans\', Roboto, sans-serif" font-size="{fs}" font-weight="600" fill="rgba(255,255,255,0.92)" text-anchor="middle" dominant-baseline="middle">{name}</text>\n'

# Center text
svg += f'  <text x="{cx_m}" y="{cy_m-9}" font-family="\'Google Sans\', Roboto, sans-serif" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">What I</text>\n'
svg += f'  <text x="{cx_m}" y="{cy_m+9}" font-family="\'Google Sans\', Roboto, sans-serif" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">Value</text>\n'

# Main circle labels (bold, in outer region of each circle)
for (cid, label, ccx, ccy, light, main, dark, lx, ly) in circles_data:
    svg += f'  <text x="{lx}" y="{ly}" font-family="\'Google Sans\', Roboto, sans-serif" font-size="22" font-weight="700" fill="#ffffff" text-anchor="middle" dominant-baseline="middle">{label}</text>\n'

svg += '</svg>\n'

with open("logos/dev_dna.svg", "w", encoding="utf-8") as f:
    f.write(svg)
print("dev_dna.svg (Venn diagram) done")
