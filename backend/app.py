from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

app = Flask(__name__)
CORS(app)

stored = {}

LOGO_PATH = os.path.join(os.path.dirname(__file__), "logo.png")

# ---------------- ANALYZE ----------------
@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["image"]
    img = Image.open(file).convert("RGB")

    arr = np.array(img.resize((120,120)))

    brightness = np.mean(arr)/255
    r = np.mean(arr[:,:,0])
    b = np.mean(arr[:,:,2])

    tone = "Warm" if r > b else "Cool"
    depth = "Light" if brightness > 0.6 else "Deep"

    preview = f"{tone} tone detected with {depth} depth"

    stored["tone"] = tone
    stored["depth"] = depth

    return jsonify({"preview": preview})


# ---------------- PDF ----------------
@app.route("/pdf")
def pdf():

    file = "report.pdf"
    c = canvas.Canvas(file, pagesize=A4)

    w, h = A4
    y = h - 80

    # LOGO FIX (IMPORTANT)
    if os.path.exists(LOGO_PATH):
        c.drawImage(LOGO_PATH, 220, y, width=120, height=70)

    y -= 120

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "HANEUL PALETTE REPORT")

    y -= 40

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Tone: {stored.get('tone','')}")
    y -= 20
    c.drawString(50, y, f"Depth: {stored.get('depth','')}")

    c.save()

    return send_file(file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
