import numpy as np
from PIL import Image
from palette import generate_palette

def classify(r, g, b, bright, contrast):

    warm = r > b
    cool = b > r

    if warm and bright:
        season = "Warm Spring"
    elif cool and bright:
        season = "Light Summer"
    elif warm and not bright:
        season = "Soft Autumn"
    else:
        season = "True Winter"

    return season


def analyze_image(file):

    img = Image.open(file).convert("RGB")
    img = img.resize((100,100))

    pixels = np.array(img).reshape(-1,3)

    r = np.mean(pixels[:,0])
    g = np.mean(pixels[:,1])
    b = np.mean(pixels[:,2])

    bright = np.mean([r,g,b]) > 140
    contrast = np.std(pixels)

    season = classify(r,g,b,bright,contrast)

    return {
        "undertone": "Warm" if r > b else "Cool",
        "season": season,
        "contrast": "Low" if contrast < 50 else "High",
        "palette": generate_palette(season),

        "recommend": {
            "formal": "Elegant neutral tones",
            "casual": "Soft seasonal colors"
        },

        "avoid": "Avoid neon and clashing tones",
        "grooming": "Match hair tones with undertone"
    }
