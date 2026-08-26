#!/usr/bin/env python3
"""Генерит аватарку канала toptestsoft (640x640 PNG) тёмно-зелёную,
в стиле скина dark-forest. Без внешних зависимостей, кроме PIL."""
from PIL import Image, ImageDraw, ImageFont
import os

SIZE = 640
img = Image.new("RGB", (SIZE, SIZE), (14, 28, 20))  # тёмно-зелёный фон (#0e1c14)
d = ImageDraw.Draw(img)

# круг-«орбита» акцентным зелёным
accent = (74, 222, 128)  # #4ade80
d.ellipse([140, 140, 500, 500], outline=accent, width=14)
d.ellipse([230, 230, 410, 410], outline=(45, 212, 191), width=6)

# текст по центру
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 150)
except Exception:
    font = ImageFont.load_default()
txt = "AI"
b = d.textbbox((0, 0), txt, font=font)
w, h = b[2] - b[0], b[3] - b[1]
d.text(((SIZE - w) / 2 - b[0], (SIZE - h) / 2 - b[1]), txt, fill=accent, font=font)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "avatar.png")
img.save(out)
print("сохранено:", out)
