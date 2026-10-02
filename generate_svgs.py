import os
import base64

projects = [
    {
        "id": "handesk",
        "title": "HANdesk",
        "desc_lines": [
            "High-performance remote desktop infrastructure built around",
            "low-latency screen streaming and reliable remote control."
        ],
        "tags": "Rust • Windows • DXGI • H.264 • P2P",
        "color": "#00A4EF",
        "icon_type": "svg",
        "icon_svg": '<path fill="currentColor" d="M4 6h16v10H4z" opacity="0.2"/><path fill="currentColor" d="M20 4H4c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h6v2H8v2h8v-2h-2v-2h6c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zM4 16V6h16v10H4z"/>',
        "buttons": [
            {"type": "download_windows"}
        ],
        "link": "https://github.com/Shashankinfernape/Handesk/releases/latest"
    },
    {
        "id": "chatflix",
        "title": "CHATFLIX",
        "desc_lines": [
            "Real-time messaging platform featuring a cinematic interface.",
            "Engineered for scalable communication and instant data sync."
        ],
        "tags": "JWT Auth • Socket.IO • MERN",
        "color": "#E50914",
        "icon_type": "svg",
        "icon_svg": '<path fill="currentColor" d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-6 9.5l-6 3.5v-7l6 3.5z"/>',
        "buttons": [
            {"type": "link"},
            {"type": "github"}
        ],
        "link": "https://github.com/Shashankinfernape/Chatflix"
    },
    {
        "id": "slidepapers",
        "title": "SLIDEPAPERS",
        "desc_lines": [
            "Dynamic documentation and presentation engine for developers.",
            "Streamlines interactive content delivery and visualizations."
        ],
        "tags": "React • Vite • Document Engine",
        "color": "#9D4EDD",
        "icon_type": "image",
        "logo_path": "logos/slidepapers.png",
        "buttons": [
            {"type": "link"},
            {"type": "github"}
        ],
        "link": "https://github.com/Shashankinfernape/Slidepaper"
    },
    {
        "id": "examinar",
        "title": "EXAMINAR",
        "desc_lines": [
            "Cross-platform assessment environment and secure testing.",
            "Provides strict parameters alongside real-time metrics."
        ],
        "tags": "Dart • Cross-platform • Secure Testing",
        "color": "#00C4B3",
        "icon_type": "image",
        "logo_path": "logos/examinar.png",
        "buttons": [
            {"type": "download_generic"}
        ],
        "link": "https://github.com/Shashankinfernape/Examinar/releases/latest"
    },
    {
        "id": "territory",
        "title": "TERRITORY",
        "desc_lines": [
            "TypeScript-based architectural framework for complex state.",
            "Optimizes real-time location tracking for user clusters."
        ],
        "tags": "TypeScript • Real-time Sync • State Management",
        "color": "#F5A623",
        "icon_type": "svg",
        "icon_svg": '<path fill="currentColor" d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 10c1.66 0 2.99-1.34 2.99-3s-1.33-3-2.99-3c-1.66 0-3 1.34-3 3s1.34 3 3 3zm8-10c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/>',
        "buttons": [
            {"type": "link"},
            {"type": "github"}
        ],
        "link": "https://github.com/Shashankinfernape/Territory"
    },
    {
        "id": "sstraess",
        "title": "SSTRAESS",
        "desc_lines": [
            "High-intensity load testing and system stress simulation.",
            "Features modernized UI tracking for active threshold limits."
        ],
        "tags": "Load Testing • Simulation • Monitoring",
        "color": "#FFC107",
        "icon_type": "svg",
        "icon_svg": '<path fill="currentColor" d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z"/>',
        "buttons": [
            {"type": "download_generic"}
        ],
        "link": "https://github.com/Shashankinfernape/SSTRAESS/releases/latest"
    }
]

W = 800
H = 124  # Compact tab height
GAP = 12 # Gap below the tab for spacing in Markdown without relying on <br>
TOTAL_H = H + GAP

