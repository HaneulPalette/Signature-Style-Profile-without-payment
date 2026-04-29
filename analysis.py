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
    if warm and bright and contrast > 60:
        return "Bright Spring"
    if warm and soft:
        return "Warm Spring"
    if warm and brightness > 150:
        return "Light Spring"

    # ☀️ SUMMER
    if cool and soft and brightness > 160:
        return "Light Summer"
    if cool and soft:
        return "Soft Summer"
    if cool and bright:
        return "True Summer"

    # 🍂 AUTUMN
    if warm and deep and soft:
        return "Soft Autumn"
    if warm and deep and contrast < 60:
        return "Muted Autumn"
    if warm and deep:
        return "Deep Autumn"
    if warm:
        return "True Autumn"

    # ❄️ WINTER
    if cool and bright and contrast > 70:
        return "Bright Winter"
    if cool and deep:
        return "Deep Winter"
    if cool:
        return "True Winter"

    return "Soft Autumn"


def analyze_image(file):

    img = Image.open(file).convert("RGB")
    img = img.resize((120,120))

    pixels = np.array(img).reshape(-1,3)

    r = np.mean(pixels[:,0])
    g = np.mean(pixels[:,1])
    b = np.mean(pixels[:,2])

    brightness = np.mean([r,g,b])
    contrast = np.std(pixels)

    season = classify_season(r,g,b,brightness,contrast)

    return {
        "undertone": "Warm" if r > b else "Cool",
        "season": season,
        "contrast": "Low" if contrast < 45 else "High",

        "palette": generate_palette(season),

        "recommend": {
            "formal": "Structured elegant tones matching your season",
            "casual": "Soft natural seasonal colors"
        },

        "avoid": "Avoid clashing undertone + neon colors",

        "grooming": "Hair tones should align with undertone harmony"
    }
