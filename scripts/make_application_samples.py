#!/usr/bin/env python3
"""99designs 지원서용 작품 시트 6점을 만든다.

각 시트는 1200×1500 PNG 한 장으로, 히어로 이미지 + 영문 제목·설명 + 메타 정보를 담는다.
이미지는 HTML로 조판한 뒤 Chromium headless로 캡처한다.

사용:
    python3 scripts/make_application_samples.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SONAGI = ROOT.parent / "sonagi-assets"
CAP = SONAGI / ".tmp-samples" / "cap"
OUT = ROOT / "assets" / "png" / "99designs-application"

PAPER = "#FBF9F5"
INK = "#161616"
MUTED = "#63635E"
ACCENT = "#B4551F"


# ── 토큰 시트용 데이터 ────────────────────────────────────────────────
def token_panels() -> tuple[str, str]:
    prim = json.loads((SONAGI / "tokens" / "primitives.json").read_text())
    sem = json.loads((SONAGI / "tokens" / "semantic.json").read_text())

    scale_rows = []
    for name, steps in prim.items():
        cells = "".join(f'<div class="sw"><i style="background:{hexv}"></i><b>{step}</b><s>{hexv}</s></div>' for step, hexv in steps.items())
        scale_rows.append(f'<div class="scale"><span class="scale-name">{name}</span><div class="sw-row">{cells}</div></div>')
    scales = "".join(scale_rows)

    themes = []
    for theme, values in sem.items():
        rows = "".join(f'<div class="sem"><i style="background:{v}"></i><code>{k}</code><s>{v}</s></div>' for k, v in values.items())
        themes.append(f'<div class="theme"><h4>{theme}</h4><div class="sem-grid">{rows}</div></div>')
    return scales, "".join(themes)


def uri(path: Path) -> str:
    return path.resolve().as_uri()


SHEETS = []


def sheet(**kw):
    SHEETS.append(kw)


sheet(
    slug="01-portfolio-webgl",
    index="01",
    category="WEB · INTERACTIVE",
    title="Mindulle Atelier — WebGL Portfolio",
    subtitle="A scroll-driven 3D story in four acts",
    body=(
        "A portfolio that behaves like a landscape rather than a page. Four acts — "
        "threshold, rain, dandelion, release — each a low-poly scene with its own light, "
        "fog and ambience. Korean editorial typography sits over the WebGL canvas, and the "
        "scroll position drives the camera so the story never breaks."
    ),
    meta=[("Role", "Design & build"), ("Stack", "Three.js · GLSL · Next.js"), ("Year", "2026")],
    images=[(CAP / "portfolio-hero.png", "Act 01 · threshold", "full"), (CAP / "portfolio-2.png", "Act 02 · dandelion field", "full")],
)

sheet(
    slug="02-blog-editorial",
    index="02",
    category="WEB · EDITORIAL",
    title="Mindulle Garden — Editorial Blog",
    subtitle="Constraints enforced by code, not by discipline",
    body=(
        "An editorial system for a personal blog. Masthead, volume markers and a two-column "
        "dispatch grid share one type scale; articles are generated from MDX so layout, "
        "measure and hierarchy cannot drift between posts."
    ),
    meta=[("Role", "Design & build"), ("Stack", "Next.js · MDX · CSS tokens"), ("Year", "2026")],
    images=[(CAP / "blog-front.png", "Front page · volume 01", "full"), (CAP / "blog-article.png", "Article · case study layout", "full")],
)

sheet(
    slug="03-packaging-label",
    index="03",
    category="PACKAGING · PRINT",
    title="Sonagi Tea — Print-Ready Label",
    subtitle="Bleed, separation and barcode built into the spec",
    body=(
        "Label system for a Korean green tea. Front and side panels are defined as a data "
        "contract, then rendered with 3mm bleed, CMYK separation, crop marks and a reserved "
        "barcode quiet zone — press-ready without a redesign loop at the print shop."
    ),
    meta=[("Role", "Design & prepress"), ("Output", "CMYK PDF · 90×60mm + bleed"), ("Year", "2026")],
    images=[
        (SONAGI / "out" / "mockup" / "sonagi-mockup@2x.png", "Front and side panels", "full"),
        (SONAGI / "out" / "pkgmock" / "sonagi-tea-label@2x.png", "Proof · bleed and fold marks", "band"),
    ],
)

sheet(
    slug="04-identity-system",
    index="04",
    category="BRAND IDENTITY",
    title="Sonagi — Identity System",
    subtitle="One mark, one accent, defined clear space",
    body=(
        "A quiet identity built on one mark — a seed with three falling lines — and a single "
        "terracotta accent. Logo construction, colour scales and the type specimen are set as "
        "plates rather than slides, with clear space and minimum size defined so print, app "
        "icon and signage stay consistent."
    ),
    meta=[("Role", "Identity & guidelines"), ("Deliverable", "8-plate brand book"), ("Year", "2026")],
    images=[
        (SONAGI / "out" / "brandsheet-dist" / "02-logo@1x.png", "Logo construction plate", "pair"),
        (SONAGI / "out" / "brandsheet-dist" / "05-type@1x.png", "Type specimen plate", "pair"),
    ],
)

sheet(
    slug="05-design-tokens",
    index="05",
    category="DESIGN SYSTEM",
    title="Design Tokens — Two Themes, One Contract",
    subtitle="Primitives compile to CSS variables and Figma Variables",
    body=(
        "Eight primitive scales and two semantic themes are derived from a single JSON "
        "source, then compiled to CSS custom properties and Figma Variables. Design and code "
        "read the same contract, so a theme change is one commit rather than a redesign."
    ),
    meta=[("Role", "System design"), ("Scope", "8 scales · 2 themes · 34 semantics"), ("Year", "2026")],
    tokens=True,
)

sheet(
    slug="06-studio-collateral",
    index="06",
    category="BRAND COLLATERAL",
    title="Studio Collateral — Cross-Format Typography",
    subtitle="One grid across three aspect ratios",
    body=(
        "Banner system for X, LinkedIn and 99designs. The wordmark, rule and accent hold "
        "their place while the ratio shifts from 3:1 to 6.2:1. The same typographic grid as "
        "the print work, redrawn per channel rather than re-composed."
    ),
    meta=[("Role", "Art direction"), ("Formats", "1500×500 · 1584×396 · 2480×400"), ("Year", "2026")],
    images=[
        (ROOT / "assets" / "png" / "social" / "x-1500x500.png", "X · 3:1", "full"),
        (ROOT / "assets" / "png" / "social" / "linkedin-1584x396.png", "LinkedIn · 4:1", "full"),
        (ROOT / "assets" / "png" / "social" / "99designs-2480x400.png", "99designs · 6.2:1", "full"),
    ],
)

CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  margin: 0; width: 1200px; height: 1500px; background: PAPER;
  font-family: 'Lato', 'NanumSquare', sans-serif; color: INK;
  padding: 72px 76px 56px; display: flex; flex-direction: column;
}
.rule { height: 2px; background: INK; }
.top { display: flex; justify-content: space-between; align-items: baseline;
       margin-top: 12px; font-family: 'JetBrains Mono', monospace; font-size: 12px;
       letter-spacing: 2.4px; color: MUTED; }
.top b { color: ACCENT; font-weight: 600; }
h1 { font-size: 52px; line-height: 1.06; letter-spacing: -1.1px; font-weight: 900;
     margin: 54px 0 0; max-width: 940px; }
h2 { font-size: 21px; font-weight: 400; color: MUTED; margin: 16px 0 0; letter-spacing: .2px; }
p.body { font-size: 17px; line-height: 1.72; color: #3A3A36; margin: 34px 0 0; max-width: 940px; }
.figs { margin-top: 44px; display: flex; flex-direction: column; gap: 18px; }
figure { margin: 0; }
.shot { border: 1px solid #DCD7CB; background: #fff; overflow: hidden; }
.shot img { display: block; width: 100%; }
figcaption { font-family: 'JetBrains Mono', monospace; font-size: 11px;
             letter-spacing: 1.6px; color: MUTED; margin-top: 8px; text-transform: uppercase; }
.pair { display: flex; gap: 22px; margin-top: 40px; }
.pair figure { flex: 1; }
.pair .shot { max-height: 720px; }
.pair img { width: 100%; display: block; }
.meta { margin-top: auto; padding-top: 26px; border-top: 1px solid #DCD7CB;
        display: flex; gap: 52px; font-family: 'JetBrains Mono', monospace; font-size: 11.5px;
        letter-spacing: 1.2px; color: MUTED; text-transform: uppercase; }
.meta span b { display: block; color: INK; letter-spacing: .4px; margin-top: 5px;
               text-transform: none; font-family: 'Lato'; font-size: 13px; }
.scales { margin-top: 34px; }
.scale { display: flex; align-items: center; gap: 14px; margin-bottom: 9px; }
.scale-name { width: 92px; font-family: 'JetBrains Mono', monospace; font-size: 11px;
              color: MUTED; letter-spacing: 1px; }
.sw-row { display: flex; flex: 1; gap: 3px; }
.sw { flex: 1; }
.sw i { display: block; height: 22px; border: 1px solid #00000014; }
.sw b { display: block; font-size: 8.5px; font-family: 'JetBrains Mono', monospace;
        color: MUTED; margin-top: 3px; font-weight: 400; }
.sw s { display: none; text-decoration: none; }
.themes { display: flex; gap: 20px; margin-top: 26px; }
.theme { flex: 1; border: 1px solid #DCD7CB; padding: 16px 16px 12px; }
.theme h4 { margin: 0 0 12px; font-family: 'JetBrains Mono', monospace; font-size: 11px;
            letter-spacing: 1.6px; text-transform: uppercase; color: INK; }
.sem { display: flex; align-items: center; gap: 8px; margin-bottom: 5px; }
.sem i { width: 14px; height: 14px; border: 1px solid #00000018; flex: none; }
.sem code { font-family: 'JetBrains Mono', monospace; font-size: 9px; color: #3A3A36; min-width: 118px; }
.sem s { font-family: 'JetBrains Mono', monospace; font-size: 8.5px; color: MUTED; text-decoration: none; }
"""


