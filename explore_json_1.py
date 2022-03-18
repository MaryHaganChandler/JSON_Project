import json

infile = open("eq_data_1_day_m1.json","r")
outfile = open("readable_eq_data.json","w")


eq_data = json.load(infile)
    #json.load() takes our json file and converts it into a Python object, and eq_data
    #   becomes a dictionary. We haven't fixed the format yet.

json.dump(eq_data, outfile, indent = 4)
    #To help us be in a more readable format
    #Three arguments: our object, the outfile, and how many indents we want in the file

list_of_eqs = eq_data["features"]
    #This will return the value of features, which is a list of earthquakes.


mags, lons, lats = [], [], []
    #You can create multiple lists in one line.

for eq in list_of_eqs:
    #eq is a dictionary; this goes through each element of the list, which is a dictionary
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [Scattergeo(lon = lons,lat = lats)]
                   #This is the argument for the function Scattergeo

my_layout = Layout(title = "Global Earthquakes")

fig = {'data':data, 'layout':my_layout}
    #We're creating a dictionary called fig, and we're giving it two keys: data and layout

offline.plot(fig, filename = "global_earthquakes.html")