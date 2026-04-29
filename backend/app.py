from flask import Flask, request, jsonify
from analysis import analyze_image

app = Flask(__name__)

# 🔥 Manual CORS fix (NO Flask-CORS needed)
@app.after_request
def add_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route("/analyze", methods=["POST", "OPTIONS"])
def analyze():

    if request.method == "OPTIONS":
        return jsonify({}), 200

    file = request.files["image"]
    result = analyze_image(file)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