def render_buttons(buttons):
    svg = ""
    # Start positioning from right to left
    current_x = W - 20
    
    # SVG Paths
    icon_link = "M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"
    icon_github = "M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5c.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34c-.45-1.15-1.11-1.46-1.11-1.46c-.91-.62.07-.6.07-.6c1 .07 1.53 1.03 1.53 1.03c.87 1.52 2.34 1.07 2.91.83c.09-.65.35-1.09.63-1.34c-2.22-.25-4.55-1.11-4.55-4.92c0-1.11.38-2 1.03-2.71c-.1-.25-.45-1.29.1-2.64c0 0 .84-.27 2.75 1.02c.79-.22 1.65-.33 2.5-.33c.85 0 1.71.11 2.5.33c1.91-1.29 2.75-1.02 2.75-1.02c.55 1.35.2 2.39.1 2.64c.65.71 1.03 1.6 1.03 2.71c0 3.82-2.34 4.66-4.57 4.91c.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2z"
    icon_download = "M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"
    icon_windows = "M0 3.449L9.75 2.1v7.641H0V3.45zM10.668 1.965L22.5 0v9.74H10.668V1.965zM0 10.5h9.75v7.641L0 16.792V10.5zM10.668 10.5H22.5v9.74l-11.832-1.666V10.5z"
    
    # Process buttons in reverse so they stack right-to-left
    for btn in reversed(buttons):
        t = btn["type"]
        if t == "download_windows":
            width = 84
            current_x -= width
            svg += f'''
            <rect x="{current_x}" y="{(H-36)//2}" width="{width}" height="36" rx="10" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.08)"/>
            <g transform="translate({current_x + 16}, {(H-24)//2})">
                <path fill="#ffffff" opacity="0.9" d="{icon_download}" transform="scale(0.8) translate(0, 3)"/>
                <path fill="#ffffff" opacity="0.9" d="{icon_windows}" transform="scale(0.9) translate(30, 2)"/>
            </g>
            '''
        elif t == "download_generic":
            width = 44
            current_x -= width
            svg += f'''
            <rect x="{current_x}" y="{(H-36)//2}" width="{width}" height="36" rx="10" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.08)"/>
            <g transform="translate({current_x + 10}, {(H-24)//2})">
                <path fill="#ffffff" opacity="0.9" d="{icon_download}"/>
            </g>
            '''
        elif t == "link":
            width = 44
            current_x -= width
            svg += f'''
            <rect x="{current_x}" y="{(H-36)//2}" width="{width}" height="36" rx="10" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.08)"/>
            <g transform="translate({current_x + 10}, {(H-24)//2})">
                <path fill="#ffffff" opacity="0.8" d="{icon_link}"/>
            </g>
            '''
        elif t == "github":
            width = 44
            current_x -= width
            svg += f'''
            <rect x="{current_x}" y="{(H-36)//2}" width="{width}" height="36" rx="10" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.06)"/>
            <g transform="translate({current_x + 10}, {(H-24)//2})">
                <path fill="#ffffff" opacity="0.7" d="{icon_github}"/>
            </g>
            '''
        current_x -= 8 # Gap between buttons
    
    return svg

def make_svg(p):
    # Base Premium Colors
    bg_fill = "#0C0C0E"
    border_color = "rgba(255,255,255,0.08)"
    highlight_color = "rgba(255,255,255,0.04)"
    
    # Icon Render
    icon_content = ""
    if p["icon_type"] == "svg":
        icon_content = f'<g transform="translate(36, 36) scale(1.1)"><g fill="{p["color"]}">{p["icon_svg"]}</g></g>'
    else:
        if p.get("logo_path") and os.path.exists(p["logo_path"]):
            ext = p["logo_path"].split('.')[-1].lower()
            mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
            with open(p["logo_path"], "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            icon_content = f'<image href="data:{mime};base64,{b64}" x="32" y="32" width="32" height="32" preserveAspectRatio="xMidYMid meet"/>'
    
    btn_svg = render_buttons(p["buttons"])

    svg = f'''<svg width="{W}" height="{TOTAL_H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <!-- Subtle radial glow for the icon container -->
    <radialGradient id="glow-{p['id']}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{p['color']}" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="{p['color']}" stop-opacity="0"/>
    </radialGradient>
    
    <clipPath id="card-clip">
      <rect x="0" y="0" width="{W}" height="{H}" rx="18"/>
    </clipPath>
  </defs>

  <!-- Base Card Container -->
  <rect x="0" y="0" width="{W}" height="{H}" rx="18" fill="{bg_fill}" stroke="{border_color}" stroke-width="1.5"/>

  <!-- Subtle Top Edge Highlight -->
  <path d="M18 1 L782 1 C791 1 799 9 799 18 L799 24 L1 24 L1 18 C1 9 9 1 18 1 Z" fill="{highlight_color}" clip-path="url(#card-clip)"/>

  <!-- Icon Container Glow -->
  <circle cx="48" cy="{H//2}" r="50" fill="url(#glow-{p['id']})"/>

  <!-- Icon Squircle -->
  <rect x="24" y="{(H-48)//2}" width="48" height="48" rx="14" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.08)"/>
  
  <!-- Icon Asset -->
  {icon_content}

  <!-- Typography -->
  <!-- Title -->
  <text x="96" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="20" font-weight="700" fill="#ffffff" letter-spacing="0.5">{p['title']}</text>

  <!-- Description -->
  <text x="96" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="14" font-weight="400" fill="#999999">{p['desc_lines'][0]}</text>
  <text x="96" y="88" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="14" font-weight="400" fill="#999999">{p['desc_lines'][1]}</text>

  <!-- Tags -->
  <text x="96" y="112" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="12" font-weight="600" fill="rgba(255,255,255,0.3)" letter-spacing="0.5">{p['tags'].upper()}</text>

  <!-- Action Buttons -->
  {btn_svg}
  
</svg>'''
    return svg

# Generate
for p in projects:
    svg_code = make_svg(p)
    with open(f"logos/{p['id']}_banner.svg", "w", encoding="utf-8") as f:
        f.write(svg_code)

print("Done — premium OS-style launcher tabs generated.")
