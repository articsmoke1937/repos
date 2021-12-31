import pandas
data = pandas.read_csv("https://covidtracking.com/api/v1/us/daily.csv")
states = list(data["states"])
#print(type(data))
#print(type(states))

for state in states:
    print(state)

