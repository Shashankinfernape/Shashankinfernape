import base64
import os
import textwrap

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

    # Glassy gradients and colors
    bg_stops      = ("#ffffff", "#f0f2f5") if is_light else ("#232326", "#141415")
    border_color  = "rgba(0,0,0,0.12)" if is_light else "rgba(255,255,255,0.15)"
    title_fill    = "#1d1d1f" if is_light else "#ffffff"
    desc_fill     = "#515154" if is_light else "#a1a1a6"
    hl_fill       = "rgba(255,255,255,0.8)" if is_light else "rgba(255,255,255,0.1)"
    shadow_clr    = "rgba(0,0,0,0.15)" if is_light else "rgba(0,0,0,0.6)"
    bg_text_fill  = "rgba(0,0,0,0.04)" if is_light else "rgba(255,255,255,0.04)"

    # Action Pills
    icon_path = "M5,20H19V18H5M19,9H15V3H9V9H5L12,16L19,9Z" if not p["webapp"] else "M3.9,12C3.9,10.29 5.29,8.9 7,8.9H11V7H7A5,5 0 0,0 2,12A5,5 0 0,0 7,17H11V15.1H7C5.29,15.1 3.9,13.71 3.9,12M8,13H16V11H8V13M17,7H13V8.9H17C18.71,8.9 20.1,10.29 20.1,12C20.1,13.71 18.71,15.1 17,15.1H13V17H17A5,5 0 0,0 22,12A5,5 0 0,0 17,7Z"
    icon_fill = "#007AFF" if not p["webapp"] else "#34C759"
    icon_bg   = "rgba(0,122,255,0.12)" if not p["webapp"] else "rgba(52,199,89,0.12)"

    # Logo coordinates for the sharp foreground logo
    logo_x, logo_y, logo_w, logo_h = 580, 25, 200, 160
    logo_rx = 16

    bg_watermark_svg = ""
    fg_logo_svg = ""

    if p["logo_path"] and os.path.exists(p["logo_path"]):
        ext = p["logo_path"].split('.')[-1].lower()
        mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png" if ext == "png" else "image/svg+xml"
        with open(p["logo_path"], "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        
        # 1. Premium Background Logo Watermark (Spans the whole card)
        bg_opacity = "0.15" if is_light else "0.25"
        bg_watermark_svg = f'''
  <image href="data:{mime};base64,{b64}" x="8" y="8" width="{W-16}" height="{H-16}"
    preserveAspectRatio="xMidYMid slice" opacity="{bg_opacity}" clip-path="url(#card-clip-{p['id']})"/>'''
        
        # 2. Sharp Foreground Logo (unless it's Territory which is fully banner-styled)
        if p["id"] != "territory":
            fg_logo_svg = f'''
  <clipPath id="logo-clip-{p['id']}"><rect x="{logo_x}" y="{logo_y}" width="{logo_w}" height="{logo_h}" rx="{logo_rx}"/></clipPath>
  <image href="data:{mime};base64,{b64}" x="{logo_x}" y="{logo_y}" width="{logo_w}" height="{logo_h}"
    preserveAspectRatio="xMidYMid meet" opacity="0.95" clip-path="url(#logo-clip-{p['id']})"/>'''
    else:
        # Huge Text Watermark for projects without logos
        bg_watermark_svg = f'''
  <text x="20" y="200" font-family="Impact, 'Arial Black', sans-serif" font-size="160" font-weight="900" fill="{bg_text_fill}" clip-path="url(#card-clip-{p['id']})">{p['title'].split(' ')[0]}</text>'''

    # Text wrapping
    wrapped = textwrap.wrap(p["desc"], width=60)
    desc_lines_svg = ""
    for i, line in enumerate(wrapped):
        desc_lines_svg += f'\n    <text font-family="-apple-system,BlinkMacSystemFont,\'Segoe UI\',Roboto,sans-serif" font-size="16" fill="{desc_fill}" font-weight="500" x="0" y="{45 + i * 26}">{line}</text>'

    svg = f'''<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <!-- Base Card Clip Path -->
    <clipPath id="card-clip-{p['id']}">
      <rect x="8" y="8" width="{W-16}" height="{H-16}" rx="22"/>
    </clipPath>

    <!-- Gradients and Shadows -->
    <linearGradient id="bg-grad-{p['id']}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="{bg_stops[0]}"/>
      <stop offset="100%" stop-color="{bg_stops[1]}"/>
    </linearGradient>
    <linearGradient id="hl-grad-{p['id']}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="{hl_fill}"/>
      <stop offset="100%" stop-color="rgba(255,255,255,0)"/>
    </linearGradient>
    <filter id="shadow-{p['id']}" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="12" stdDeviation="14" flood-color="{shadow_clr}"/>
    </filter>
  </defs>

  <!-- 1. Drop Shadow & Base Glass Layer -->
  <rect x="8" y="8" width="{W-16}" height="{H-16}"
    rx="22" fill="url(#bg-grad-{p['id']})"
    stroke="{border_color}" stroke-width="2"
    filter="url(#shadow-{p['id']})"/>

  <!-- 2. Premium Background Watermarks (Logos / Title) -->
  {bg_watermark_svg.strip()}

  <!-- 3. Top Glass Sheen Highlight -->
  <rect x="8" y="8" width="{W-16}" height="{(H-16)//2}"
    rx="22" fill="url(#hl-grad-{p['id']})"/>
  <rect x="9.5" y="9.5" width="{W-19}" height="3" rx="3" fill="rgba(255,255,255,0.4)"/>

  <!-- 4. Foreground Sharp Logo (if applicable) -->
  {fg_logo_svg.strip()}

  <!-- 5. Action Pill (Top Right) -->
  <a href="{p['link']}">
    <rect x="{W-76}" y="16" width="60" height="34" rx="17" fill="{icon_bg}"/>
    <g transform="translate({W-63}, 21) scale(0.85)">
      <path d="{icon_path}" fill="{icon_fill}"/>
    </g>
  </a>

  <!-- 6. Title and Description -->
  <text x="35" y="52"
    font-family="-apple-system,BlinkMacSystemFont,'SF Pro Display',Roboto,sans-serif"
    font-size="26" font-weight="800" fill="{title_fill}" letter-spacing="0.5">❖ {p['title']}</text>
  
  <g transform="translate(35, 72)">{desc_lines_svg}
  </g>
</svg>'''
    return svg

# Generate
for p in projects:
    svg_code = make_svg(p)
    with open(f"logos/{p['id']}_banner.svg", "w", encoding="utf-8") as f:
        f.write(svg_code)

print("Done — premium Apple glassy cards generated with dual background watermarks.")
