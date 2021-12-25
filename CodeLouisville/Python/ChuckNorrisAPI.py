import requests
import csv
from requests import api
api_key = "R4OXOFNFJW9ZGXJR"
city = "Louisville"
url = "https://api.chucknorris.io/jokes/random"


answer = input("Would you Like to hear a chuck Norris Joke? Y or N")
if answer == 'N':
        print("Well that's too damn bad")
        request = requests.get(url)
        json = request.json()
        print(json)
elif answer == 'Y':
        print("Ya damn skippy")
        request = requests.get(url)
        json = request.json()
        print(json)
else: 
    print("Answer the damn question right now")


