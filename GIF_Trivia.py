import requests
import random

def init():
    print("Enter name to play game")
    name = input()
    print("***************************************")
    print("* Hello,", name, "Welcome to GIF-Trivia! *")
    print("**************************************")
    new_game(name)
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
        play_again = input("That was fun!... do you wish to play again?(y/n): ")
        if play_again == "y":
            new_game(player)
    return ''

def keep_scores(player_name, correcr_responses, total_questions):
    return ''

    

def display_gifs():

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
            print("**********************")
            print("* Nice, thats right! *")
            print("**********************")
            print()
            print("Next GIF will display...")
            print()
        else:
            print()
            print("*Sorry! wrong answer..", "the answer was:",choice_of_movie,"*")
            print()
    else:
        print("Error:", response.status_code)
    return ''

    

print(init())
