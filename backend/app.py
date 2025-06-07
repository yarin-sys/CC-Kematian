from flask import Flask, request, jsonify, send_file
import tenseal as ts
import os
import base64

app = Flask(__name__)

# Initialize TenSEAL context
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 60])
context.generate_galois_keys()

# Temporary vote storage (use a database in production)
# Store encrypted votes for demonstration purposes
encrypted_votes_storage = []
votes = {"1": 0, "2": 0} # Clear vote counts will be derived from encrypted_votes_storage

# Encrypt a vote using TenSEAL
def encrypt_vote_tenseal(vote_value):
    # Ensure vote_value is a float for CKKS
    return ts.ckks_vector(context, [float(vote_value)])

# Decrypt a vote using TenSEAL
def decrypt_vote_tenseal(encrypted_vote_ts):
    # encrypted_vote_ts should be a TenSEAL encrypted vector object
    decrypted_vote_list = encrypted_vote_ts.decrypt()
    return str(int(round(decrypted_vote_list[0]))) # Round to nearest integer for candidate number

@app.route("/")
def serve_voting_page():
    # Construct the path to your votingpage.html
    # Assumes votingpage.html is in the parent directory of the backend folder
    return send_file(os.path.join(os.path.dirname(__file__), '..', 'votingpage.html'))

@app.route("/vote", methods=["POST"])
def vote():
    data = request.get_json()

    # The frontend is sending a base64 encoded string as 'vote'
    simulated_encrypted_vote_b64 = data.get("vote")
    
    if simulated_encrypted_vote_b64:
        try:
            # Decode the base64 string to get the original vote value (e.g., "1" or "2")
            plain_vote_str = base64.b64decode(simulated_encrypted_vote_b64).decode('utf-8')
            plain_vote_int = int(plain_vote_str)

            # --- This is where the FHE magic happens on the backend ---
            # Encrypt the plain vote using TenSEAL
            encrypted_vote_ts = encrypt_vote_tenseal(plain_vote_int)
            
            # Store the *TenSEAL encrypted object* (for demonstration/further FHE operations)
            # In a real scenario, you'd store the serialized bytes of this object in a DB.
            encrypted_votes_storage.append(encrypted_vote_ts.serialize()) # Store serialized bytes

            # To "count" the vote, we would ideally perform homomorphic addition here
            # and then decrypt the final sum. For simplicity, and to show TenSEAL decryption,
            # we'll decrypt the individual vote received to update our 'votes' dictionary.
            # In a real FHE voting system, you'd add encrypted votes together and then decrypt the sum.
            decrypted_candidate = decrypt_vote_tenseal(encrypted_vote_ts)


            if decrypted_candidate in votes:
                votes[decrypted_candidate] += 1
                return jsonify({"message": f"Vote for Candidate {decrypted_candidate} counted successfully!"}), 200
            else:
                return jsonify({"message": "Invalid decrypted vote"}), 400

        except Exception as e:
            print(f"Error processing vote: {e}")
            return jsonify({"message": "Error processing vote"}), 400
    return jsonify({"message": "No vote data provided"}), 400

@app.route("/result", methods=["GET"])
def result():
    # In a full FHE system, here you'd sum all encrypted_votes_storage homomorphically
    # and then decrypt the final sum to get total counts.
    # For this demonstration, 'votes' dictionary is directly updated.
    return jsonify(votes)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)