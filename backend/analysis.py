import numpy as np
from PIL import Image
from palette import generate_palette

def classify_season(r, g, b, brightness, contrast):

    warm = r > b
    cool = b > r
    bright = brightness > 170
    soft = contrast < 45
    deep = brightness < 120

    # 🌸 SPRING
    if warm and bright:
        return "Bright Spring"
    if warm and soft:
        return "Light Spring"
    if warm:
        return "Warm Spring"

    # ☀️ SUMMER
    if cool and soft and bright:
        return "Light Summer"
    if cool and soft:
        return "Soft Summer"
    if cool:
        return "True Summer"

    # 🍂 AUTUMN
    if warm and deep and soft:
        return "Soft Autumn"
    if warm and deep:
        return "Deep Autumn"
    if warm:
        return "True Autumn"

    # ❄️ WINTER
    if cool and bright:
        return "Bright Winter"
    if cool and deep:
        return "Deep Winter"
    if cool:
        return "True Winter"

    return "Soft Autumn"


def analyze_image(file):

    image = Image.open(file).convert("RGB")
    image = image.resize((150, 150))

    pixels = np.array(image).reshape(-1, 3)

    r = np.mean(pixels[:, 0])
    g = np.mean(pixels[:, 1])
    b = np.mean(pixels[:, 2])

    brightness = np.mean([r, g, b])
    contrast = np.std(pixels)

    season = classify_season(r, g, b, brightness, contrast)

    undertone = "Warm" if r > b else "Cool"

    contrast_level = (
        "Low" if contrast < 40 else
        "Medium" if contrast < 70 else
        "High"
    )

    return {
        "undertone": undertone,
        "season": season,
        "contrast": contrast_level,

        "palette": generate_palette(season),

        "recommend": {
            "formal": "Muted structured tones, elegant neutrals",
            "casual": "Soft natural fabrics in seasonal tones"
        },

        "avoid": "Avoid clashing undertone colors and neon shades",

        "grooming": "Hair + beard tones should match undertone harmony"
    }
