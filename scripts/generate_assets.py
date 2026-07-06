#!/usr/bin/env python3
"""Generate the glass project cards and live stat cards for the profile README.

Stdlib only. Run from the repo root:  python3 scripts/generate_assets.py
Uses GITHUB_TOKEN if present (recommended in CI) for API calls.
"""
import json
import os
import urllib.request

USER = "pufferfish3e"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets")

LANG_COLORS = {
    "TypeScript": "#3178c6", "Python": "#3572A5", "CSS": "#663399",
    "Jupyter Notebook": "#DA5B0B", "HTML": "#e34c26", "JavaScript": "#f1e05a",
}

PROJECTS = [
    ("supervised-learning", ["scikit-learn", "pandas", "Jupyter"],
     "Supervised learning workflow with scikit-learn:", "training and evaluating ML models."),
    ("unsupervised-learning", ["scikit-learn", "Clustering"],
     "Unsupervised learning for my AI & Machine", "Learning CA2 project."),
    ("data-cleaning-workflow", ["pandas", "matplotlib", "Jupyter"],
     "Data cleaning, preprocessing and visualization", "workflow for Programming for Data Analytics."),
    ("b25_hackathon", ["Python", "Jupyter"],
     "Team hackathon build: rapid data exploration", "and modelling against the clock."),
]

GEO = [
    dict(g1x=0.85, g1y=0.9, g2x=0.1, g2y=0.1, wavey=350, wavey2=290, b1x=620, b1y=110),
    dict(g1x=0.1, g1y=0.85, g2x=0.9, g2y=0.15, wavey=330, wavey2=380, b1x=650, b1y=90),
    dict(g1x=0.9, g1y=0.15, g2x=0.15, g2y=0.9, wavey=360, wavey2=300, b1x=610, b1y=310),
    dict(g1x=0.5, g1y=1.0, g2x=0.95, g2y=0.05, wavey=340, wavey2=390, b1x=660, b1y=140),
]


def api(path):
    req = urllib.request.Request(f"https://api.github.com{path}")
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    req.add_header("Accept", "application/vnd.github+json")
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def wallpaper(g, extra_attrs=""):
    return f'''<g{extra_attrs}>
      <rect x="4" y="4" width="712" height="392" rx="40" fill="#0a0a0d"/>
      <rect x="4" y="4" width="712" height="392" rx="40" fill="url(#rg1)"/>
      <rect x="4" y="4" width="712" height="392" rx="40" fill="url(#rg2)"/>
      <path d="M-40 {g['wavey']} Q 200 {g['wavey2']} 420 {g['wavey']} T 780 {g['wavey2']}" stroke="#ff2d2d" stroke-width="60" stroke-opacity="0.18" fill="none"/>
      <circle cx="{g['b1x']}" cy="{g['b1y']}" r="70" fill="#ff2d2d" fill-opacity="0.12"/>
    </g>'''


def head(g):
    return f'''<svg width="720" height="400" viewBox="0 0 720 400" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,'SF Pro Display','Segoe UI','Helvetica Neue',Arial,sans-serif">
  <defs>
    <radialGradient id="rg1" cx="{g['g1x']}" cy="{g['g1y']}" r="0.65">
      <stop offset="0" stop-color="#ff2d2d" stop-opacity="0.55"/><stop offset="1" stop-color="#ff2d2d" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="rg2" cx="{g['g2x']}" cy="{g['g2y']}" r="0.5">
      <stop offset="0" stop-color="#8a0f0f" stop-opacity="0.6"/><stop offset="1" stop-color="#8a0f0f" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="sheen" x1="0" y1="0" x2="0.6" y2="1">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0.10"/>
      <stop offset="0.45" stop-color="#ffffff" stop-opacity="0.02"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0.045"/>
    </linearGradient>
    <linearGradient id="btn" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ff4b4b" stop-opacity="0.28"/><stop offset="1" stop-color="#c1121f" stop-opacity="0.22"/>
    </linearGradient>
    <filter id="soften" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="22"/></filter>
    <clipPath id="panel"><rect x="4" y="4" width="712" height="392" rx="40"/></clipPath>
  </defs>
  <g clip-path="url(#panel)">
{wallpaper(g)}
{wallpaper(g, ' filter="url(#soften)" opacity="0.85"')}
  </g>
  <rect x="4" y="4" width="712" height="392" rx="40" fill="url(#sheen)"/>
  <rect x="4.5" y="4.5" width="711" height="391" rx="39.5" fill="none" stroke="#ffffff" stroke-opacity="0.22"/>
  <path d="M64 4.5 H 580" stroke="#ffffff" stroke-opacity="0.3" stroke-width="1" stroke-linecap="round"/>
'''


