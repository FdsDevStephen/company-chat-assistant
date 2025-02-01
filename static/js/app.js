document.getElementById("chatForm").addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent page reload

    const userInput = document.getElementById("userInput").value;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").textContent = data.response;
        document.getElementById("userInput").value = ""; // Clear the input field
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("response").textContent = "There was an error processing your request.";
    });
});
