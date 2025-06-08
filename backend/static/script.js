document.addEventListener("DOMContentLoaded", function () {
  const voteForm = document.getElementById("voteForm");
  const resultDiv = document.getElementById("result");
  const encryptedMessageDiv = document.getElementById("encryptedMessage");
  const showResultsButton = document.getElementById("showResults");

  voteForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const selectedCandidate = document.querySelector(
      'input[name="candidate"]:checked'
    );
    if (!selectedCandidate) {
      alert("Please select a candidate.");
      return;
    }

    const vote = selectedCandidate.value;

    // ✅ SIMULATED encryption: base64 encoding only
    const simulatedEncryptedVote = btoa(vote);

    fetch("/vote", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ encrypted_vote: simulatedEncryptedVote }),
    })
      .then((response) => {
        if (!response.ok) {
          return response.json().then((data) => {
            throw new Error(data.message || "Error processing vote.");
          });
        }
        return response.json();
      })
      .then((data) => {
        encryptedMessageDiv.textContent =
          "Encrypted Vote (simulated): " + simulatedEncryptedVote;
        resultDiv.textContent = data.message;
      })
      .catch((error) => {
        resultDiv.textContent = error.message;
      });
  });

  showResultsButton.addEventListener("click", function () {
    fetch("/results")
      .then((response) => response.json())
      .then((data) => {
        resultDiv.innerHTML = `
          <strong>Current Tally:</strong><br>
          Candidate A: ${data["Candidate A"]} votes<br>
          Candidate B: ${data["Candidate B"]} votes
        `;
      });
  });
});
