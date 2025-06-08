from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

votes = {
    "Candidate A": 0,
    "Candidate B": 0
}

@app.route("/")
def index():
    return render_template("votingpage.html")

@app.route("/vote", methods=["POST"])
def vote():
    try:
        encrypted_vote = request.json.get("encrypted_vote")
        if not encrypted_vote:
            return jsonify({"message": "No vote received"}), 400

        # Simulated decryption (base64 decode)
        decoded_bytes = base64.b64decode(encrypted_vote)
        plain_vote_str = decoded_bytes.decode("utf-8")

        if plain_vote_str == "Candidate A":
            votes["Candidate A"] += 1
        elif plain_vote_str == "Candidate B":
            votes["Candidate B"] += 1
        else:
            return jsonify({"message": "Invalid vote value"}), 400

        return jsonify({"message": f"Vote for {plain_vote_str} recorded successfully!"}), 200

    except Exception as e:
        return jsonify({"message": f"Error processing vote: {str(e)}"}), 500

@app.route("/results", methods=["GET"])
def get_results():
    return jsonify(votes)

if __name__ == "__main__":
    app.run(debug=True)
