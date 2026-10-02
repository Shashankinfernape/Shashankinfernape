import os
import base64
import textwrap

projects = [
    {
        "id": "handesk",
        "title": "HANdesk",
        "purpose": "DirectLink remote desktop",
        "meta": "Windows &amp; Android &#183; Rust &#183; H.264",
        "icon_type": "image",
        "logo_path": "logos/handesk.jpg",
        "color": "#00A4EF",
        "buttons": [
            {"type": "download_android"},
            {"type": "download_windows"}
        ]
    },
    {
        "id": "chatflix",
        "title": "CHATFLIX",
        "purpose": "Real-time messaging platform",
        "meta": "Web app &#183; React &#183; Node.js",
        "icon_type": "svg",
        "icon_svg": '<path fill="currentColor" d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-6 9.5l-6 3.5v-7l6 3.5z"/>',
        "color": "#E50914",
        "buttons": [
            {"type": "github"},
            {"type": "link"}
        ]
    },
    {
        "id": "slidepapers",
        "title": "SLIDEPAPERS",
        "purpose": "Developer presentation engine",
        "meta": "Web app &#183; React &#183; Vite",
        "icon_type": "image",
        "logo_path": "logos/slidepapers.png",
        "color": "#9D4EDD",
        "buttons": [
            {"type": "github"},
            {"type": "link"}
        ]
    },
    {
        "id": "examinar",
        "title": "EXAMINAR",
        "purpose": "Secure testing environment",
        "meta": "42 MB &#183; Android",
        "icon_type": "image",
        "logo_path": "logos/examinar.png",
        "color": "#00C4B3",
        "buttons": [
            {"type": "download"}
        ]
    },
    {
        "id": "territory",
        "title": "TERRITORY",
        "purpose": "Real-time location tracking &amp; state sync",
        "meta": "Library &#183; TypeScript &#183; React",
        "icon_type": "image",
        "logo_path": "logos/territory_new.jpg",
        "color": "#F5A623",
        "buttons": [
            {"type": "github"}
        ]
    },
    {
        "id": "sstraess",
        "title": "SSTRAESS",
        "purpose": "High-intensity load testing simulation",
        "meta": "Web app &#183; Node.js &#183; Monitoring",
        "icon_type": "svg",
        "icon_svg": '<path fill="currentColor" d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z"/>',
        "color": "#FFC107",
        "buttons": [
            {"type": "link"}
        ]
    }
]

W = 400
H = 100
GAP = 12
TOTAL_H = H + GAP

