import json

infile = open("eq_data_30_day_m1.json","r")
outfile = open("readable_eq_data.json","w")


eq_data = json.load(infile)
    #json.load() takes our json file and converts it into a Python object, and eq_data
    #   becomes a dictionary. We haven't fixed the format yet.

json.dump(eq_data, outfile, indent = 4)
    #To help us be in a more readable format
    #Three arguments: our object, the outfile, and how many indents we want in the file

list_of_eqs = eq_data["features"]
    #This will return the value of features, which is a list of earthquakes.


mags, lons, lats, hover_texts = [], [], [], []
    #You can create multiple lists in one line.

for eq in list_of_eqs:
    #eq is a dictionary; this goes through each element of the list, which is a dictionary
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    title = eq["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

print(mags[:10])
print(lons[:10])
print(lats[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [
    {"type":"scattergeo",       #Scattergeo is a type of plot, which is based on a world map.
    "lon":lons,             #These lists all have to have the same number of elements
    "lat":lats,             #"                          "
    "text":hover_texts,     #"                          "
    "marker": {
        "size":[5*mag for mag in mags],
        "color":mags,
        "colorscale":"Viridis",
        "reversescale":True,        #switches the colors to decreasing instead of increasing
        "colorbar":{"title":"Magnitude"},      #the title of the colorscale will be Magnitude
    },
    }]

#We can change the scale of the dots by using list comprehension. You could use a for loop to multiply
#   each element of the list by a number, but it's faster to use LC.

#Three parts to list comprehension:     [expression     iteration       condition]
#Iterate is like our for loop, the expression is our i*5 thing, and the condition is optional


my_layout = Layout(title = "Global Earthquakes")

fig = {'data':data, 'layout':my_layout}
    #We're creating a dictionary called fig, and we're giving it two keys: data and layout

offline.plot(fig, filename = "global_earthquakes.html")