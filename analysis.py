import numpy as np
from PIL import Image
from palette import generate_palette

def analyze_image(file):

    img = Image.open(file).convert("RGB")
    img = img.resize((120,120))

    pixels = np.array(img).reshape(-1,3)

    r = np.mean(pixels[:,0])
    g = np.mean(pixels[:,1])
    b = np.mean(pixels[:,2])

    brightness = np.mean([r,g,b])
    contrast = np.std(pixels)

    warm = r > b
    cool = b > r
    high_contrast = contrast > 55
    low_contrast = contrast < 40
    bright = brightness > 170
    deep = brightness < 120

    # 🌸 SPRING
    if warm and bright and high_contrast:
        season = "Bright Spring"
    elif warm and bright:
        season = "Light Spring"
    elif warm and low_contrast:
        season = "Soft Spring"
    elif warm:
        season = "Warm Spring"

    # ☀️ SUMMER
    elif cool and bright:
        season = "Light Summer"
    elif cool and low_contrast:
        season = "Soft Summer"
    elif cool and high_contrast:
        season = "True Summer"

    # 🍂 AUTUMN
    elif warm and deep and low_contrast:
        season = "Soft Autumn"
    elif warm and deep and high_contrast:
        season = "Deep Autumn"
    elif warm and deep:
        season = "True Autumn"
    elif warm:
        season = "Muted Autumn"

    # ❄️ WINTER
    elif cool and bright and high_contrast:
        season = "Bright Winter"
    elif cool and deep and low_contrast:
        season = "Deep Winter"
    elif cool and deep:
        season = "True Winter"
    else:
        season = "Cool Winter"

    return {
        "undertone": "Warm" if warm else "Cool",
        "season": season,
        "contrast": "Low" if low_contrast else "High",
        "palette": generate_palette(season),

        "recommend": {
            "formal": "Season-matched structured outfits",
            "casual": "Soft coordinated natural tones"
        },

        "avoid": "Avoid clashing undertone + neon shades",
        "grooming": "Match hair tones with undertone harmony"
    }
