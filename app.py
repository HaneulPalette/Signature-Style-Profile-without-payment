from flask import Flask, request, jsonify

app = Flask(__name__)

# simple CORS fix (no install needed)
@app.after_request
def add_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["image"]

    from analysis import analyze_image
    result = analyze_image(file)

    return jsonify(result)


app.run(debug=True)
