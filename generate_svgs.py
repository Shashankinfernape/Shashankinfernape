import base64
import os
import textwrap

projects = [
    {
        "id": "handesk",
        "title": "HANDESK (DirectLink)",
        "desc": "High-performance remote desktop infrastructure delivering ultra-low latency screensharing. Engineered for direct systems access and highly reliable control operations.",
        "logo_path": "logos/handesk.jpg",
        "theme": "light"
    },
    {
        "id": "chatflix",
        "title": "CHATFLIX",
        "desc": "A full-stack real-time messaging ecosystem featuring a Netflix-inspired interface. Powered by advanced JWT authentication protocols and seamless Socket.io integration.",
        "logo_path": None,
        "theme": "dark"
    },
    {
        "id": "slidepapers",
        "title": "SLIDEPAPERS",
        "desc": "A dynamic documentation and presentation engine tailored for software developers. Built to streamline interactive content delivery and optimize complex visualizations.",
        "logo_path": "logos/slidepapers.png",
        "theme": "dark"
    },
    {
        "id": "examinar",
        "title": "EXAMINAR",
        "desc": "A cross-platform assessment environment engineered with the robust Dart framework. Provides highly secure testing parameters alongside comprehensive real-time metrics.",
        "logo_path": "logos/examinar.png",
        "theme": "dark"
    },
    {
        "id": "territory",
        "title": "TERRITORY",
        "desc": "Advanced TypeScript-based architectural framework managing complex application state. Optimizes real-time location tracking algorithms and data sync for user clusters.",
        "logo_path": "logos/territory.png",
        "theme": "dark"
    },
    {
        "id": "sstraess",
        "title": "SSTRAESS",
        "desc": "High-intensity load testing and system stress simulation architectural framework. Features modernized UI tracking mechanisms to monitor active system threshold limits.",
        "logo_path": None,
        "theme": "dark"
    }
]

svg_template = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <!-- Glassy Drop Shadow -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="#000000" flood-opacity="{shadow_opacity}" />
    </filter>

    <!-- Dark Mode Gradient -->
    <linearGradient id="bg-dark" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2c2c2e" />
      <stop offset="100%" stop-color="#151516" />
    </linearGradient>

    <!-- Light Mode Gradient (Handesk) -->
    <linearGradient id="bg-light" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#f5f5f7" />
    </linearGradient>

    <!-- Clip Paths for beautifully rounded images -->
    <clipPath id="card-clip">
      <rect x="10" y="10" width="780" height="180" rx="20"/>
    </clipPath>
    <clipPath id="logo-clip">
      <rect x="560" y="25" width="210" height="150" rx="14"/>
    </clipPath>

    <style>
      .title-dark {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 24px; font-weight: 800; fill: #ffffff; letter-spacing: 0.5px; }}
      .desc-dark {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 15px; fill: #a1a1a6; line-height: 1.6; font-weight: 500; }}
      
      .title-light {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 24px; font-weight: 800; fill: #1d1d1f; letter-spacing: 0.5px; }}
      .desc-light {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 15px; fill: #515154; line-height: 1.6; font-weight: 500; }}
    </style>
  </defs>

  <!-- Glassy Base -->
  <rect x="10" y="10" width="780" height="180" fill="{bg_fill}" rx="20" filter="url(#shadow)" stroke="{stroke_color}" stroke-width="1.5" />
  
  <!-- Subtle Top Inner Highlight for Glassy Apple look -->
  <path d="M 30 11 L 770 11 C 780.5 11 789 19.5 789 30 L 789 50 C 789 19.5 780.5 11 770 11 L 30 11 C 19.5 11 11 19.5 11 30 L 11 50 C 11 19.5 19.5 11 30 11 Z" fill="{highlight_color}" opacity="0.6"/>

  <!-- Background / Logo Area -->
  {bg_content}

  <!-- Foreground Text -->
  <g transform="translate(45, 65)">
    <text class="title-{theme}" x="0" y="0">{title}</text>
    {desc_svg}
  </g>
</svg>"""

for p in projects:
    bg_content = ""
    is_light = (p.get("theme") == "light")
    
    theme_vars = {
        "theme": "light" if is_light else "dark",
        "bg_fill": "url(#bg-light)" if is_light else "url(#bg-dark)",
        "stroke_color": "rgba(0,0,0,0.12)" if is_light else "rgba(255,255,255,0.12)",
        "shadow_opacity": "0.15" if is_light else "0.4",
        "highlight_color": "#ffffff" if is_light else "#ffffff",
    }

    if p["logo_path"] and os.path.exists(p["logo_path"]):
        with open(p["logo_path"], "rb") as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            ext = p["logo_path"].split('.')[-1].lower()
            mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png" if ext == "png" else "image/svg+xml"
            
            # Special layouts
            if p["id"] == "territory":
                # Territory spans the whole card background
                bg_content = f'<image href="data:{mime};base64,{b64}" x="10" y="10" width="780" height="180" preserveAspectRatio="xMidYMid slice" opacity="0.35" clip-path="url(#card-clip)"/>'
            else:
                # Other logos (Handesk, Slidepapers, Examinar) elegantly sit on the right with meet and rounded corners
                bg_content = f'<image href="data:{mime};base64,{b64}" x="560" y="25" width="210" height="150" preserveAspectRatio="xMidYMid meet" opacity="0.9" clip-path="url(#logo-clip)"/>'

    elif p["id"] == "chatflix":
        # Cool SVG Icon for Chatflix instead of ugly text
        bg_content = '<g transform="translate(610, 40) scale(5)"><path fill="#E50914" opacity="0.4" d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-6 9.5l-6 3.5v-7l6 3.5z"/></g>'
    elif p["id"] == "sstraess":
        # Cool SVG Icon for SSTRAESS (Activity Monitor Line Chart)
        bg_content = '<g transform="translate(590, 40) scale(4.5)"><path fill="#E2B714" opacity="0.25" d="M21 3H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H3V5h18v14zM9.5 15.5L13 11l2.5 3.5L20 8.5 18.5 7 15.5 11l-2.5-3.5L9 12.5 7.5 9 4 14l1.5 1.5L9.5 12z"/></g>'
        
    # Text wrapping to ensure it NEVER overlaps the logo on the right side
    # 58 chars max ensures the text stops around x=500, leaving right area clear
    wrapped_desc = textwrap.wrap(p["desc"], width=62)
    desc_svg = ""
    for i, line in enumerate(wrapped_desc):
        desc_svg += f'<text class="desc-{theme_vars["theme"]}" x="0" y="{35 + i*24}">{line}</text>\n    '
    
    svg_code = svg_template.format(
        title="❖ " + p["title"],
        desc_svg=desc_svg,
        bg_content=bg_content,
        **theme_vars
    )
    
    with open(f"logos/{p['id']}_banner.svg", "w", encoding="utf-8") as f:
        f.write(svg_code)

print("Generated Auto-Wrapped Glassy Apple UI SVGs.")
