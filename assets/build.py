"""Generates the profile README artwork in light and dark variants.

Run:  python3 assets/build.py
Every SVG is self-contained (system fonts, inline CSS animation) so GitHub can
render it as an <img>. Edit the THEMES tokens or the copy below, then rebuild.
"""
from pathlib import Path

OUT = Path(__file__).parent
W = 1200

THEMES = {
    "dark": dict(bg="#0B0D10", surface="#12151A", sunken="#0E1014", line="#232831",
                 text="#ECEDEF", muted="#8A929E", accent="#FF7A00", accent2="#4C7BF4",
                 accentSoft="#FF7A0022", shadow="#00000088"),
    "light": dict(bg="#F7F6F2", surface="#FFFFFF", sunken="#F1EFEA", line="#E3E0D8",
                  text="#121417", muted="#6B7078", accent="#E8620C", accent2="#2F5BD3",
                  accentSoft="#E8620C1A", shadow="#1214171F"),
}

SANS = "Inter, 'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'SF Mono', ui-monospace, Menlo, Consolas, monospace"

BASE_CSS = f"""
  .sans {{ font-family: {SANS}; }}
  .mono {{ font-family: {MONO}; letter-spacing: .06em; }}
  .in {{ opacity: 0; animation: in .9s cubic-bezier(.2,.7,.2,1) forwards; }}
  @keyframes in {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: none; }} }}
  @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
  @keyframes pulse {{ 0% {{ r: 6; opacity: .9; }} 100% {{ r: 18; opacity: 0; }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; opacity: 1 !important; }} }}
"""


def svg(h, body, css="", title=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" '
            f'role="img" aria-label="{title}"><title>{title}</title><style>{BASE_CSS}{css}</style>{body}</svg>\n')


def d(i):
    return f'style="animation-delay:{i:.2f}s"'


# ---------------------------------------------------------------- hero
def hero(t):
    h = 520
    index = ["Senior Frontend Developer", "UI/UX Designer", "Urchin Systems", "Building MovesFlow"]
    rows = "".join(
        f'<g class="in" {d(.5 + i * .12)}>'
        f'<text x="780" y="{232 + i * 46}" class="mono" font-size="15" fill="{t["accent"]}">0{i + 1}</text>'
        f'<text x="824" y="{232 + i * 46}" class="sans" font-size="23" fill="{t["text"]}">{s}</text></g>'
        for i, s in enumerate(index))
    css = f"""
      .orb {{ animation: drift 14s ease-in-out infinite alternate; transform-origin: center; }}
      @keyframes drift {{ from {{ transform: translate(0,0) scale(1); }} to {{ transform: translate(-120px,60px) scale(1.15); }} }}
      .caret {{ animation: blink 1.1s steps(1) infinite; }}
      .ring {{ animation: pulse 1.8s ease-out infinite; }}
    """
    body = f"""
  <defs>
    <pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M48 0H0V48" fill="none" stroke="{t['line']}" stroke-width="1"/>
    </pattern>
    <radialGradient id="fade" cx="35%" cy="40%" r="75%">
      <stop offset="0" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </radialGradient>
    <mask id="m"><rect width="{W}" height="{h}" fill="url(#fade)"/></mask>
    <radialGradient id="glow"><stop offset="0" stop-color="{t['accent']}" stop-opacity=".38"/>
      <stop offset="1" stop-color="{t['accent']}" stop-opacity="0"/></radialGradient>
    <radialGradient id="glow2"><stop offset="0" stop-color="{t['accent2']}" stop-opacity=".30"/>
      <stop offset="1" stop-color="{t['accent2']}" stop-opacity="0"/></radialGradient>
    <clipPath id="c"><rect width="{W}" height="{h}" rx="24"/></clipPath>
  </defs>
  <g clip-path="url(#c)">
    <rect width="{W}" height="{h}" fill="{t['bg']}"/>
    <rect width="{W}" height="{h}" fill="url(#grid)" mask="url(#m)" opacity=".7"/>
    <circle class="orb" cx="1000" cy="110" r="300" fill="url(#glow)"/>
    <circle class="orb" cx="1120" cy="470" r="240" fill="url(#glow2)" style="animation-duration:18s"/>
  </g>
  <rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="24" fill="none" stroke="{t['line']}"/>

  <text x="56" y="66" class="mono in" font-size="15" fill="{t['muted']}">SSDENISS / README.MD</text>
  <g class="in" {d(.1)}>
    <circle class="ring" cx="846" cy="61" r="6" fill="none" stroke="{t['accent']}" stroke-width="2"/>
    <circle cx="846" cy="61" r="5" fill="{t['accent']}"/>
    <text x="1144" y="66" class="mono" font-size="15" fill="{t['text']}" text-anchor="end">NOW BUILDING <tspan fill="{t['accent']}">MOVESFLOW.IT</tspan></text>
  </g>
  <line x1="56" y1="92" x2="1144" y2="92" stroke="{t['line']}"/>

  <g class="sans" font-weight="700" fill="{t['text']}" letter-spacing="-5">
    <text x="50" y="270" font-size="138" class="in" {d(.15)}>Denis</text>
    <text x="50" y="402" font-size="138" class="in" {d(.3)}>Șeremet<tspan fill="{t['accent']}">.</tspan></text>
  </g>
  {rows}

  <line x1="56" y1="446" x2="1144" y2="446" stroke="{t['line']}"/>
  <text x="56" y="484" class="mono in" {d(.9)} font-size="15" fill="{t['muted']}">INTERFACES · DESIGN SYSTEMS · REACT · TYPESCRIPT · SPRING BOOT</text>
  <text x="1012" y="484" class="mono in" {d(1)} font-size="15" fill="{t['text']}">movesflow.it</text>
  <rect class="caret" x="1128" y="470" width="10" height="18" fill="{t['accent']}"/>
"""
    return svg(h, body, css, "Denis Șeremet — Senior Frontend Developer and UI/UX Designer")


