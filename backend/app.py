from flask import Flask, request, jsonify
import tenseal as ts  # Import TenSEAL

app = Flask(__name__)

# Initialize TenSEAL context
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 60])
context.generate_galois_keys()

# Temporary vote storage (use a database in production)
votes = {"1": 0, "2": 0}  # Candidate 1 and Candidate 2 vote counts

# Encrypt a vote
def encrypt_vote(vote):
    encrypted_vote = context.encrypt([float(vote)])
    return encrypted_vote

# Decrypt a vote
def decrypt_vote(encrypted_vote):
    decrypted_vote = context.decrypt(encrypted_vote)
    return str(int(decrypted_vote[0]))  # Assuming the vote is "1" or "2"

@app.route("/vote", methods=["POST"])
def vote():
    data = request.get_json()

    encrypted_vote = data.get("vote")
    if encrypted_vote:
        decrypted_vote = decrypt_vote(encrypted_vote)

        if decrypted_vote in votes:
            votes[decrypted_vote] += 1
            return jsonify({"message": "Vote counted successfully!"}), 200
        else:
            return jsonify({"message": "Invalid vote"}), 400
    return jsonify({"message": "No vote data provided"}), 400

@app.route("/result", methods=["GET"])
def result():
    return jsonify(votes)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