def footer(left_text, button_text, bw=140):
    bx = 656 - bw
    return f'''  <path d="M64 302 H 656" stroke="#ffffff" stroke-opacity="0.1"/>
  <text x="64" y="344" font-size="14" fill="#8e8e93">{left_text}</text>
  <rect x="{bx}" y="320" width="{bw}" height="38" rx="19" fill="url(#btn)" stroke="#ff4b4b" stroke-opacity="0.45"/>
  <text x="{bx + (bw - 26) / 2:.0f}" y="344" font-size="14.5" fill="#ffb3b3" text-anchor="middle">{button_text}</text>
  <text x="640" y="344" font-size="15" fill="#ff6b6b" text-anchor="middle">&#8594;</text>
</svg>
'''


def chips_svg(chips, x, y):
    parts = []
    for c in chips:
        w = 34 + len(c) * 8.2
        parts.append(f'''  <rect x="{x}" y="{y}" width="{w:.0f}" height="34" rx="17" fill="#ffffff" fill-opacity="0.06" stroke="#ffffff" stroke-opacity="0.14"/>
  <text x="{x + w / 2:.0f}" y="{y + 22}" font-size="14" fill="#d1d1d6" text-anchor="middle">{c}</text>''')
        x += w + 12
    return "\n".join(parts)


def project_cards():
    os.makedirs(os.path.join(OUT, "projects"), exist_ok=True)
    for i, (name, chips, d1, d2) in enumerate(PROJECTS):
        body = f'''  <text x="64" y="106" font-size="40" font-weight="700" fill="#f5f5f7" letter-spacing="0.2">{name}</text>
  <text x="64" y="150" font-size="17.5" fill="#a1a1a6">{d1}</text>
  <text x="64" y="176" font-size="17.5" fill="#a1a1a6">{d2}</text>
{chips_svg(chips, 64, 210)}
'''
        svg = head(GEO[i]) + body + footer(f"{USER}/{name}", "View Project")
        with open(os.path.join(OUT, "projects", f"{name}.svg"), "w") as f:
            f.write(svg)


def stat_cards():
    user = api(f"/users/{USER}")
    repos = api(f"/users/{USER}/repos?per_page=100")
    own = [r for r in repos if not r["fork"]]
    commits = api(f"/search/commits?q=author:{USER}")["total_count"]
    prs = api(f"/search/issues?q=author:{USER}+type:pr")["total_count"]

    stats = [
        (str(commits), "commits"),
        (str(prs), "pull requests"),
        (str(user["public_repos"]), "repositories"),
        (str(user["followers"]), "followers"),
    ]
    cols = "".join(
        f'''    <text x="{64 + i * 170}" y="196" font-size="44" font-weight="700" fill="#f5f5f7">{v}</text>
    <text x="{64 + i * 170}" y="224" fill="#a1a1a6">{label}</text>
'''
        for i, (v, label) in enumerate(stats)
    )
    body = f'''  <text x="64" y="96" font-size="34" font-weight="700" fill="#f5f5f7">GitHub activity</text>
  <g font-size="15">
{cols}  </g>
'''
    g = dict(g1x=0.9, g1y=0.85, g2x=0.08, g2y=0.12, wavey=345, wavey2=285, b1x=640, b1y=100)
    with open(os.path.join(OUT, "stats.svg"), "w") as f:
        f.write(head(g) + body + footer(f"github.com/{USER}", "View Profile"))

    counts = {}
    for r in own:
        if r["language"]:
            counts[r["language"]] = counts.get(r["language"], 0) + 1
    langs = sorted(counts.items(), key=lambda kv: -kv[1])[:5]
    total = sum(n for _, n in langs)
    segs, labels = [], []
    x = 64.0
    for j, (ln, n) in enumerate(langs):
        w = 592 * n / total
        col = LANG_COLORS.get(ln, "#8e8e93")
        segs.append(f'    <rect x="{x:.1f}" y="150" width="{w:.1f}" height="12" fill="{col}"/>')
        lx = 64 + (j % 3) * 200
        ly = 216 + (j // 3) * 40
        labels.append(
            f'  <circle cx="{lx + 6}" cy="{ly - 5}" r="6" fill="{col}"/>'
            f'<text x="{lx + 22}" y="{ly}" font-size="15" fill="#d1d1d6">{ln} <tspan fill="#8e8e93">{round(100 * n / total)}%</tspan></text>'
        )
        x += w
    body = f'''  <text x="64" y="96" font-size="34" font-weight="700" fill="#f5f5f7">Most used languages</text>
  <rect x="63" y="149" width="594" height="14" rx="7" fill="#ffffff" fill-opacity="0.08"/>
  <clipPath id="barclip"><rect x="64" y="150" width="592" height="12" rx="6"/></clipPath>
  <g clip-path="url(#barclip)">
{chr(10).join(segs)}
  </g>
{chr(10).join(labels)}
'''
    g = dict(g1x=0.12, g1y=0.9, g2x=0.9, g2y=0.1, wavey=335, wavey2=385, b1x=615, b1y=95)
    with open(os.path.join(OUT, "langs.svg"), "w") as f:
        f.write(head(g) + body + footer(f"{len(own)} original repositories", "Browse Repos", 170))


if __name__ == "__main__":
    project_cards()
    stat_cards()
    print("assets generated")
