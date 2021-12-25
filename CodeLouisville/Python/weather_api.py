import requests
import json
api_key = "78ed65bbe878c5c5b37152e70a8ae591"
city = "Louisville"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()
# /* Prints Json file output */
print(json)

description = json.get("weather")[0].get("description")
tempmin = json.get("main").get("temp_min")
tempmax = json.get("main").get("temp_max")

print ("Today's forecast is", description)
print ("The temperature will be between ", tempmin, " and ", tempmax)
