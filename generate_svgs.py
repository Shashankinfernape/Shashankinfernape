import base64
import os

projects = [
    {
        "id": "handesk",
        "title": "HANDESK (DirectLink)",
        "desc": "High-performance remote desktop infrastructure delivering ultra-low latency screensharing. Engineered for direct systems access and highly reliable control operations.",
        "logo_path": "logos/handesk.png"
    },
    {
        "id": "chatflix",
        "title": "CHATFLIX",
        "desc": "A full-stack real-time messaging ecosystem featuring a Netflix-inspired interface. Powered by advanced JWT authentication protocols and seamless Socket.io integration.",
        "logo_path": None 
    },
    {
        "id": "slidepapers",
        "title": "SLIDEPAPERS",
        "desc": "A dynamic documentation and presentation engine tailored for software developers. Built to streamline interactive content delivery and optimize complex visualizations.",
        "logo_path": "logos/slidepapers.png"
    },
    {
        "id": "examinar",
        "title": "EXAMINAR",
        "desc": "A cross-platform assessment environment engineered with the robust Dart framework. Provides highly secure testing parameters alongside comprehensive real-time metrics.",
        "logo_path": None
    },
    {
        "id": "territory",
        "title": "TERRITORY",
        "desc": "Advanced TypeScript-based architectural framework managing complex application state. Optimizes real-time location tracking algorithms and data sync for user clusters.",
        "logo_path": "logos/territory.png"
    },
    {
        "id": "sstraess",
        "title": "SSTRAESS",
        "desc": "High-intensity load testing and system stress simulation architectural framework. Features modernized UI tracking mechanisms to monitor active system threshold limits.",
        "logo_path": None
    }
]

svg_template = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <style>
      .title {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 24px; font-weight: 800; fill: #E2B714; }}
      .desc {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 15px; fill: #c9c9c9; line-height: 1.5; }}
      .bg-text {{ font-family: 'Impact', sans-serif; font-size: 120px; font-weight: 900; fill: rgba(255, 255, 255, 0.03); }}
    </style>
  </defs>
  <rect width="100%" height="100%" fill="#0D1117" rx="8"/>
  
  {bg_content}

  <g transform="translate(40, 70)">
    <text class="title" x="0" y="0">{title}</text>
    <text class="desc" x="0" y="40">{desc_line1}</text>
    <text class="desc" x="0" y="65">{desc_line2}</text>
  </g>
</svg>"""

for p in projects:
    bg_content = ""
    if p["logo_path"] and os.path.exists(p["logo_path"]):
        with open(p["logo_path"], "rb") as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
            ext = p["logo_path"].split('.')[-1]
            mime = "image/png" if ext == "png" else "image/svg+xml"
            bg_content = f'<image href="data:{mime};base64,{b64}" x="500" y="-50" width="300" height="300" opacity="0.1" />'
    elif p["id"] == "sstraess":
        bg_content = '<text class="bg-text" x="150" y="150">SSTRAESS</text>'
    else:
        bg_content = f'<text class="bg-text" x="150" y="150">{p["id"].upper()}</text>'
        
    desc_words = p["desc"].split()
    mid = len(desc_words) // 2
    desc_line1 = " ".join(desc_words[:mid+1])
    desc_line2 = " ".join(desc_words[mid+1:])
    
    svg_code = svg_template.format(
        title="❖ " + p["title"],
        desc_line1=desc_line1,
        desc_line2=desc_line2,
        bg_content=bg_content
    )
    
    with open(f"logos/{p['id']}_banner.svg", "w", encoding="utf-8") as f:
        f.write(svg_code)

print("Generated SVGs.")
