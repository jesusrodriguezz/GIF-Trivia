# Created by Jesus Rodriguez
import requests
def init():
    print("Enter name")
    name = input()
    print("Hello:", name, "Welcome to GIF-Trivia!")
    
    new_game(name)
    return ''

def new_game(player):
    print("Let's play the game.")
    print("Which GIF category would you like to start with?")
    print("Categories: movies")
    category = input()
    if category == "movies":
        print("this where the api will get GIFS from category movies")
        display_gifs()
        pass
    return ''

def keep_scores(player_input):
    return ''

def display_gifs():
    API_KEY = 'K6YniUbHKX81UPXHjkdbz5YTWgeCX7ab'
    category_key = 'movies'
    url = f"https://api.giphy.com/v1/gifs/random?api_key={API_KEY}&tag={category_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        gif_url = data["data"]["images"]["fixed_height_downsampled"]["url"]
        print("GIF URL:", gif_url)
    else:
        print("Error:", response.status_code)
    return ''
print(init())
