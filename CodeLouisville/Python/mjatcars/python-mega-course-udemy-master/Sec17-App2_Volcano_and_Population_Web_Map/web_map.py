'''-------------------------------------------------------------------------------------------
DESCRIPTION: 
Use Folium to generate ana three layered html map with markers for Volcanoes in USA and outlined 
of countries with fill colored denoting population size.

HOW TO USE:
EXECUTE: python wev_map.py WHICH CREATES: web_map.html
LAUNCH: web_map.html
FEATURES:
- Country fill colors denote population size
  - green=<1,000,000
  - orange between 1,000,000 and 2,000,000
  - red>23,000,000
-Colored Circle Markers for Volcanoes in USA
  - green=<1,000 feet
  - orange between 1,000 and 3,000 feet
  - red>3,000 feet
LAYER CONTROL:
- There is a layer control in the upper right corner that allows you to toggle each layer
  on/off individually  
-------------------------------------------------------------------------------------------'''
import folium
import pandas
import json

data = pandas.read_csv("Volcanoes.txt") # CSV containing lat, long, elevation
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# Color volcano markers based on elevation
def color_producer(e):
    if e < 1000:
        return 'green'
    elif e >1000 and e < 3000:
        return 'orange'
    else:
        return 'red'

# Feature Group for volcano layer
data = pandas.read_csv("Volcanoes.txt")
map = folium.Map(location=[41.857943, -87.633145], zoom_start=4)  #, tiles="Stamen Toner")
fgv = folium.FeatureGroup(name="volcano")
for lt, ln, el in zip(lat, lon, elev): # process lat, lon and elev columns together
    fgv.add_child(folium.CircleMarker(radius=6,location=[lt, ln], popup=str(el)+" m", fill_color=color_producer(el), coloer='grey',fill_opacity=0.7))

#Feature Group for Population layer
fgp = folium.FeatureGroup(name="population")
json_data = json.load(open("world.json", encoding="utf-8-sig"))
fgp.add_child(folium.GeoJson(json_data, 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<1000000 
else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl()) # This creates a control switching each layer on and off separately
map.save("web_map.html")
