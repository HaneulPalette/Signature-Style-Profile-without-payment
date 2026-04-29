from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["image"]

    from analysis import analyze_image
    result = analyze_image(file)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