# ---------------------------------------------------------------- section labels
def label(t, num, title):
    body = f"""
  <text x="0" y="56" class="mono" font-size="16" fill="{t['accent']}">{num}</text>
  <text x="52" y="60" class="sans" font-size="36" font-weight="650" letter-spacing="-1" fill="{t['text']}">{title}</text>
  <line x1="380" y1="48" x2="{W}" y2="48" stroke="{t['line']}"/>
  <rect x="{W - 8}" y="44" width="8" height="8" fill="{t['accent']}"/>
"""
    return svg(84, body, "", f"{num} {title}")


# ---------------------------------------------------------------- MovesFlow board
def board(t):
    h = 640
    nav = ["Orders", "Calendar", "Fleet", "Chat", "Surveys", "Billing"]
    navsvg = ""
    for i, n in enumerate(nav):
        y = 150 + i * 46
        active = i == 0
        if active:
            navsvg += f'<rect x="16" y="{y - 22}" width="188" height="38" rx="10" fill="{t["accentSoft"]}"/>'
        c = t["accent"] if active else t["muted"]
        navsvg += (f'<rect x="32" y="{y - 11}" width="16" height="16" rx="4" fill="none" stroke="{c}" stroke-width="2"/>'
                   f'<text x="62" y="{y + 3}" class="sans" font-size="17" fill="{t["text"] if active else t["muted"]}" '
                   f'font-weight="{600 if active else 400}">{n}</text>')

    cols = [("REQUEST", t["accent2"]), ("SCHEDULED", t["muted"]), ("IN TRANSIT", t["accent"]), ("DONE", "#22A06B")]
    cards = {
        0: [("Milano → Torino", "Survey pending", "Survey"), ("Bergamo → Como", "Quote requested", "Quote")],
        1: [("Roma → Napoli", "3 movers · 1 van", "Fri 08:00"), ("Verona → Padova", "2 movers · 1 van", "Fri 13:30")],
        2: [("Firenze → Bologna", "4 movers · 2 vans", "Live")],
        3: [("Genova → Pisa", "Invoice sent", "Paid"), ("Parma → Modena", "Invoice sent", "Paid")],
    }
    colsvg = ""
    for ci, (name, c) in enumerate(cols):
        x = 248 + ci * 236
        colsvg += (f'<circle cx="{x + 6}" cy="155" r="5" fill="{c}"/>'
                   f'<text x="{x + 20}" y="160" class="mono" font-size="13" fill="{t["muted"]}">{name}</text>'
                   f'<text x="{x + 220}" y="160" class="mono" font-size="13" fill="{t["muted"]}" text-anchor="end">{len(cards[ci]) + (1 if ci == 1 else 0)}</text>'
                   f'<rect x="{x}" y="176" width="220" height="420" rx="14" fill="{t["sunken"]}" stroke="{t["line"]}"/>')
        for k, (title, sub, chip) in enumerate(cards[ci]):
            colsvg += card(t, x + 12, 190 + k * 108, title, sub, chip, c, faded=(ci == 3))
    moving = card(t, 248 + 236 + 12, 190 + 2 * 108, "Torino → Asti", "2 movers · 1 van", "Loading", t["accent"], hl=True)
    css = """
      .mv { animation: move 7s cubic-bezier(.65,0,.35,1) infinite; }
      @keyframes move { 0%, 30% { transform: translate(0,0); } 45%, 80% { transform: translate(236px,-108px); }
                        90% { transform: translate(236px,-108px); opacity: 0; } 91% { transform: translate(0,0); opacity: 0; }
                        100% { transform: translate(0,0); opacity: 1; } }
      .toast { animation: toast 7s ease infinite; }
      @keyframes toast { 0%, 46% { opacity: 0; transform: translateY(16px); } 52%, 82% { opacity: 1; transform: none; }
                         90%, 100% { opacity: 0; transform: translateY(16px); } }
    """
    body = f"""
  <defs>
    <filter id="sh" x="-20%" y="-20%" width="140%" height="160%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="{t['shadow']}"/></filter>
    <clipPath id="c"><rect width="{W}" height="{h}" rx="20"/></clipPath>
  </defs>
  <g clip-path="url(#c)">
  <rect width="{W}" height="{h}" fill="{t['surface']}"/>
  <rect width="{W}" height="52" fill="{t['sunken']}"/>
  <circle cx="28" cy="26" r="6" fill="{t['line']}"/><circle cx="48" cy="26" r="6" fill="{t['line']}"/><circle cx="68" cy="26" r="6" fill="{t['line']}"/>
  <text x="{W / 2}" y="31" class="mono" font-size="14" fill="{t['muted']}" text-anchor="middle">MOVESFLOW — DISPATCH BOARD</text>
  <line x1="0" y1="52" x2="{W}" y2="52" stroke="{t['line']}"/>

  <path d="M30 76 l14 8 v18 l-14 -8z" fill="{t['accent']}"/><path d="M48 84 l14 -8 v18 l-14 8z" fill="{t['accent']}" opacity=".8"/>
  <path d="M40 70 l12 -7 l10 6 l-12 7z" fill="{t['accent2']}"/>
  <text x="74" y="96" class="sans" font-size="20" font-weight="700" fill="{t['text']}">Moves<tspan fill="{t['accent2']}">Flow</tspan></text>
  {navsvg}
  <line x1="220" y1="52" x2="220" y2="{h}" stroke="{t['line']}"/>

  <text x="248" y="104" class="sans" font-size="28" font-weight="700" letter-spacing="-.5" fill="{t['text']}">Today</text>
  <text x="340" y="104" class="sans" font-size="16" fill="{t['muted']}">Dispatch overview</text>
  <rect x="1032" y="78" width="144" height="38" rx="10" fill="{t['accent']}"/>
  <text x="1104" y="103" class="sans" font-size="16" font-weight="600" fill="#fff" text-anchor="middle">+ New order</text>
  {colsvg}
  <g class="mv">{moving}</g>

  <g class="toast" filter="url(#sh)">
    <rect x="884" y="532" width="292" height="72" rx="14" fill="{t['surface']}" stroke="{t['line']}"/>
    <circle cx="912" cy="568" r="14" fill="{t['accentSoft']}"/><path d="M905 568 l5 5 l9 -10" stroke="{t['accent']}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <text x="938" y="562" class="sans" font-size="15" font-weight="600" fill="{t['text']}">Crew update</text>
    <text x="938" y="584" class="sans" font-size="14" fill="{t['muted']}">Truck loaded, on the way</text>
  </g>
  </g>
  <rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="20" fill="none" stroke="{t['line']}"/>
"""
    return svg(h, body, css, "Illustration of the MovesFlow dispatch board")


