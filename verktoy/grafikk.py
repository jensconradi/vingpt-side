#!/usr/bin/env python3
"""Ikoner og delekort for vingpt.no (22.11.2026). Kjøres på mini 1 (systemskrifter + VinGPT/ikon.py).

    python3 verktoy/grafikk.py            # favicon.ico, apple-touch-icon.png, ikon-512.png, bilder/sv/kort.jpg

Ikonet kommer fra /Applications/vingpt/VinGPT/ikon.py (eneste kilde). Delekortet i samme stil som
godvin/kort.jpg: tekst til venstre, toppen av skjermbildet til høyre. Ingen etikett i tekst.
"""
import importlib.util, os, sys
from pathlib import Path
from PIL import Image, ImageDraw

ROT = Path(__file__).resolve().parent.parent
APP = Path("/Applications/vingpt")

def last(navn, sti):
    spec = importlib.util.spec_from_file_location(navn, sti); m = importlib.util.module_from_spec(spec)
    sys.argv, gammel = [str(sti)], sys.argv
    spec.loader.exec_module(m); sys.argv = gammel
    return m

ik = last("ikon", APP / "VinGPT/ikon.py")
ramme = last("ramme", APP / "skjermbilder-ramme.py")

def ikoner():
    stor = ik.render(size=512).convert("RGB")
    stor.save(ROT / "ikon-512.png")
    stor.resize((180, 180), Image.LANCZOS).save(ROT / "apple-touch-icon.png")
    stor.resize((48, 48), Image.LANCZOS).save(ROT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

def delekort(ut, l1, rader, under, skjerm):
    B, H = 1200, 630
    img = Image.new("RGB", (B, H)); d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        d.line((0, y, B, y), fill=tuple(round(a + (b - a) * t) for a, b in zip(ramme.BAKGRUNN_TOPP, ramme.BAKGRUNN_BUNN)))
    # skjermbildet: toppen, avrundet, til høyre
    s = Image.open(skjerm).convert("RGB")
    bredde = 360; s = s.resize((bredde, round(s.height * bredde / s.width)), Image.LANCZOS).crop((0, 0, bredde, 560))
    img.paste(s, (780, 70), ramme.avrundet_maske((bredde, 560), 40))
    d.text((70, 72), "VinGPT", font=ramme.font(ramme.SANS, 34, "Semibold"), fill=(232, 196, 204))
    y = 140
    for linje in l1:
        d.text((70, y), linje, font=ramme.font(ramme.SANS, 60, "Bold"), fill=ramme.CREAM); y += 72
    y += 18
    for linje in rader:
        d.text((70, y), linje, font=ramme.font(ramme.SANS, 30, "Regular"), fill=ramme.CREAM_DEMPET); y += 42
    d.text((70, 550), under, font=ramme.font(ramme.SANS, 28, "Regular"), fill=(160, 140, 135))
    img.save(ut, quality=88)

if __name__ == "__main__":
    ikoner()
    delekort(ROT / "bilder/sv/kort.jpg",
             ["Vilket är det bästa", "vinet i lager på", "ditt Systembolag?"],
             ["Vinerna i din butik, rankade efter", "betyg från tusentals vinälskare.", "Fråga: ”rött vin till lamm under 150 kr”."],
             "iPhone · App Store", ROT / "bilder/sv/1-utforska.jpg")
    print("skrev ikon-512.png, apple-touch-icon.png, favicon.ico, bilder/sv/kort.jpg")
