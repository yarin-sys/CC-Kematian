from flask import Flask, request, jsonify, send_file # Add send_file
import tenseal as ts
import os # Import os for path manipulation

app = Flask(__name__)

# Initialize TenSEAL context
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 60])
context.generate_galois_keys()

# Temporary vote storage (use a database in production)
votes = {"1": 0, "2": 0}  # Candidate 1 and Candidate 2 vote counts

# Encrypt a vote (This function is not directly used in the current frontend,
# as the frontend sends unencrypted votes to be decrypted by the backend.
# However, it's good to keep if you plan to move encryption to the frontend later.)
def encrypt_vote(vote):
    encrypted_vote = context.encrypt([float(vote)])
    return encrypted_vote

# Decrypt a vote
def decrypt_vote(encrypted_vote):
    # Ensure encrypted_vote is a TenSEAL encrypted vector if it's coming from an actual FHE operation
    # For this current setup, as frontend sends plain text, we directly convert
    # If you intend for FHE in frontend, the 'encrypted_vote' would be bytes and need deserialization
    try:
        # Assuming the vote is sent as a string "1" or "2" from the frontend directly
        # and not an actual TenSEAL encrypted object.
        # If it were an actual TenSEAL object, you would deserialize it first.
        # For now, let's assume the vote received is the plain text string.
        # This part of the code needs to be adjusted based on whether the frontend
        # truly encrypts the vote before sending, or if 'encrypted_vote' is a misnomer
        # for a plain text value.
        # Given script.js, it's sending the vote directly as a string.
        decrypted_vote = float(encrypted_vote) # Convert to float for consistency if it was encrypted
        return str(int(decrypted_vote))
    except ValueError:
        # If it's not a direct float conversion, perhaps it's a serialized TenSEAL object
        # This part would be relevant if actual FHE was happening in the frontend
        try:
            enc_v = ts.ckks_vector_from(context, bytes.fromhex(encrypted_vote))
            decrypted_vote_list = enc_v.decrypt()
            return str(int(decrypted_vote_list[0]))
        except Exception as e:
            print(f"Error decrypting: {e}")
            return None # Indicate decryption failure


@app.route("/")
def serve_voting_page():
    # Construct the path to your votingpage.html
    # Assumes votingpage.html is in the parent directory of the backend folder
    # or wherever your script is being run from relative to backend/app.py
    return send_file(os.path.join(os.path.dirname(__file__), '..', 'votingpage.html'))

@app.route("/vote", methods=["POST"])
def vote():
    data = request.get_json()

    # The script.js sends "vote" directly as a string, not an encrypted object
    # So, we'll directly use the value from data.get("vote")
    plain_vote = data.get("vote") # Renamed for clarity since it's not encrypted from frontend
    
    if plain_vote:
        # We are not decrypting here because the frontend is sending plain text.
        # If you were to implement FHE in the frontend, you would call decrypt_vote here.
        # For the current setup, 'plain_vote' is already the candidate number.
        
        if plain_vote in votes:
            votes[plain_vote] += 1
            return jsonify({"message": "Vote counted successfully!"}), 200
        else:
            return jsonify({"message": "Invalid vote"}), 400
    return jsonify({"message": "No vote data provided"}), 400

@app.route("/result", methods=["GET"])
def result():
    return jsonify(votes)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)