def card(t, x, y, title, sub, chip, c, faded=False, hl=False):
    op = ' opacity=".55"' if faded else ""
    stroke = t["accent"] if hl else t["line"]
    sw = 2 if hl else 1
    f = ' filter="url(#sh)"' if hl else ""
    cw = len(chip) * 8 + 20
    return (f'<g{op}><rect x="{x}" y="{y}" width="196" height="96" rx="12" fill="{t["surface"]}" stroke="{stroke}" stroke-width="{sw}"{f}/>'
            f'<text x="{x + 16}" y="{y + 30}" class="sans" font-size="16" font-weight="600" fill="{t["text"]}">{title}</text>'
            f'<text x="{x + 16}" y="{y + 52}" class="sans" font-size="13" fill="{t["muted"]}">{sub}</text>'
            f'<circle cx="{x + 26}" cy="{y + 76}" r="9" fill="{t["accent2"]}" opacity=".85"/>'
            f'<circle cx="{x + 40}" cy="{y + 76}" r="9" fill="{t["accent"]}" opacity=".85" stroke="{t["surface"]}" stroke-width="2"/>'
            f'<rect x="{x + 180 - cw}" y="{y + 66}" width="{cw}" height="20" rx="10" fill="none" stroke="{c}"/>'
            f'<text x="{x + 180 - cw / 2}" y="{y + 80}" class="mono" font-size="11" fill="{c}" text-anchor="middle">{chip.upper()}</text></g>')


