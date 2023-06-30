
# Game of Trivia with Giphy API and SQLite Database

 
### Overview
Welcome to the Game of Trivia! This is an interactive trivia game where players have to guess the movie title based on a GIF obtained from the Giphy API. The game utilizes a SQLite database to store player scores and track their progress.

#### Features
- Randomly selects a movie GIF from a predefined list using the Giphy API.

- Displays the GIF to the player and prompts them to guess the movie title.

- Awards points to the player for correct guesses and displays a congratulatory message.

- Tracks failed attempts and provides feedback for incorrect guesses.

- Stores player scores in a SQLite database.

- Leaderboard functionality to display top scores from the database.

### Technologies Used
Python: The game is implemented in Python, leveraging various libraries and modules.

Giphy API: The Giphy API is used to fetch movie GIFs for the trivia game.

SQLite: The SQLite database is utilized to store and query player scores.

  

# Installation

Clone or download the trivia game repository from [https://github.com/jesusrodriguezz/GIF-Trivia].

Ensure you have a valid Giphy API Key. If you don't have one, you can obtain it from [https://developers.giphy.com/].

Open the gif.py file and replace the API_KEY variable with your Giphy API Key.

Dependencies :
```
pip install flask requests
```

Run the game from the command line using the following command:

`python3 GIF_trivia.py`
`flask run`