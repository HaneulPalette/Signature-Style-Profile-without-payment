from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
import numpy as np
from reportlab.pdfgen import canvas

app = Flask(__name__)
CORS(app)

stored = {}

# ---------------- ANALYZE IMAGE ----------------
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


# ---------------- PDF GENERATION ----------------
@app.route("/pdf")
def pdf():

    file = "report.pdf"
    c = canvas.Canvas(file)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "HANEUL PALETTE REPORT")

    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"Tone: {stored.get('tone','')}")
    c.drawString(50, 740, f"Depth: {stored.get('depth','')}")

    c.save()

    return send_file(file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
