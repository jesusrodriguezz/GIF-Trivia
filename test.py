#Created by Jesus Rodriguez
import requests
import json


API_KEY = 'K6YniUbHKX81UPXHjkdbz5YTWgeCX7ab'
url = 'https://api.giphy.com/v1/gifs/trending'
params = {
    'api_key': API_KEY,
    'limit': 1
}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    gif_urls = [gif['images']['original']['url'] for gif in data['data']]

    print(gif_urls)
else:
    print("Error occurred:", response.status_code)