def build_html(s: dict) -> str:
    css = CSS.replace("PAPER", PAPER).replace("INK", INK).replace("MUTED", MUTED).replace("ACCENT", ACCENT)

    figs = ""
    if s.get("tokens"):
        scales, themes = token_panels()
        figs = f'<div class="scales">{scales}</div><div class="themes">{themes}</div>'
    else:
        imgs = s["images"]
        mode = imgs[0][2]
        if mode == "pair":
            cells = "".join(
                f'<figure><div class="shot"><img src="{uri(p)}"></div>'
                f'<figcaption>{cap}</figcaption></figure>' for p, cap, _ in imgs
            )
            figs = f'<div class="pair">{cells}</div>'
        else:
            cells = []
            for p, cap, m in imgs:
                style = ' style="height:280px;object-fit:cover;object-position:center"' if m == "band" else ""
                cells.append(
                    f'<figure><div class="shot"><img src="{uri(p)}"{style}></div>'
                    f'<figcaption>{cap}</figcaption></figure>'
                )
            figs = f'<div class="figs">{"".join(cells)}</div>'

    meta = "".join(f"<span>{k}<b>{v}</b></span>" for k, v in s["meta"])
    return f"""<!doctype html><meta charset="utf-8"><style>{css}</style>
<div class="rule"></div>
<div class="top"><span>WORK SAMPLE <b>{s["index"]}</b> / 06</span>
<span>{s["category"]}</span><span>MINDULLE STUDIO</span></div>
<div class="rule"></div>
<h1>{s["title"]}</h1>
<h2>{s["subtitle"]}</h2>
<p class="body">{s["body"]}</p>
{figs}
<div class="meta">{meta}</div>
"""


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = ROOT / ".tmp-samples"
    tmp.mkdir(exist_ok=True)
    made = []
    for s in SHEETS:
        page = (tmp / f"{s['slug']}.html").resolve()
        page.write_text(build_html(s), encoding="utf-8")
        out = OUT / f"{s['slug']}.png"
        subprocess.run(
            [
                "chromium",
                "--headless",
                "--no-sandbox",
                "--disable-gpu",
                "--hide-scrollbars",
                "--allow-file-access-from-files",
                "--force-device-scale-factor=1",
                f"--screenshot={out}",
                "--window-size=1200,1500",
                page.as_uri(),
            ],
            capture_output=True,
        )
        if not out.exists():
            print(f"FAIL {s['slug']}", file=sys.stderr)
            return 1
        made.append((out, out.stat().st_size))
    for path, size in made:
        print(f"{path.name:34s} {size / 1024:7.0f} KB")
    print(f"{len(made)}개 · {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
