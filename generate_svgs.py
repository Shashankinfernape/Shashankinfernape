import json
import base64
import os

projects = [
    {
        "id": "handesk",
        "title": "HANDESK",
        "purpose": "DirectLink remote desktop",
        "meta": "Rust &#183; H.264 &#183; DXGI",
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
        "purpose": "Real-time messaging",
        "meta": "React &#183; Node.js &#183; Socket.IO",
        "icon_type": "svg",
        "icon_svg": '<path fill="currentColor" d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-6 9.5l-6 3.5v-7l6 3.5z"/>',
        "color": "#E50914",
        "buttons": [
            {"type": "download_android"},
            {"type": "link"}
        ]
    },
    {
        "id": "slidepapers",
        "title": "SLIDEPAPERS",
        "purpose": "Community wallpaper hub",
        "meta": "React &#183; Node.js &#183; MongoDB",
        "icon_type": "image",
        "logo_path": "logos/slidepapers.png",
        "color": "#9D4EDD",
        "buttons": [
            {"type": "link"}
        ]
    },
    {
        "id": "examinar",
        "title": "EXAMINAR",
        "purpose": "Student\'s app",
        "meta": "Flutter &#183; Dart &#183; Isar",
        "icon_type": "image",
        "logo_path": "logos/examinar.png",
        "color": "#00C4B3",
        "buttons": [
            {"type": "download_android"},
            {"type": "download_windows"}
        ]
    },
    {
        "id": "territory",
        "title": "TERRITORY",
        "purpose": "Real estate platform",
        "meta": "React &#183; FastAPI &#183; MongoDB",
        "icon_type": "image",
        "logo_path": "logos/territory_new.jpg",
        "color": "#F5A623",
        "buttons": [
            {"type": "link"}
        ]
    },
    {
        "id": "sstraess",
        "title": "SSTRAESS",
        "purpose": "JWT authentication system",
        "meta": "Node.js &#183; Monitoring",
        "icon_type": "svg",
        "icon_svg": '<path fill="currentColor" d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z"/>',
        "color": "#FFC107",
        "buttons": [
            {"type": "link"}
        ]
    }
]

H = 126
GAP = 12
TOTAL_H = H + GAP
BW = 46  # Button Width

icon_link = "M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"
icon_windows = "M0 3.449L9.75 2.1v7.641H0V3.45zM10.668 1.965L22.5 0v9.74H10.668V1.965zM0 10.5h9.75v7.641L0 16.792V10.5zM10.668 10.5H22.5v9.74l-11.832-1.666V10.5z"
icon_android = "M17.6 9.48l1.84-3.18c.16-.31.04-.69-.26-.85-.29-.15-.65-.06-.81.24L16.5 8.96C15.11 8.35 13.6 8 12 8s-3.11.35-4.5.96L5.66 5.69C5.5 5.39 5.14 5.3 4.85 5.45c-.3.16-.42.54-.26.85l1.84 3.18C3.82 11.28 2.21 13.9 2 17h20c-.21-3.1-1.82-5.72-4.4-7.52zM7 14.25c-.69 0-1.25-.56-1.25-1.25s.56-1.25 1.25-1.25 1.25.56 1.25 1.25-.56 1.25-1.25 1.25zm10 0c-.69 0-1.25-.56-1.25-1.25s.56-1.25 1.25-1.25 1.25.56 1.25 1.25-.56 1.25-1.25 1.25z"

def make_card_svg(p):
    # Dynamically calculate W so all cards + buttons align to exactly 412px
    W = 412 - (len(p["buttons"]) * BW)
    
    bg_fill = "#000000"
    border_color = "rgba(255,255,255,0.08)"
    
    icon_content = ""
    if p["icon_type"] == "svg":
        icon_content = f"""
        <rect x="18" y="27" width="72" height="72" rx="18" fill="{p['color']}" fill-opacity="0.15" stroke="{p['color']}" stroke-opacity="0.3" stroke-width="1"/>
        <g transform="translate(38, 47) scale(1.4)"><g fill="{p['color']}">{p['icon_svg']}</g></g>
        """
    else:
        if p.get("logo_path") and os.path.exists(p["logo_path"]):
            ext = p["logo_path"].split('.')[-1].lower()
            mime = "image/jpeg" if ext in ["jpg", "jpeg"] else "image/png"
            with open(p["logo_path"], "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            icon_content = f"""
            <clipPath id="icon-clip-{p['id']}">
                <rect x="18" y="27" width="72" height="72" rx="18"/>
            </clipPath>
            <rect x="18" y="27" width="72" height="72" rx="18" fill="#ffffff"/>
            <image href="data:{mime};base64,{b64}" x="18" y="27" width="72" height="72" preserveAspectRatio="xMidYMid slice" clip-path="url(#icon-clip-{p['id']})"/>
            <rect x="18" y="27" width="72" height="72" rx="18" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>
            """
    
    svg = f"""<svg width="{W}" height="{TOTAL_H}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{bg_fill}" stroke="{border_color}" stroke-width="1"/>
  <rect x="1" y="1" width="{W-2}" height="1" fill="rgba(255,255,255,0.04)"/>
  
  {icon_content}

  <text x="104" y="48" font-family="'Google Sans', Roboto, 'Segoe UI', system-ui, sans-serif" font-size="18" font-weight="700" fill="#ffffff" letter-spacing="0.2">{p['title']}</text>
  <text x="104" y="70" font-family="Roboto, 'Segoe UI', system-ui, sans-serif" font-size="14" font-weight="400" fill="#f0f0f0">{p['purpose']}</text>
  <text x="104" y="88" font-family="Roboto, 'Segoe UI', system-ui, sans-serif" font-size="12" font-weight="500" fill="#a0a0a0">{p['meta']}</text>
</svg>"""
    return svg

def generate_button_svg(btn_type):
    BH = TOTAL_H
    
    if btn_type == "download_windows":
        icon_path = f'<path fill="#ffffff" d="{icon_windows}" transform="translate(12, 10.5) scale(0.95)"/>'
    elif btn_type == "download_android":
        icon_path = f'<path fill="#3ddc84" d="{icon_android}" transform="translate(11, 6) scale(1)"/>'
    elif btn_type == "link":
        icon_path = f'<path fill="#ffffff" d="{icon_link}" transform="translate(11, 6) scale(1)"/>'
    else:
        return ""

    svg = f"""<svg width="{BW}" height="{BH}" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(6, {(H-36)//2})">
    <rect width="36" height="36" rx="12" fill="rgba(255,255,255,0.06)" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
    <rect x="1" y="1" width="34" height="1" rx="6" fill="rgba(255,255,255,0.08)"/>
    {icon_path}
  </g>
</svg>"""
    return svg

for p in projects:
    with open(f"logos/{p['id']}_app.svg", "w", encoding="utf-8") as f:
        f.write(make_card_svg(p))

with open(f"logos/btn_android.svg", "w", encoding="utf-8") as f:
    f.write(generate_button_svg("download_android"))
    
with open(f"logos/btn_windows.svg", "w", encoding="utf-8") as f:
    f.write(generate_button_svg("download_windows"))
    
with open(f"logos/btn_link.svg", "w", encoding="utf-8") as f:
    f.write(generate_button_svg("link"))
