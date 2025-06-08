from flask import Flask, request, jsonify, send_file
import tenseal as ts
import os
import base64

app = Flask(__name__)

# Initialize TenSEAL context (CKKS scheme)
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 60])
context.generate_galois_keys()

encrypted_votes_storage = []
votes = {"1": 0, "2": 0}

def encrypt_vote_tenseal(vote_value):
    return ts.ckks_vector(context, [float(vote_value)])

def decrypt_vote_tenseal(encrypted_vote_ts):
    return str(int(round(encrypted_vote_ts.decrypt()[0])))

@app.route("/")
def serve_voting_page():
    return send_file(os.path.join(os.path.dirname(__file__), '..', 'votingpage.html'))

@app.route("/vote", methods=["POST"])
def vote():
    data = request.get_json()
    simulated_encrypted_vote_b64 = data.get("vote")
    
    if simulated_encrypted_vote_b64:
        try:
            plain_vote_str = base64.b64decode(simulated_encrypted_vote_b64).decode('utf-8')
            plain_vote_int = int(plain_vote_str)

            encrypted_vote_ts = encrypt_vote_tenseal(plain_vote_int)
            encrypted_votes_storage.append(encrypted_vote_ts.serialize())

            decrypted_candidate = decrypt_vote_tenseal(encrypted_vote_ts)

            if decrypted_candidate in votes:
                votes[decrypted_candidate] += 1
                return jsonify({
                    "message": f"Vote for Candidate {decrypted_candidate} counted successfully!",
                    "tenseal_encrypted_hex": encrypted_vote_ts.serialize().hex()[:100] + "..."
                }), 200
            else:
                return jsonify({"message": "Invalid decrypted vote"}), 400

        except Exception as e:
            print(f"Error processing vote: {e}")
            return jsonify({"message": "Error processing vote"}), 400

    return jsonify({"message": "No vote data provided"}), 400

@app.route("/result", methods=["GET"])
def result():
    return jsonify(votes)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
