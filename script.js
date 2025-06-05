document.getElementById('votingForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const selectedCandidate = document.querySelector('input[name="candidate"]:checked');
  
  if (selectedCandidate) {
    const vote = selectedCandidate.value;
    
    // Send encrypted vote to backend (No need for encryption in frontend)
    fetch('http://127.0.0.1:5000/vote', {  // Use the correct backend URL for WSL
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ vote: vote })  // Send the vote directly to the backend
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('responseMessage').innerText = 'Vote submitted successfully!';
    })
    .catch(error => {
      document.getElementById('responseMessage').innerText = 'Error submitting vote. Please try again.';
    });
  } else {
    alert('Please select a candidate before submitting.');
  }
});
