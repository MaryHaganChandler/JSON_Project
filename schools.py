"""
Process the JSON file named univ.json. Create 3 maps per instructions
below.
The size of the point on the map should be based on the size
of total enrollment.
Display only those schools that are part of the
ACC, Big 12, Big Ten, Pac-12 and SEC divisons (refer to valueLabels.csv
file).
The school name and the specific map criteria should be
displayed when you hover over it. (For example for Map 1, when you
hover over Baylor, it should display "Baylor University, 81%".)

Choose appropriate tiles for each map.

Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African
       American over 10%
Map 3) Total price for in-state students living off campus over $50,000


ACC, Big 12, Big Ten, Pac-12 and SEC divisons: Division Numbers
102,    108,     107,    127,             130

"""


import json

univ_file = open("univ.json","r")

univ_data = json.load(univ_file)
    #univ_data is a LIST

list_of_univs, lons, lats = [], [], []
grad_rate_women, black_aa_enroll, total_price_instate = [], [], []

relevant_conferences = [102,107,108,127,180]

list_length = len(univ_data)


map_1_index = 0
while map_1_index < list_length:
    if univ_data[map_1_index]["NCAA"]["NAIA conference number football (IC2020)"] in relevant_conferences:
        univs = univ_data[map_1_index]["instnm"]
        lon = univ_data[map_1_index]["Longitude location of institution (HD2020)"]
        lat = univ_data[map_1_index]["Latitude location of institution (HD2020)"]
        grad = univ_data[map_1_index]["Graduation rate  women (DRVGR2020)"]

        list_of_univs.append(univs)
        lons.append(lon)
        lats.append(lat)
        grad_rate_women.append(grad)

    map_1_index += 1

print(list_of_univs)
print(lons)
print()
print(lats)
print(grad_rate_women)



from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

map_1_data = [
    {"type":"scattergeo",
    "lon":lons,
    "lat":lats,
    "text":list_of_univs,
    "marker": {
        #"size":
        #"color":
        "colorscale":"Viridis",
        "reversescale":True,
        "colorbar":{"title":"Percentage"},
    },
    }]


map_1_layout = Layout(title = "Graduation Rate for Women - Above 50%")

fig = {"data":map_1_data, "layout": map_1_layout}


offline.plot(fig, filename = "Graduation_Rate_For_Women.html")