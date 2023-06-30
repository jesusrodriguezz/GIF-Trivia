#Created by Jesus Rodriguez

import random
import requests


def getGif():
    #list_of_movies = ["BeetleJuice", "Edward ScissorHands", "IronMan", "Charlie and the Chocolate Factory"]
    list_of_movies = ["Phantom Of Music", "Tick Tick Boom", "Iron Man", "The Greatest Showman"]
    choice_of_movie = random.choice(list_of_movies)

    API_KEY = 'K6YniUbHKX81UPXHjkdbz5YTWgeCX7ab'

    url = f"https://api.giphy.com/v1/gifs/search?api_key={API_KEY}&q={choice_of_movie}&limit=5"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        gifs = data["data"]
        random_gif = random.choice(gifs)
        return random_gif["images"]["fixed_height_downsampled"]["url"], choice_of_movie

    return "", choice_of_movie
