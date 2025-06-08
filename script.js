window.onload = function () {
  const votingForm = document.getElementById('votingForm');
  const responseMessageDiv = document.getElementById('responseMessage');
  const encryptedVoteDisplayDiv = document.getElementById('encryptedVoteDisplay');
  const viewResultButton = document.getElementById('viewResultButton');

  votingForm.addEventListener('submit', function (event) {
    event.preventDefault();

    const selectedCandidate = document.querySelector('input[name="candidate"]:checked');

    if (selectedCandidate) {
      const vote = selectedCandidate.value;

      // Simulate encryption using base64
      const simulatedEncryptedVote = btoa(vote);
      encryptedVoteDisplayDiv.innerText = `Sending Encrypted Vote (simulated): ${simulatedEncryptedVote}`;
      responseMessageDiv.innerText = 'Submitting vote...';

      fetch('http://127.0.0.1:5000/vote', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ vote: simulatedEncryptedVote })
      })
        .then(response => response.json())
        .then(data => {
          responseMessageDiv.innerText = data.message;
          if (data.tenseal_encrypted_hex) {
            encryptedVoteDisplayDiv.innerText = `Stored Encrypted (CKKS): ${data.tenseal_encrypted_hex}`;
          } else {
            encryptedVoteDisplayDiv.innerText = '';
          }
        })
        .catch(error => {
          console.error('Error:', error);
          responseMessageDiv.innerText = 'Error submitting vote. Please try again.';
          encryptedVoteDisplayDiv.innerText = '';
        });
    } else {
      alert('Please select a candidate before submitting.');
      encryptedVoteDisplayDiv.innerText = '';
      responseMessageDiv.innerText = '';
    }
  });

  viewResultButton.addEventListener('click', function () {
    fetch('http://127.0.0.1:5000/result')
      .then(res => res.json())
      .then(data => {
        document.getElementById('voteResult').innerText =
          `Candidate A: ${data["1"]}, Candidate B: ${data["2"]}`;
      });
  });
};