def render_buttons(buttons):
    svg = ""
    current_x = W - 12
    
    icon_link = "M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"
    icon_github = "M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5c.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34c-.45-1.15-1.11-1.46-1.11-1.46c-.91-.62.07-.6.07-.6c1 .07 1.53 1.03 1.53 1.03c.87 1.52 2.34 1.07 2.91.83c.09-.65.35-1.09.63-1.34c-2.22-.25-4.55-1.11-4.55-4.92c0-1.11.38-2 1.03-2.71c-.1-.25-.45-1.29.1-2.64c0 0 .84-.27 2.75 1.02c.79-.22 1.65-.33 2.5-.33c.85 0 1.71.11 2.5.33c1.91-1.29 2.75-1.02 2.75-1.02c.55 1.35.2 2.39.1 2.64c.65.71 1.03 1.6 1.03 2.71c0 3.82-2.34 4.66-4.57 4.91c.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2z"
    icon_download = "M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"
    icon_windows = "M0 3.449L9.75 2.1v7.641H0V3.45zM10.668 1.965L22.5 0v9.74H10.668V1.965zM0 10.5h9.75v7.641L0 16.792V10.5zM10.668 10.5H22.5v9.74l-11.832-1.666V10.5z"
    icon_android = "M17.6 9.48l1.84-3.18c.16-.31.04-.69-.26-.85-.29-.15-.65-.06-.81.24L16.5 8.96C15.11 8.35 13.6 8 12 8s-3.11.35-4.5.96L5.66 5.69C5.5 5.39 5.14 5.3 4.85 5.45c-.3.16-.42.54-.26.85l1.84 3.18C3.82 11.28 2.21 13.9 2 17h20c-.21-3.1-1.82-5.72-4.4-7.52zM7 14.25c-.69 0-1.25-.56-1.25-1.25s.56-1.25 1.25-1.25 1.25.56 1.25 1.25-.56 1.25-1.25 1.25zm10 0c-.69 0-1.25-.56-1.25-1.25s.56-1.25 1.25-1.25 1.25.56 1.25 1.25-.56 1.25-1.25 1.25z"
    
    for btn in reversed(buttons):
        t = btn["type"]
        if t == "download_windows":
            width = 32
            current_x -= width
            svg += f'<g transform="translate({current_x}, {(H-32)//2})"><rect width="{width}" height="32" rx="10" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.12)"/><path fill="#ffffff" d="{icon_windows}" transform="translate(6, 8.5) scale(0.85)"/></g>'
        elif t == "download_android":
            width = 32
            current_x -= width
            svg += f'<g transform="translate({current_x}, {(H-32)//2})"><rect width="{width}" height="32" rx="10" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.12)"/><path fill="#3ddc84" d="{icon_android}" transform="translate(4, 4) scale(1)"/></g>'
        elif t == "download":
            width = 32
            current_x -= width
            svg += f'<g transform="translate({current_x}, {(H-32)//2})"><rect width="{width}" height="32" rx="10" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.12)"/><path fill="#ffffff" d="{icon_download}" transform="translate(4, 4) scale(1)"/></g>'
        elif t == "link":
            width = 32
            current_x -= width
            svg += f'<g transform="translate({current_x}, {(H-32)//2})"><rect width="{width}" height="32" rx="10" fill="rgba(255,255,255,0.08)" stroke="rgba(255,255,255,0.12)"/><path fill="#ffffff" d="{icon_link}" transform="translate(4, 4) scale(1)"/></g>'
        elif t == "github":
            width = 32
            current_x -= width
            svg += f'<g transform="translate({current_x}, {(H-32)//2})"><rect width="{width}" height="32" rx="10" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.08)"/><path fill="#ffffff" opacity="0.8" d="{icon_github}" transform="translate(4, 4) scale(1)"/></g>'
        current_x -= 6
    
    return svg

def make_svg(p):
    bg_fill = "#0E0E11"
    border_color = "rgba(255,255,255,0.05)"
    
    icon_content = ""
    if p["icon_type"] == "svg":
        icon_content = f'''
        <rect x="12" y="22" width="56" height="56" rx="14" fill="{p['color']}" fill-opacity="0.15" stroke="{p['color']}" stroke-opacity="0.3" stroke-width="1"/>
        <g transform="translate(28, 38) scale(1.1)"><g fill="{p['color']}">{p['icon_svg']}</g></g>
        '''
    else:
        if p.get("logo_path") and os.path.exists(p["logo_path"]):
            ext = p["logo_path"].split('.')[-1].lower()
            mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
            with open(p["logo_path"], "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            icon_content = f'''
            <clipPath id="icon-clip-{p['id']}">
                <rect x="12" y="22" width="56" height="56" rx="14"/>
            </clipPath>
            <rect x="12" y="22" width="56" height="56" rx="14" fill="#ffffff"/>
            <image href="data:{mime};base64,{b64}" x="12" y="22" width="56" height="56" preserveAspectRatio="xMidYMid slice" clip-path="url(#icon-clip-{p['id']})"/>
            <rect x="12" y="22" width="56" height="56" rx="14" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>
            '''
    
    btn_svg = render_buttons(p["buttons"])

    svg = f'''<svg width="{W}" height="{TOTAL_H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <rect x="0" y="0" width="{W}" height="{H}" rx="12" fill="{bg_fill}" stroke="{border_color}" stroke-width="1"/>
  <rect x="1" y="1" width="{W-2}" height="1" fill="rgba(255,255,255,0.04)"/>
  
  {icon_content}

  <text x="80" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="16" font-weight="600" fill="#ffffff" letter-spacing="0.2">{p['title']}</text>
  <text x="80" y="62" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" font-weight="400" fill="#a0a0a0">{p['purpose']}</text>
  <text x="80" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="11" font-weight="500" fill="#666666">{p['meta']}</text>

  {btn_svg}
</svg>'''
    return svg

for p in projects:
    with open(f"logos/{p['id']}_banner.svg", "w", encoding="utf-8") as f:
        f.write(make_svg(p))

print("Done — 2-column Play Store SVGs generated.")

print("Done — Play Store style app listing rows generated.")
