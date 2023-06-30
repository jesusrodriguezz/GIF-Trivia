import requests
import random
import sqlite3
from migration import create_table, drop_all_tables
drop_all_tables()
create_table()

points = 0
attempts = 0

def printTable(rows):
    headers = ["ID", "Username", "Score", "Attempts", "Status"]
    print()
    print("-" * 60)
    print()
    for header in headers:
        print(f"{header:10s}", end=" ")
    print()

    print("-" * 60)

    for row in rows:
        row_id = row["rowid"]
        username = row["username"]
        score = row["score"]
        attempts = row["attempts"]
        status = row["status"]

        print(f"{row_id:<10d}", end=" ")
        print(f"{username:10s}", end=" ")
        print(f"{score:<10d}", end=" ")
        print(f"{attempts:<10d}", end=" ")
        print(f"{status:10s}")

    print() 



def listScores():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM score")

    rows = cur.fetchall()
    con.close()
    return rows

def insertScore(username, score, attempts, status):
    try:
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO score (username, score, attempts, status) VALUES (?,?,?,?)",
                (username, score, attempts, status))
            con.commit()

            return "Score added successfully"
    except Exception as e:
            print("An error occurred:", str(e))
            return "Error adding score"

def init():
    while True:
        print("***************************************")
        print("*               MENU                  *")
        print("***************************************")
        print("* Options:                            *")
        print("* 1) List Scores                      *")
        print("* 2) Play                             *")
        print("* 3) Exit                             *")
        print("***************************************")
        option = input("Select an option (1-3): ")

        if option == "1":
            scores = listScores()
            print("\nSCORES\n")
            printTable(scores)
        elif option == "2":
            name = input("\nEnter your name: ")
            print("\n***************************************")
            print("* Hello,", name + "! Welcome to GIF-Trivia! *")
            print("***************************************")
            new_game(name)
        elif option == "3":
            print("\nExiting...")
            break
        else:
            print("\nInvalid option. Please try again.\n")
    return ''

def new_game(player):
    print()
    print("Let's play the game.")
    print("Which GIF category would you like to start with?")
    print("Categories: movies")
    category = input()
    if category == "movies":
        print()
        print("Guess the name of the movie based on the GIF")
        print()
        for _ in range(2):
            display_gifs()
        
        print("game over!")
        print()
        insertScore(player, points, attempts, "WINNER" if points > attempts else "LOSER")
        play_again = input("That was fun!... do you wish to play again?(y/n): ")
        if play_again == "y":
            new_game(player)
    return ''

def keep_scores(player_name, correcr_responses, total_questions):
    return ''

    

def display_gifs():
    global points, attempts
    list_of_movies = ["BeetleJuice", "Edward ScissorHands", "IronMan", "Charlie and the Chocolate Factory"]
    choice_of_movie = random.choice(list_of_movies)

    API_KEY = 'K6YniUbHKX81UPXHjkdbz5YTWgeCX7ab'
    
    
    url =f"https://api.giphy.com/v1/gifs/search?api_key={API_KEY}&q={choice_of_movie}&limit=5"
    #print(choice_of_movie)
    response = requests.get(url)
    if response.status_code == 200:
        
        data = response.json()
        gifs = data["data"]
        random_gif = random.choice(gifs)

        gif_url = random_gif["images"]["fixed_height_downsampled"]["url"]
        
        print("GIF URL:", gif_url)
        print()
        
        print("*based on the GIF, can you guess the name of the movie the character is from?*")
        print()
        
        print("type down your answer:", list_of_movies)
        answer = input()
        
        if answer == choice_of_movie:
            points += 1
            print("**********************")
            print("* Nice, thats right! *")
            print("**********************")
            print()
            print("Next GIF will display...")
            print()
        else:
            attempts += 1
            print()
            print("*Sorry! wrong answer..", "the answer was:",choice_of_movie,"*")
            print()
    else:
        print("Error:", response.status_code)
    return ''

    

print(init())
