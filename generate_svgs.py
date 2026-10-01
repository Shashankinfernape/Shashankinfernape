import base64
import os
import textwrap

# Projects config: webapp=True means link icon, webapp=False means download icon
projects = [
    {
        "id": "handesk",
        "title": "HANDESK (DirectLink)",
        "desc": "High-performance remote desktop infrastructure delivering ultra-low latency screensharing. Engineered for direct systems access and highly reliable control operations.",
        "logo_path": "logos/handesk.jpg",
        "theme": "light",
        "webapp": False,
        "link": "https://github.com/Shashankinfernape/Handesk/releases/latest"
    },
    {
        "id": "chatflix",
        "title": "CHATFLIX",
        "desc": "A full-stack real-time messaging ecosystem featuring a Netflix-inspired interface. Powered by advanced JWT authentication protocols and seamless Socket.io integration.",
        "logo_path": None,
        "theme": "dark",
        "webapp": True,
        "link": "https://github.com/Shashankinfernape/Chatflix"
    },
    {
        "id": "slidepapers",
        "title": "SLIDEPAPERS",
        "desc": "A dynamic documentation and presentation engine tailored for software developers. Built to streamline interactive content delivery and optimize complex visualizations.",
        "logo_path": "logos/slidepapers.png",
        "theme": "dark",
        "webapp": True,
        "link": "https://github.com/Shashankinfernape/Slidepaper"
    },
    {
        "id": "examinar",
        "title": "EXAMINAR",
        "desc": "A cross-platform assessment environment engineered with the robust Dart framework. Provides highly secure testing parameters alongside comprehensive real-time metrics.",
        "logo_path": "logos/examinar.png",
        "theme": "dark",
        "webapp": False,
        "link": "https://github.com/Shashankinfernape/Examinar/releases/latest"
    },
    {
        "id": "territory",
        "title": "TERRITORY",
        "desc": "Advanced TypeScript-based architectural framework managing complex application state. Optimizes real-time location tracking algorithms and data sync for user clusters.",
        "logo_path": "logos/territory.png",
        "theme": "dark",
        "webapp": True,
        "link": "https://github.com/Shashankinfernape/Territory"
    },
    {
        "id": "sstraess",
        "title": "SSTRAESS",
        "desc": "High-intensity load testing and system stress simulation architectural framework. Features modernized UI tracking mechanisms to monitor active system threshold limits.",
        "logo_path": None,
        "theme": "dark",
        "webapp": False,
        "link": "https://github.com/Shashankinfernape/SSTRAESS/releases/latest"
    }
]

W = 820
H = 230

