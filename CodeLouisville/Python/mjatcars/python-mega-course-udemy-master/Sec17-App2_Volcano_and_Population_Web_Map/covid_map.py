import folium
import pandas
import json

data = pandas.read_csv("https://covidtracking.com/api/v1/states/daily.csv")
state= list(data["state"])
death= list(data["death"])
state_death = dict(zip(state,death))

datag = pandas.read_csv("state_geo.csv")
stateg= list(datag["state"])
lat= list(datag["lat"])
long= list(datag["long"])
state_lat = dict(zip(stateg,lat))
state_long = dict(zip(st

# Color volcano markers based on elevation
def color_producer(det):
    if det < 1000:
        return 'green'
    elif dt >1000 and det < 3000:
        return 'orange'
    else:
        return 'red'

# Color volcano markers based on elevation
def circle_size(detb):
    if detb < 1000:
        return 4
    elif detb >1000 and dt < 3000:
        return 6
    else:
        return 12

# Feature Group for covid layer
data = pandas.read_csv("https://covidtracking.com/api/v1/us/daily.csv")
map = folium.Map(location=[41.857943, -87.633145], zoom_start=4)  #, tiles="Stamen Toner")
fgc = folium.FeatureGroup(name="covid")
for st,dt in (state,death):
    fgc.add_child(folium.CircleMarker(radius=6,location=[state_lat[st], state_lat[st]], popup="deaths "+str(dt), fill_color=color_producer(el), coloer='grey',fill_opacity=0.7))

map.add_child(fgc)
map.add_child(folium.LayerControl()) # This creates a control switching each layer on and off separately
map.save("covid_map.html")

