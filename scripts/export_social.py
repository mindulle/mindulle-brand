#!/usr/bin/env python3
"""SNS·콘테스트 플랫폼 PNG 내보내기 — 규격은 docs/SOCIAL_CHANNEL_INVENTORY.md §3·§4.

두 종류를 다룬다.
- SVG(브랜드 자산) → 플랫폼 규격 PNG (chromium으로 정확한 픽셀 크기 렌더)
- PNG(목업) → 콘테스트 참여작(600² 썸네일 · 1024 가로 상세)

사용::

    export_social.py --all                      # SVG 세트 전체
    export_social.py --only avatar,banner       # 이름 필터
    export_social.py --entry out/mockup/x.png   # 콘테스트 참여작
"""

import argparse
import base64
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOCIAL = ROOT / "assets/svg/social"
OUT = ROOT / "assets/png/social"

CHROME_CANDIDATES = ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable")

# 대상 규격 (2026-11-23 실측)
PRESETS = {
    # 파일 접두사: [(이름, 가로, 세로, 맞춤, 배경)]
    "avatar": [
        ("loudsourcing-132", 132, 132, "contain", "#FBF9F5"),
        ("99designs-500", 500, 500, "contain", "#FBF9F5"),
    ],
    "banner-behance": [("behance-3200x410", 3200, 410, "cover", "#FBF9F5")],
    "banner-dribbble": [("dribbble-1600x1200", 1600, 1200, "cover", "#FBF9F5")],
    "banner-linkedin": [("linkedin-1584x396", 1584, 396, "cover", "#FBF9F5")],
    "banner-x": [("x-1500x500", 1500, 500, "cover", "#111111")],
    "banner-99designs": [("99designs-2480x400", 2480, 400, "cover", "#05080E")],
    "banner-loudsourcing": [("loudsourcing-1920x240", 1920, 240, "cover", "#05080E")],
}

ENTRY_PRESETS = {
    # 이름: (가로, 세로, 맞춤) — fit=contain이면 잘리지 않게 여백을 둔다
    "thumbnail-600": (600, 600, "contain"),  # 라우드소싱 썸네일(1:1)
    "detail-1024": (1024, None, "width"),  # 라우드소싱 상세(가로 고정, 세로 자유)
    "99designs-1200": (1200, None, "width"),
}


def find_chrome():
    for name in CHROME_CANDIDATES:
        path = shutil.which(name)
        if path:
            return path
    raise SystemExit("chromium not found")


def render(svg_text, w, h, fit, bg, chrome):
    data = base64.b64encode(svg_text.encode()).decode()
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
html, body {{ margin: 0; background: {bg}; }}
img {{ display: block; width: {w}px; height: {h}px; object-fit: {fit}; }}
</style></head><body>
<img src="data:image/svg+xml;base64,{data}" alt="">
</body></html>"""
    # snap chromium은 /tmp을 볼 수 없다 → 저장소 안 임시 폴더를 쓴다
    tmp_root = ROOT / ".tmp-social"
    tmp_root.mkdir(exist_ok=True)
    out = Path(tempfile.mkdtemp(prefix="run-", dir=tmp_root)) / "page.html"
    out.write_text(html)
    png = out.with_suffix(".png")
    subprocess.run(
        [
            chrome,
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--screenshot={png}",
            f"--window-size={w},{h}",
            out.as_uri(),
        ],
        capture_output=True,
        check=True,
    )
    data = png.read_bytes()
    shutil.rmtree(out.parent, ignore_errors=True)
    return data


def entry_from_png(png_path, w, h, fit="width", bg="#FBF9F5"):
    """목업 PNG를 플랫폼 규격으로. width=폭 맞춤, contain=잘리지 않게 여백."""
    from PIL import Image

    im = Image.open(png_path).convert("RGB")
    if fit == "width":
        h = h or round(im.height * w / im.width)
        return im.resize((w, h), Image.LANCZOS)

    # contain: 정사각 캔버스에 맞춰 축소 후 가운데 배치
    scale = min(w / im.width, h / im.height)
    resized = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    canvas = Image.new("RGB", (w, h), bg)
    canvas.paste(resized, ((w - resized.width) // 2, (h - resized.height) // 2))
    return canvas


def main():
    ap = argparse.ArgumentParser(description="SNS·콘테스트 PNG 내보내기")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--only", default="", help="이름 필터(쉼표)")
    ap.add_argument("--entry", default=None, help="목업 PNG 경로 → 참여작 세트")
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    results = []

    if args.entry:
        src = Path(args.entry)
        if not src.is_file():
            raise SystemExit(f"PNG가 없습니다: {src}")
        for name, (w, h, fit) in ENTRY_PRESETS.items():
            im = entry_from_png(src, w, h, fit)
            target = out_dir / f"{src.stem}-{name}.png"
            im.save(target, "PNG", optimize=True)
            results.append({"file": target.name, "size": [im.width, im.height], "bytes": target.stat().st_size})

    filters = [f.strip() for f in args.only.split(",") if f.strip()]

    if args.all or filters:
        chrome = find_chrome()
        svgs = sorted(SOCIAL.glob("*.svg"))
        if filters:
            svgs = [p for p in svgs if any(f in p.name for f in filters)]
        if not svgs:
            raise SystemExit(f"SVG가 없습니다: {SOCIAL}")
        for svg in svgs:
            key = next((k for k in PRESETS if svg.name.startswith(k)), None)
            if not key:
                continue
            text = svg.read_text()
            for name, w, h, fit, bg in PRESETS[key]:
                png = render(text, w, h, fit, bg, chrome)
                # 아바타는 dark/light를 둘 다 쓰므로 원본 이름을 붙인다
                file_name = f"{svg.stem}-{name}.png" if key == "avatar" else f"{name}.png"
                target = out_dir / file_name
                target.write_bytes(png)
                results.append(
                    {
                        "file": target.name,
                        "size": [w, h],
                        "bytes": target.stat().st_size,
                        "sha256": hashlib.sha256(png).hexdigest(),
                    }
                )

    manifest = out_dir / "social.manifest.json"
    manifest.write_text(json.dumps({"presets": results}, indent=4, ensure_ascii=False) + "\n")
    if args.json:
        print(json.dumps({"files": results}, ensure_ascii=False))
    else:
        for r in results:
            print(f"  {r['file']:34s} {r['size'][0]}×{r['size'][1]}  {r['bytes'] // 1024}KB")
        print(f"{len(results)}개 · {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