# ---------------------------------------------------------------- stats strip
def stats(t):
    data = [("465", "COMMITS"), ("21", "API MODULES"), ("280+", "TSX FILES"), ("86", "DB MIGRATIONS")]
    body = f'<line x1="0" y1="1" x2="{W}" y2="1" stroke="{t["line"]}"/><line x1="0" y1="139" x2="{W}" y2="139" stroke="{t["line"]}"/>'
    for i, (n, l) in enumerate(data):
        x = i * 300
        if i:
            body += f'<line x1="{x}" y1="24" x2="{x}" y2="116" stroke="{t["line"]}"/>'
        body += (f'<g class="in" {d(i * .12)}><text x="{x + (0 if i == 0 else 32)}" y="82" class="sans" font-size="58" font-weight="700" letter-spacing="-2" fill="{t["text"]}">{n}</text>'
                 f'<text x="{x + (0 if i == 0 else 32)}" y="112" class="mono" font-size="13" fill="{t["muted"]}">{l}</text></g>')
    return svg(140, body, "", "MovesFlow web platform in numbers")


# ---------------------------------------------------------------- ecosystem
def ecosystem(t):
    items = [("MOBILE", "Field app for crews", ["Orders, chat, push notifications", "and proof-of-delivery photos"], "REACT NATIVE · EXPO"),
             ("WEBSITE", "movesflow.it", ["Italian marketing site with", "move-request forms"], "ASTRO · TYPESCRIPT"),
             ("LEGACY", "Odoo v1", ["The original platform, built", "as custom Odoo 19 modules"], "ODOO · PYTHON")]
    body = ""
    for i, (k, ttl, lines, stack) in enumerate(items):
        x = i * 408
        body += (f'<g class="in" {d(i * .12)}><rect x="{x + .5}" y=".5" width="383" height="219" rx="16" fill="{t["surface"]}" stroke="{t["line"]}"/>'
                 f'<text x="{x + 28}" y="44" class="mono" font-size="13" fill="{t["accent"]}">{k}</text>'
                 f'<text x="{x + 28}" y="84" class="sans" font-size="26" font-weight="650" letter-spacing="-.5" fill="{t["text"]}">{ttl}</text>'
                 + "".join(f'<text x="{x + 28}" y="{118 + j * 24}" class="sans" font-size="16" fill="{t["muted"]}">{s}</text>' for j, s in enumerate(lines))
                 + f'<line x1="{x + 28}" y1="170" x2="{x + 356}" y2="170" stroke="{t["line"]}"/>'
                 f'<text x="{x + 28}" y="198" class="mono" font-size="12" fill="{t["muted"]}">{stack}</text></g>')
    return svg(220, body, "", "MovesFlow ecosystem: mobile app, website and legacy Odoo platform")


