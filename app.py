from flask import Flask, render_template,request,jsonify
from services.eligibility import find_schemes
from services.ai_advisor import ask_ai
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/find-schemes", methods=["POST"])

def get_schemes():

    user_data = request.json

    schemes = find_schemes(user_data)

    return jsonify(schemes)

@app.route("/search-schemes", methods=["POST"])

def search_schemes():

    data = request.json

    keyword = data["keyword"].lower()

    with open(
        "data/processed/schemes.json",
        "r",
        encoding="utf-8"
    ) as file:

        schemes = json.load(file)

    results = []

    for scheme in schemes:

        if (
            keyword in scheme.get("name", "").lower()
            or keyword in scheme.get("description", "").lower()
            or keyword in scheme.get("ministry", "").lower()
        ):

            results.append(scheme)

    return jsonify(results)


@app.route("/ask-ai", methods=["POST"])
def ai_advisor():

    data = request.json

    answer = ask_ai(data)

    return jsonify({
        "answer": answer
    })

if __name__ == "__main__":
    app.run(debug=True)