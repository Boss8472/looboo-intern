#!/usr/bin/env python3
"""Erzeugt alle Raster-Icons und das OG-Bild für looboo.de.

Aufruf (aus dem äußeren Repo):  python3 tools/make_icons.py
Ausgabe landet im htdocs-Submodule ./looboo/
Benötigt: Pillow
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "looboo"

INK = (17, 17, 17)
PAPER = (250, 248, 244)
ACCENT = (255, 90, 54)

SS = 8  # Supersampling-Faktor für glatte Kanten


def signet(size, *, rounded=True, safe=1.0, bg=INK, fg=PAPER):
    """Das 'oo'-Signet: zwei Ringe auf (abgerundetem) Quadrat.

    Geometrie in einem 32er-Raster, identisch zu favicon.svg.
    safe < 1 verkleinert das Motiv (für maskable Icons).
    """
    S = size * SS
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    u = S / 32
    if rounded:
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=7 * u, fill=bg)
    else:
        d.rectangle([0, 0, S, S], fill=bg)
    # Ringe: Mittelpunkte (10.5|16) und (21.5|16), Radius 4.5, Strich 3
    r, w = 4.5 * safe, 3 * safe
    for cx in (16 - 5.5 * safe, 16 + 5.5 * safe):
        ro = (r + w / 2) * u
        d.ellipse([cx * u - ro, 16 * u - ro, cx * u + ro, 16 * u + ro], fill=fg)
        ri = (r - w / 2) * u
        d.ellipse([cx * u - ri, 16 * u - ri, cx * u + ri, 16 * u + ri], fill=bg)
    # Akzentpunkt (Pupille) im rechten Ring
    pr = 1.25 * safe * u
    px = (16 + 5.5 * safe + 1.2 * safe) * u
    py = (16 + 1.0 * safe) * u
    d.ellipse([px - pr, py - pr, px + pr, py + pr], fill=ACCENT)
    return img.resize((size, size), Image.LANCZOS)


def og_image():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    font_path = "/System/Library/Fonts/HelveticaNeue.ttc"
    big = ImageFont.truetype(font_path, 190, index=1)   # Bold
    small = ImageFont.truetype(font_path, 44, index=0)  # Regular
    icon = signet(140)
    img.paste(icon, (96, 96), icon)
    d.text((90, 250), "looboo", font=big, fill=INK)
    d.text((100, 480), "Hier entsteht etwas Neues.", font=small, fill=(90, 90, 90))
    d.rectangle([0, H - 14, W, H], fill=ACCENT)
    img.save(OUT / "og-image.png", optimize=True)


def main():
    signet(180, rounded=False).save(OUT / "apple-touch-icon.png", optimize=True)
    signet(192).save(OUT / "icon-192.png", optimize=True)
    signet(512).save(OUT / "icon-512.png", optimize=True)
    signet(512, rounded=False, safe=0.72).save(OUT / "icon-maskable-512.png", optimize=True)
    base = signet(256)
    base.save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    og_image()
    print("Icons erzeugt in", OUT)


if __name__ == "__main__":
    main()