# ---------------------------------------------------------------- toolkit spec sheet
TOOLKIT = [
    ("INTERFACE", "React · Next.js · Angular · Vue · TypeScript"),
    ("STATE & DATA", "Redux · TanStack Query · Zustand · Zod"),
    ("STYLING", "MUI · Ant Design · Tailwind · SCSS · styled-components"),
    ("MOBILE", "React Native · Expo"),
    ("BACKEND", "Spring Boot · Node.js · NestJS · Express · jOOQ"),
    ("DATABASES", "PostgreSQL · MySQL · MongoDB"),
    ("QUALITY", "Vitest · Jest · Playwright · Testcontainers"),
    ("DESIGN", "Figma · Photoshop · Illustrator · After Effects · Blender"),
    ("OPS", "Docker · Nginx · GitLab CI · Linux"),
]


def toolkit(t):
    rh = 58
    h = len(TOOLKIT) * rh + 2
    body = ""
    for i, (k, v) in enumerate(TOOLKIT):
        y = i * rh
        body += (f'<g class="in" {d(i * .06)}><line x1="0" y1="{y + 1}" x2="{W}" y2="{y + 1}" stroke="{t["line"]}"/>'
                 f'<text x="0" y="{y + 37}" class="mono" font-size="13" fill="{t["accent"]}">{i + 1:02d}</text>'
                 f'<text x="52" y="{y + 37}" class="mono" font-size="14" fill="{t["muted"]}">{k.replace("&", "&amp;")}</text>'
                 f'<text x="300" y="{y + 38}" class="sans" font-size="21" fill="{t["text"]}">{v}</text></g>')
    body += f'<line x1="0" y1="{h - 1}" x2="{W}" y2="{h - 1}" stroke="{t["line"]}"/>'
    return svg(h, body, "", "Toolkit")


# ---------------------------------------------------------------- footer
def footer(t):
    css = ".caret { animation: blink 1.1s steps(1) infinite; }"
    body = f"""
  <line x1="0" y1="1" x2="{W}" y2="1" stroke="{t['line']}"/>
  <text x="0" y="52" class="mono" font-size="14" fill="{t['muted']}">© 2026 DENIS ȘEREMET</text>
  <text x="{W - 24}" y="52" class="mono" font-size="14" fill="{t['muted']}" text-anchor="end">DESIGNED IN FIGMA · SHIPPED IN TYPESCRIPT</text>
  <rect class="caret" x="{W - 10}" y="38" width="10" height="18" fill="{t['accent']}"/>
"""
    return svg(72, body, css, "Footer")


SECTIONS = [("about", "01", "About"), ("work", "02", "Selected work"), ("toolkit", "03", "Toolkit"), ("contact", "04", "Elsewhere")]

if __name__ == "__main__":
    for name, t in THEMES.items():
        files = {"hero": hero(t), "movesflow-board": board(t), "movesflow-stats": stats(t),
                 "movesflow-ecosystem": ecosystem(t), "toolkit": toolkit(t), "footer": footer(t)}
        for key, num, title in SECTIONS:
            files[f"label-{key}"] = label(t, num, title)
        for f, content in files.items():
            (OUT / f"{f}-{name}.svg").write_text(content, encoding="utf-8")
    print("built", len(list(OUT.glob("*.svg"))), "svgs")
