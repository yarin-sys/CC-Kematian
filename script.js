document.getElementById('votingForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const selectedCandidate = document.querySelector('input[name="candidate"]:checked');
  const responseMessageDiv = document.getElementById('responseMessage');
  const encryptedVoteDisplayDiv = document.getElementById('encryptedVoteDisplay');

  if (selectedCandidate) {
    const vote = selectedCandidate.value;
    
    // Simulate encryption for display purposes
    // In a real FHE scenario, a client-side FHE library would encrypt the vote here.
    const simulatedEncryptedVote = btoa(vote); // Base64 encode for a visual 'encrypted' string

    encryptedVoteDisplayDiv.innerText = `Sending Encrypted Vote: ${simulatedEncryptedVote}`;
    responseMessageDiv.innerText = 'Submitting vote...';

    // Send the simulated encrypted vote to backend
    fetch('http://127.0.0.1:5000/vote', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      // Send the base64 encoded string. The backend will "decrypt" it using TenSEAL.
      body: JSON.stringify({ vote: simulatedEncryptedVote })
    })
    .then(response => response.json())
    .then(data => {
      responseMessageDiv.innerText = data.message;
      encryptedVoteDisplayDiv.innerText = ''; // Clear display after submission
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