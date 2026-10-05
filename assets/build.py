"""Generates the profile README artwork in light and dark variants.

Run:  python3 assets/build.py   (bump VERSION so GitHub's image cache picks up changes)
Every SVG is self-contained (system fonts, inline CSS animation) so GitHub can
render it as an <img>. Edit the THEMES tokens or the copy below, then rebuild.
"""
from pathlib import Path

OUT = Path(__file__).parent
W = 1200

THEMES = {
    # brand = deep green for fills and large shapes; accent = readable tint of it for small text
    "dark": dict(bg="#07110D", surface="#0C1813", sunken="#09130F", line="#1F3329",
                 text="#E9F1EC", muted="#86978E", brand="#0B6E4F", accent="#4CC38A", accent2="#2E9C74",
                 accentSoft="#0B6E4F55", onAccent="#FFFFFF", shadow="#00000088"),
    "light": dict(bg="#F3F7F4", surface="#FFFFFF", sunken="#ECF2EE", line="#D2DED7",
                  text="#0E1713", muted="#5C6A63", brand="#0B6E4F", accent="#0B6E4F", accent2="#3E9C78",
                  accentSoft="#0B6E4F1A", onAccent="#FFFFFF", shadow="#0E17131F"),
}

SANS = "Inter, 'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'SF Mono', ui-monospace, Menlo, Consolas, monospace"

BASE_CSS = f"""
  .sans {{ font-family: {SANS}; }}
  .mono {{ font-family: {MONO}; letter-spacing: .06em; }}
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
    info = [("ROLE", "Senior Frontend Developer"), ("COMPANY", "Urchin Systems"),
            ("EXPERIENCE", "6+ years, full stack"), ("BASED IN", "Chișinău, Moldova"),
            ("EDUCATION", "Technical University of Moldova")]
    rows = "".join(
        f'<g class="in" {d(.5 + i * .1)}>'
        f'<line x1="690" y1="{170 + i * 52}" x2="1144" y2="{170 + i * 52}" stroke="{t["line"]}"/>'
        f'<text x="690" y="{202 + i * 52}" class="mono" font-size="13" fill="{t["accent"]}">{k}</text>'
        f'<text x="820" y="{203 + i * 52}" class="sans" font-size="20" fill="{t["text"]}">{v}</text></g>'
        for i, (k, v) in enumerate(info))
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
    <radialGradient id="glow"><stop offset="0" stop-color="{t['brand']}" stop-opacity=".75"/>
      <stop offset="1" stop-color="{t['brand']}" stop-opacity="0"/></radialGradient>
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
    <circle class="ring" cx="834" cy="61" r="6" fill="none" stroke="{t['accent']}" stroke-width="2"/>
    <circle cx="834" cy="61" r="5" fill="{t['brand']}"/>
    <text x="1144" y="66" class="mono" font-size="15" fill="{t['text']}" text-anchor="end">FRONTEND <tspan fill="{t['accent']}">·</tspan> UI/UX <tspan fill="{t['accent']}">·</tspan> FULL STACK</text>
  </g>
  <line x1="56" y1="92" x2="1144" y2="92" stroke="{t['line']}"/>

  <g class="sans" font-weight="700" fill="{t['text']}" letter-spacing="-5">
    <text x="50" y="270" font-size="124" class="in" {d(.15)}>Denis</text>
    <text x="50" y="392" font-size="124" class="in" {d(.3)}>Șeremet<tspan fill="{t['brand']}">.</tspan></text>
  </g>
  {rows}

  <line x1="56" y1="446" x2="1144" y2="446" stroke="{t['line']}"/>
  <text x="56" y="484" class="mono in" {d(.9)} font-size="15" fill="{t['muted']}">INTERFACES · DESIGN SYSTEMS · REACT · TYPESCRIPT · SPRING BOOT</text>
  <text x="1110" y="484" class="mono in" {d(1)} font-size="15" fill="{t['text']}" text-anchor="end">hello, world</text>
  <rect class="caret" x="1128" y="470" width="10" height="18" fill="{t['brand']}"/>
"""
    return svg(h, body, css, "Denis Șeremet — Senior Frontend Developer and UI/UX Designer")


