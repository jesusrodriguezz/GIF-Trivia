//Created by Maria Barrera

document.addEventListener("DOMContentLoaded", function () {
  var sendButton = document.getElementById("send-button");
  sendButton.addEventListener("click", sendMessage);

  var userInput = document.getElementById("user-input");
  userInput.addEventListener("keydown", function (event) {
    if (event.keyCode === 13) {
      // Enter key
      sendMessage();
    }
  });

  var pointsNeeded = 3;
  var points = 0;
  var incorrectResponses = 0;
  var correctResponses = 0;
  var maxAttempts = 3;
  var username = "";
  var gifTitle = "";
  var gameFinished = false;
  var setName = false;

  async function renderGif() {
    const response = await fetch("/gif");
    const { url, title } = await response.json();
    var gifElement = document.createElement("img");
    gifElement.src = url;
    gifElement.alt = title;
    gifTitle = title;
    displayMessage(
      "based on the GIF, can you guess the name of the movie the character is from?",
      "bot"
    );
    displayMessage(gifElement, "bot");

    return title;
  }

  function sendMessage() {
    var message = userInput.value.trim();
    if (message == "") {
      return;
    }
    userInput.value = "";

    displayMessage(message, "user");

    if (setName) {
      username = message;
      setName = false;
      renderGif();
      return;
    }

    checkAnswer(message, gifTitle);
    if (gameFinished && message == "yes") {
      location.reload();
      return;
    }

    if (gameFinished && message == "no") {
      window.location.href = "/list";
      return;
    }

    if (gameFinished) {
      return;
    }

    renderGif();
  }

  function setUsername() {
    displayMessage("Enter name to play game", "bot");
    setName = true;
  }

  function checkAnswer(message, correctAnswer) {
    if (gameFinished) return;

    if (message == correctAnswer) {
      correctResponses++;
      points++;

      displayMessage("Nice, thats right! ", "bot");
      if (points == pointsNeeded) {
        gameFinished = true;
        sendFetchRequest(username, points, incorrectResponses, "WINNER");
        displayMessage(
          "That was fun!... do you wish to play again?(yes/no)",
          "bot"
        );
      }

      return;
    }

    displayMessage(
      "Sorry! wrong answer..! the answer was: " + correctAnswer,
      "bot"
    );

    incorrectResponses++;

    if (incorrectResponses == maxAttempts) {
      gameFinished = true;
      sendFetchRequest(username, points, incorrectResponses, "LOSER");
      displayMessage("You lose... do you wish to play again?(yes/no)", "bot");
    }

    return;
  }

  function sendFetchRequest(username, score, attempts, status) {
    var formData = new FormData();
    formData.append("username", username);
    formData.append("score", score);
    formData.append("attempts", attempts);
    formData.append("status", status);

    fetch("/score", {
      method: "POST",
      body: formData,
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        var botResponse = data.response;
        displayMessage(botResponse, "bot");
      })
      .catch(function (error) {
        console.log("Error:", error);
      });
  }

  function displayMessage(message, sender) {
    var chatMessages = document.getElementById("chat-messages");
    var messageElement = document.createElement("div");
    messageElement.classList.add("message", sender);

    if (typeof message === "string") {
      messageElement.textContent = message;
    } else {
      messageElement.appendChild(message);
    }

    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  displayMessage("Which GIF category would you like to start with?", "bot");
  displayMessage("Categories: movies", "bot");
  setUsername();
});