def make_svg(p):
    is_light = p["theme"] == "light"
    t = "light" if is_light else "dark"

    bg_stops      = ("#ffffff","#f2f2f7") if is_light else ("#232326","#141415")
    border_color  = "rgba(0,0,0,0.10)" if is_light else "rgba(255,255,255,0.10)"
    title_fill    = "#1d1d1f" if is_light else "#f5f5f7"
    desc_fill     = "#515154" if is_light else "#8e8e93"
    hl_fill       = "rgba(255,255,255,0.75)" if is_light else "rgba(255,255,255,0.07)"
    shadow_clr    = "rgba(0,0,0,0.18)" if is_light else "rgba(0,0,0,0.55)"

    # Google Material icons (SVG path data, 24x24 viewBox)
    # Download arrow: M5,20H19V18H5M19,9H15V3H9V9H5L12,16L19,9Z
    # Link icon:      M3.9,12C3.9,10.29 5.29,8.9 7,8.9H11V7H7A5,5 0 0,0 2,12A5,5 0 0,0 7,17H11V15.1H7C5.29,15.1 3.9,13.71 3.9,12M8,13H16V11H8V13M17,7H13V8.9H17C18.71,8.9 20.1,10.29 20.1,12C20.1,13.71 18.71,15.1 17,15.1H13V17H17A5,5 0 0,0 22,12A5,5 0 0,0 17,7Z
    icon_path = "M5,20H19V18H5M19,9H15V3H9V9H5L12,16L19,9Z" if not p["webapp"] else "M3.9,12C3.9,10.29 5.29,8.9 7,8.9H11V7H7A5,5 0 0,0 2,12A5,5 0 0,0 7,17H11V15.1H7C5.29,15.1 3.9,13.71 3.9,12M8,13H16V11H8V13M17,7H13V8.9H17C18.71,8.9 20.1,10.29 20.1,12C20.1,13.71 18.71,15.1 17,15.1H13V17H17A5,5 0 0,0 22,12A5,5 0 0,0 17,7Z"
    icon_fill = "#1976D2" if not p["webapp"] else "#43A047"
    icon_bg   = "rgba(25,118,210,0.10)" if not p["webapp"] else "rgba(67,160,71,0.10)"

    # ------- logo area -------
    logo_x, logo_y, logo_w, logo_h = 595, 28, 195, 174
    logo_rx = 14

    logo_svg = ""
    if p["logo_path"] and os.path.exists(p["logo_path"]):
        ext = p["logo_path"].split('.')[-1].lower()
        mime = {"jpg":"image/jpeg","jpeg":"image/jpeg","png":"image/png"}.get(ext,"image/png")
        with open(p["logo_path"], "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        if p["id"] == "territory":
            logo_svg = f'''
  <clipPath id="logo-clip-{p["id"]}"><rect x="10" y="10" width="{W-20}" height="{H-20}" rx="20"/></clipPath>
  <image href="data:{mime};base64,{b64}" x="10" y="10" width="{W-20}" height="{H-20}"
    preserveAspectRatio="xMidYMid slice" opacity="0.22" clip-path="url(#logo-clip-{p['id']})"/>'''
        else:
            logo_svg = f'''
  <clipPath id="logo-clip-{p["id"]}"><rect x="{logo_x}" y="{logo_y}" width="{logo_w}" height="{logo_h}" rx="{logo_rx}"/></clipPath>
  <image href="data:{mime};base64,{b64}" x="{logo_x}" y="{logo_y}" width="{logo_w}" height="{logo_h}"
    preserveAspectRatio="xMidYMid meet" opacity="0.92" clip-path="url(#logo-clip-{p['id']})"/>'''
    # For no-logo projects: just leave it blank (no more ugly text)

    # ------- text -------
    # Leave ~560px for text so logo/icon don't overlap
    wrapped = textwrap.wrap(p["desc"], width=58)
    desc_lines_svg = ""
    for i, line in enumerate(wrapped):
        desc_lines_svg += f'\n    <text font-family="-apple-system,BlinkMacSystemFont,\'SF Pro Text\',Roboto,sans-serif" font-size="15" fill="{desc_fill}" font-weight="450" x="0" y="{42 + i * 24}">{line}</text>'

    svg = f'''<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <linearGradient id="bg-grad-{p["id"]}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="{bg_stops[0]}"/>
      <stop offset="100%" stop-color="{bg_stops[1]}"/>
    </linearGradient>
    <!-- Subtle inner glow for glass feel -->
    <linearGradient id="hl-grad-{p["id"]}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="{hl_fill}"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0)"/>
    </linearGradient>
    <filter id="shadow-{p["id"]}" x="-3%" y="-3%" width="106%" height="118%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="{shadow_clr}"/>
    </filter>
    {logo_svg.strip()}
  </defs>

  <!-- Main card body -->
  <rect x="8" y="8" width="{W-16}" height="{H-16}"
    rx="22" fill="url(#bg-grad-{p['id']})"
    stroke="{border_color}" stroke-width="1.5"
    filter="url(#shadow-{p['id']})"/>

  <!-- Top glass sheen -->
  <rect x="8" y="8" width="{W-16}" height="{(H-16)//2}"
    rx="22" fill="url(#hl-grad-{p['id']})"/>

  <!-- Hairline top border highlight -->
  <rect x="9.5" y="9.5" width="{W-19}" height="4" rx="4" fill="rgba(255,255,255,0.5)"/>

  <!-- Logo or BG -->
  {'<!-- logo rendered via defs -->' if (p["logo_path"] and os.path.exists(p["logo_path"])) else ''}

  <!-- Action icon pill (top right) -->
  <a href="{p['link']}">
    <rect x="{W-76}" y="14" width="62" height="32" rx="16" fill="{icon_bg}"/>
    <g transform="translate({W-64}, 18) scale(0.83)">
      <path d="{icon_path}" fill="{icon_fill}"/>
    </g>
  </a>

  <!-- Project title -->
  <text x="34" y="52"
    font-family="-apple-system,BlinkMacSystemFont,'SF Pro Display',Roboto,sans-serif"
    font-size="22" font-weight="800" fill="{title_fill}" letter-spacing="0.4">❖ {p['title']}</text>

  <!-- Description text -->
  <g transform="translate(34, 68)">{desc_lines_svg}
  </g>
</svg>'''
    return svg

# Generate
for p in projects:
    svg_code = make_svg(p)
    with open(f"logos/{p['id']}_banner.svg", "w", encoding="utf-8") as f:
        f.write(svg_code)

print("Done — premium Apple glassy cards generated.")