# ---------------------------------------------------------------- section labels
def label(t, num, title):
    body = f"""
  <text x="0" y="56" class="mono" font-size="16" fill="{t['accent']}">{num}</text>
  <text x="52" y="60" class="sans" font-size="36" font-weight="650" letter-spacing="-1" fill="{t['text']}">{title}</text>
  <line x1="380" y1="48" x2="{W}" y2="48" stroke="{t['line']}"/>
  <rect x="{W - 8}" y="44" width="8" height="8" fill="{t['brand']}"/>
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

    cols = [("REQUEST", t["accent2"]), ("SCHEDULED", t["muted"]), ("IN TRANSIT", t["accent"]), ("DONE", t["muted"])]
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

  <path d="M30 76 l14 8 v18 l-14 -8z" fill="#FF7A00"/><path d="M48 84 l14 -8 v18 l-14 8z" fill="#FF7A00" opacity=".8"/>
  <path d="M40 70 l12 -7 l10 6 l-12 7z" fill="#2F5BD3"/>
  <text x="74" y="96" class="sans" font-size="20" font-weight="700" fill="{t['text']}">Moves<tspan fill="#4C7BF4">Flow</tspan></text>
  {navsvg}
  <line x1="220" y1="52" x2="220" y2="{h}" stroke="{t['line']}"/>

  <text x="248" y="104" class="sans" font-size="28" font-weight="700" letter-spacing="-.5" fill="{t['text']}">Today</text>
  <text x="340" y="104" class="sans" font-size="16" fill="{t['muted']}">Dispatch overview</text>
  <rect x="1032" y="78" width="144" height="38" rx="10" fill="{t['brand']}"/>
  <text x="1104" y="103" class="sans" font-size="16" font-weight="600" fill="{t['onAccent']}" text-anchor="middle">+ New order</text>
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
            f'<circle cx="{x + 26}" cy="{y + 76}" r="9" fill="{t["muted"]}" opacity=".85"/>'
            f'<circle cx="{x + 40}" cy="{y + 76}" r="9" fill="{t["accent"]}" opacity=".85" stroke="{t["surface"]}" stroke-width="2"/>'
            f'<rect x="{x + 180 - cw}" y="{y + 66}" width="{cw}" height="20" rx="10" fill="none" stroke="{c}"/>'
            f'<text x="{x + 180 - cw / 2}" y="{y + 80}" class="mono" font-size="11" fill="{c}" text-anchor="middle">{chip.upper()}</text></g>')



# ---------------------------------------------------------------- experience timeline
EXPERIENCE = [
    ("JAN 2025 — NOW", "Senior Frontend Developer", "Urchin Systems", "Plextera microfrontends, AI widget", "CHIȘINĂU", True),
    ("SEP 2022 — JAN 2025", "Full Stack Developer", "S&amp;T Mold", "Customs Service of Moldova, E-Bursa", "CHIȘINĂU", False),
    ("DEC 2021 — SEP 2022", "Frontend Developer", "Minicode", "Xpedite Permits, Mirri, Angro", "CHIȘINĂU", False),
    ("MAY 2020 — DEC 2021", "Frontend Developer", "Freelance", "Websites for clients on Habr", "REMOTE", False),
]


def experience(t):
    rh = 112
    h = len(EXPERIENCE) * rh
    css = ".ring { animation: pulse 1.8s ease-out infinite; }"
    body = f'<line x1="276" y1="40" x2="276" y2="{h - 40}" stroke="{t["line"]}" stroke-width="2"/>'
    for i, (period, role, company, stack, where, now) in enumerate(EXPERIENCE):
        y = i * rh
        dot = (f'<circle class="ring" cx="276" cy="{y + 46}" r="6" fill="none" stroke="{t["accent"]}" stroke-width="2"/>'
               f'<circle cx="276" cy="{y + 46}" r="7" fill="{t["brand"]}" stroke="{t["accent"]}" stroke-width="2"/>') if now else \
              f'<circle cx="276" cy="{y + 46}" r="6" fill="{t["bg"]}" stroke="{t["muted"]}" stroke-width="2"/>'
        body += (f'<text x="0" y="{y + 51}" class="mono" font-size="13" fill="{t["accent"] if now else t["muted"]}">{period}</text>'
                 + dot +
                 f'<text x="316" y="{y + 54}" class="sans" font-size="26" font-weight="650" letter-spacing="-.5" fill="{t["text"]}">{role}</text>'
                 f'<text x="316" y="{y + 84}" class="sans" font-size="18" fill="{t["muted"]}"><tspan fill="{t["text"]}">{company}</tspan>  ·  {stack}</text>'
                 f'<text x="{W}" y="{y + 51}" class="mono" font-size="12" fill="{t["muted"]}" text-anchor="end">{where}</text>')
        if i < len(EXPERIENCE) - 1:
            body += f'<line x1="316" y1="{y + rh - 4}" x2="{W}" y2="{y + rh - 4}" stroke="{t["line"]}" opacity=".6"/>'
    return svg(h, body, css, "Experience: " + "; ".join(f"{r} at {c}, {p.title()}" for p, r, c, *_ in EXPERIENCE))


# ---------------------------------------------------------------- knowledge bento
import base64

LABELS = dict(ts="TypeScript", js="JavaScript", react="React", redux="Redux", nextjs="Next.js", vue="Vue",
              angular="Angular", html="HTML", css="CSS", sass="Sass", tailwind="Tailwind",
              styledcomponents="Styled", materialui="MUI", bootstrap="Bootstrap", svg="SVG", vite="Vite",
              webpack="Webpack", babel="Babel", gulp="Gulp", pug="Pug", git="Git", github="GitHub",
              gitlab="GitLab", figma="Figma", ps="Photoshop", ai="Illustrator", ae="After Effects",
              pr="Premiere", au="Audition", blender="Blender", autocad="AutoCAD", nodejs="Node.js",
              express="Express", nestjs="NestJS", java="Java", spring="Spring", maven="Maven",
              hibernate="Hibernate", postgres="Postgres", mysql="MySQL", mongodb="MongoDB",
              androidstudio="Android", docker="Docker", postman="Postman", linux="Linux", bash="Bash",
              powershell="PowerShell", rabbitmq="RabbitMQ", c="C", cpp="C++", py="Python", fastapi="FastAPI",
              php="PHP", gatsby="Gatsby", matlab="MATLAB", octave="Octave", arduino="Arduino",
              raspberrypi="Raspberry Pi", unity="Unity", godot="Godot", vscode="VS Code", idea="IntelliJ",
              visualstudio="Visual Studio")

# rows of (title, icons, columns-span out of 4)
KNOWLEDGE = [
    [("Frontend", "ts js react redux nextjs vue angular html css sass tailwind styledcomponents materialui bootstrap svg", 4)],
    [("Design", "figma ps ai ae pr au blender autocad", 2), ("Backend", "nodejs express nestjs java spring maven hibernate", 2)],
    [("Build & tooling", "vite webpack babel gulp pug git github gitlab", 2), ("DevOps & more", "docker postman linux bash powershell rabbitmq", 2)],
    [("Also experienced with", "c cpp py fastapi php gatsby matlab octave arduino raspberrypi", 4)],
    [("Databases", "postgres mysql mongodb", 1), ("Mobile", "react androidstudio", 1), ("Game dev", "unity godot", 1), ("Editors", "vscode idea visualstudio", 1)],
]

ICON, CELL_W, CELL_H, PAD, GAP, HEAD = 48, 82, 92, 24, 16, 70


def icon_uri(key, theme):
    raw = (OUT / "icons" / f"{key}-{theme}.svg").read_bytes()
    return "data:image/svg+xml;base64," + base64.b64encode(raw).decode()


def knowledge(t, theme):
    unit = (W - 3 * GAP) / 4
    y = 0
    body = ""
    n = 0
    for row in KNOWLEDGE:
        cards = []
        for title, keys, span in row:
            keys = keys.split()
            w = unit * span + GAP * (span - 1)
            cw = min(CELL_W, (w - 2 * PAD) / len(keys))
            per = len(keys) if cw >= 66 else max(1, int((w - 2 * PAD) // CELL_W))
            cw = cw if cw >= 66 else CELL_W
            rows = -(-len(keys) // per)
            cards.append((title, keys, w, per, rows, cw))
        h = HEAD + max(c[4] for c in cards) * CELL_H + 4
        x = 0
        for title, keys, w, per, rows, cw in cards:
            n += 1
            body += (f'<g class="in" {d(n * .06)}><rect x="{x + .5}" y="{y + .5}" width="{w - 1}" height="{h - 1}" rx="18" fill="{t["surface"]}" stroke="{t["line"]}"/>'
                     f'<text x="{x + PAD}" y="{y + 44}" class="mono" font-size="13" fill="{t["accent"]}">{n:02d}</text>'
                     f'<text x="{x + PAD + 36}" y="{y + 45}" class="sans" font-size="21" font-weight="650" letter-spacing="-.3" fill="{t["text"]}">{title.replace("&", "&amp;")}</text>'
                     f'<text x="{x + w - PAD}" y="{y + 44}" class="mono" font-size="13" fill="{t["muted"]}" text-anchor="end">{len(keys):02d}</text>')
            for k, key in enumerate(keys):
                cx = x + PAD + (k % per) * cw
                cy = y + HEAD + (k // per) * CELL_H
                body += (f'<image href="{icon_uri(key, theme)}" x="{cx + (cw - ICON) / 2:.1f}" y="{cy}" width="{ICON}" height="{ICON}"/>'
                         f'<text x="{cx + cw / 2:.1f}" y="{cy + ICON + 20}" class="sans" font-size="11.5" fill="{t["muted"]}" text-anchor="middle">{LABELS[key]}</text>')
            body += "</g>"
            x += w + GAP
        y += h + GAP
    return svg(int(y - GAP), body, "", "Knowledge: " + ", ".join(LABELS[k] for r in KNOWLEDGE for _, ks, _ in r for k in ks.split()))



# ---------------------------------------------------------------- selected projects
PROJECTS = [
    ("movesflow", "movesflow.it", "MovesFlow", ["Operations app for", "moving companies"], "PERSONAL"),
    ("plextera", "plextera.com", "Plextera", ["Workforce management and", "compliance platform"], "URCHIN"),
    ("frontiera", "Customs Service of Moldova", "FRONTIERA", ["Border-crossing information", "system with device integrations"], "S&amp;T · CUSTOMS"),
    ("ecustoms", "ecustoms.trade.gov.md", "Customs Portal", ["Public portal: taxes, parcel", "checks and MPay payments"], "S&amp;T · CUSTOMS"),
]


def project(t, i, domain, name, desc, tag):
    w, h = 392, 220
    body = f"""
  <rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="18" fill="{t['surface']}" stroke="{t['line']}"/>
  <text x="28" y="44" class="mono" font-size="13" fill="{t['accent']}">{i:02d}</text>
  <text x="{w - 28}" y="44" class="mono" font-size="12" fill="{t['muted']}" text-anchor="end">{tag}</text>
  <text x="28" y="98" class="sans" font-size="32" font-weight="700" letter-spacing="-.8" fill="{t['text']}">{name}</text>
  <text x="28" y="134" class="sans" font-size="18" fill="{t['muted']}">{desc[0]}</text>
  <text x="28" y="158" class="sans" font-size="18" fill="{t['muted']}">{desc[1]}</text>
  <line x1="28" y1="178" x2="{w - 28}" y2="178" stroke="{t['line']}"/>
  <text x="28" y="202" class="mono" font-size="12" fill="{t['text']}" opacity=".75">{domain}</text>
