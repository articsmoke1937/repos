from typing import Counter
import requests
import csv
from requests import api
api_key = "78ed65bbe878c5c5b37152e70a8ae591"
city = input("What City do you live in: ")
url = "https://api.chucknorris.io/jokes/random"
good_answer = [['N','n'], ['Y', 'y']]

cycle = 2
#for i in range(cycle):
print("Let's play a game: ")  
age = int(input("How old are you: ")) 
answer = input("Would you Like to hear a chuck Norris Joke? Y or N ")

for x in range(age):
    if answer in good_answer[0]:
        print("Well that's too damn bad")
        request = requests.get(url)
        json = request.json()
        joke = json.get("value")
        print(joke)
        answer = input("Would you Like to hear a chuck Norris Joke? Y or N ")
    elif answer in good_answer[1]:
        num=int(input("How many would you like to hear? "))
        for x in range(num):
            request = requests.get(url)
            json = request.json()
        # print(json)
            joke = json.get("value")
            print(joke)
        print("You have just been Norrished!")
        break
    else: 
        print("Since you can't follow directions, then you will see the weather forecast ")
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
        request = requests.get(url)
        json = request.json()
    # /* Prints Json file output */
       # print(json)

        description = json.get("weather")[0].get("description")
        tempmin = json.get("main").get("temp_min")
        tempmax = json.get("main").get("temp_max")

        print ("Today's forecast is", description)
        print ("The temperature in "+city+" will be between ", tempmin, " and ", tempmax)

        break
