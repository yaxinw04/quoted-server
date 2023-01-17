import random
import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# TODO: sqlite

data = []

@app.route("/quotes", methods=["GET", "POST"])
def quotes():
    if request.method == "POST":
        new_quote = request.json

        # validation (incomplete, more checks needed)
        if not ("quote" in new_quote and "user" in new_quote):
            return jsonify({"error": "Missing required fields"}), 400

        # copies every property from new_quote and adds
        # an additional property called "created"
        data.append({
            **new_quote,
            "created": datetime.datetime.now().isoformat()
        })

        return jsonify(new_quote)
    else: # GET
        return jsonify(data)

@app.route("/quotes/generate", methods=["GET"])
def quote_generate():
    # if data is empty
    if not data:
        return jsonify({ "error": "No quotes"})
    quote = random.choice(data)
    return jsonify(quote)