"""
    if "." in domain:  # only linkable projects get the arrow
        body += f"""<g transform="translate({w - 40} 197) scale(.8)"><circle r="18" fill="none" stroke="{t['line']}"/>
    <path d="M-5 5 L5 -5 M-3 -5 H5 V3" stroke="{t['accent']}" stroke-width="2" fill="none" stroke-linecap="round"/></g>"""
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{name}: {' '.join(desc)}"><title>{name}</title><style>{BASE_CSS}</style>{body}</svg>\n'



# ---------------------------------------------------------------- beyond code
LANGS = [("Romanian", "Native", 6), ("Russian", "C2", 6), ("English", "B2", 4), ("German", "A1", 1)]
AWARDS = [("Hackathon IX, UTM", "2023"), ("Hackathon, UTM", "2022"), ("Microelectronic Systems contest", "2022"),
          ("Earth Rover Innovation Challenge", "2021")]
HARDWARE = [("FarmBot", "automated crop growing"), ("SkyFly", "drone control app"),
            ("Work Inspector", "room sensor monitoring"), ("CyberCar", "Bluetooth-driven car")]


def beyond(t):
    cw, h, gap = 389, 300, 16
    body = ""
    heads = [("01", "Languages"), ("02", "Awards"), ("03", "Hardware &amp; IoT")]
    for c, (n, title) in enumerate(heads):
        x = c * (cw + gap)
        body += (f'<rect x="{x + .5}" y=".5" width="{cw - 1}" height="{h - 1}" rx="18" fill="{t["surface"]}" stroke="{t["line"]}"/>'
                 f'<text x="{x + 24}" y="44" class="mono" font-size="13" fill="{t["accent"]}">{n}</text>'
                 f'<text x="{x + 60}" y="45" class="sans" font-size="21" font-weight="650" letter-spacing="-.3" fill="{t["text"]}">{title}</text>')
        for r in range(4):
            y = 98 + r * 52
            body += f'<line x1="{x + 24}" y1="{y + 22}" x2="{x + cw - 24}" y2="{y + 22}" stroke="{t["line"]}" opacity=".6"/>'
            if c == 0:
                name, lvl, n6 = LANGS[r]
                body += (f'<text x="{x + 24}" y="{y}" class="sans" font-size="17" fill="{t["text"]}">{name}</text>'
                         f'<text x="{x + cw - 24}" y="{y}" class="mono" font-size="12" fill="{t["muted"]}" text-anchor="end">{lvl.upper()}</text>'
                         + "".join(f'<rect x="{x + 150 + k * 22}" y="{y - 10}" width="16" height="6" rx="3" fill="{t["brand"] if k < n6 else t["line"]}"/>' for k in range(6)))
            elif c == 1:
                name, yr = AWARDS[r]
                body += (f'<text x="{x + 24}" y="{y}" class="sans" font-size="16" fill="{t["text"]}">{name}</text>'
                         f'<text x="{x + cw - 24}" y="{y}" class="mono" font-size="12" fill="{t["muted"]}" text-anchor="end">{yr}</text>')
            else:
                name, what = HARDWARE[r]
                body += (f'<text x="{x + 24}" y="{y}" class="sans" font-size="16" fill="{t["text"]}">{name}'
                         f'<tspan fill="{t["muted"]}">  ·  {what}</tspan></text>')
    return svg(h, body, "", "Languages: Romanian native, Russian C2, English B2, German A1. Awards: hackathons at UTM 2022 and 2023, Microelectronic Systems contest 2022, Earth Rover Innovation Challenge 2021. Hardware projects: FarmBot, SkyFly, Work Inspector, CyberCar.")


# ---------------------------------------------------------------- footer
def footer(t):
    css = ".caret { animation: blink 1.1s steps(1) infinite; }"
    body = f"""
  <line x1="0" y1="1" x2="{W}" y2="1" stroke="{t['line']}"/>
  <text x="0" y="52" class="mono" font-size="14" fill="{t['muted']}">© 2026 DENIS ȘEREMET</text>
  <text x="{W - 24}" y="52" class="mono" font-size="14" fill="{t['muted']}" text-anchor="end">DESIGNED IN FIGMA · SHIPPED IN TYPESCRIPT</text>
  <rect class="caret" x="{W - 10}" y="38" width="10" height="18" fill="{t['brand']}"/>
"""
    return svg(72, body, css, "Footer")


SECTIONS = [("about", "01", "About"), ("experience", "02", "Experience"), ("projects", "03", "Selected projects"),
            ("knowledge", "04", "Knowledge"), ("beyond", "05", "Beyond code"), ("work", "06", "Side project"),
            ("contact", "07", "Elsewhere")]
VERSION = "v11"

if __name__ == "__main__":
    for name, t in THEMES.items():
        files = {"hero": hero(t), "movesflow-board": board(t), "knowledge": knowledge(t, name), "experience": experience(t), "beyond": beyond(t), "footer": footer(t)}
        for key, num, title in SECTIONS:
            files[f"label-{key}"] = label(t, num, title)
        for i, (slug, *rest) in enumerate(PROJECTS, 1):
            files[f"project-{slug}"] = project(t, i, *rest)
        for f, content in files.items():
            (OUT / f"{f}-{name}.{VERSION}.svg").write_text(content, encoding="utf-8")
    print("built", len(list(OUT.glob(f"*.{VERSION}.svg"))), "svgs")
