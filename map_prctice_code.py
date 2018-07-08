import folium
import pandas
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elv=list(data["ELEV"])
types=list(data["TYPE"])

def marker_color(elevation):
    if elevation <= 1000:
        return "green"
    elif elevation > 1000 and elevation <=3000:
        return "orange"
    else:
        return "red"
   
    

map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")

""" for adding a single marker

fg=folium.FeatureGroup(name="My Map")
#map.add_child(folium.Marker(location=[38.2,-99.1],popup="HI,I AM HERE",icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[38.2,-99.1],popup="HI,I AM HERE",icon=folium.Icon(color='green')))
map.add_child(fg)

"""
#for multiple markers you can add number of childs or we use for loop with coordinates in a list
#map.add_child(folium.Marker(location=[38.2,-99.1],popup="HI,I AM HERE",icon=folium.Icon(color='green')))
#map.add_child(folium.Marker(location=[39.2,-96.1],popup="HI,I AM HERE",icon=folium.Icon(color='green')))

"""
    coordinate_list=[[38.2,-99.1],[36.2,-95.1],[34.2,-97.1]]
fg=folium.FeatureGroup(name="My Map")
for coordinate in coordinate_list:
    fg.add_child(folium.Marker(location=coordinate,popup="HI,I AM HERE",icon=folium.Icon(color='green')))
    map.add_child(fg)
    """

fg=folium.FeatureGroup(name="My Map")
for lt,ln,el,typ in zip(lat,lon,elv,types):
    #fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m "+typ,icon=folium.Icon(color=marker_color(el))))
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=12,popup=str(el),fill_color=marker_color(el),color='red',fill_opacity=0.7))

 #fg.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig'))))
fg.add_child(folium.GeoJson(open("world.json",encoding = "utf-8-sig").read()))
map.add_child(fg)

map.save("map1.html")
