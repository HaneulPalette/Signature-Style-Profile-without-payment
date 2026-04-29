from flask import Flask, request, jsonify
from analysis import analyze_image

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["image"]
    result = analyze_image(file)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
