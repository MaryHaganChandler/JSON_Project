"""
Process the JSON file named univ.json. Create 3 maps per instructions
below.
The size of the point on the map should be based on the size
of total enrollment.
^^^^^^^^^^^^^^^^^^^^^^^DO THIS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^DO THIS
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

list_of_univs1, lons1, lats1 = [], [], []
list_of_univs2, lons2, lats2 = [], [], []
list_of_univs3, lons3, lats3 = [], [], []
grad_rate_women, black_aa_enroll, total_price_instate = [], [], []

relevant_conferences = [102,107,108,127,180]

list_length = len(univ_data)


map_1_index = 0
map_2_index = 0
map_3_index = 0

while map_1_index < list_length:
    if univ_data[map_1_index]["NCAA"]["NAIA conference number football (IC2020)"] in relevant_conferences:
        if univ_data[map_1_index]["Graduation rate  women (DRVGR2020)"] > 50:
            univs = univ_data[map_1_index]["instnm"]
            lon = univ_data[map_1_index]["Longitude location of institution (HD2020)"]
            lat = univ_data[map_1_index]["Latitude location of institution (HD2020)"]
            grad = univ_data[map_1_index]["Graduation rate  women (DRVGR2020)"]

            list_of_univs1.append(univs)
            lons1.append(lon)
            lats1.append(lat)
            grad_rate_women.append(grad)

        if univ_data[map_2_index]["Percent of total enrollment that are Black or African American (DRVEF2020)"] > 10:
            #print(type(univ_data[map_2_index]["Percent of total enrollment that are Black or African American (DRVEF2020)"]))
            univs = univ_data[map_2_index]["instnm"]
            lon = univ_data[map_2_index]["Longitude location of institution (HD2020)"]
            lat = univ_data[map_2_index]["Latitude location of institution (HD2020)"]
            enroll = univ_data[map_2_index]["Percent of total enrollment that are Black or African American (DRVEF2020)"]

            list_of_univs2.append(univs)
            lons2.append(lon)
            lats2.append(lat)
            black_aa_enroll.append(enroll)
        """
        if univ_data[map_3_index]["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"] > 50000:
            univs = univ_data[map_3_index]["instnm"]
            print(univs)
            
            lon = univ_data[map_3_index]["Longitude location of institution (HD2020)"]
            lat = univ_data[map_3_index]["Latitude location of institution (HD2020)"]
            price = univ_data[map_3_index]["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]

            list_of_univs3.append(univs)
            lons3.append(lon)
            lats3.append(lat)
            total_price_instate.append(price)
        """
    map_1_index += 1
    map_2_index += 1
    map_3_index += 1


#print(list_of_univs)
#print(lons)
#print()
#print(lats)
#print(grad_rate_women)
#print(list_of_univs1)
#print()
#print(list_of_univs2)
#print(black_aa_enroll)
#print(total_price_instate)




from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


"""--------MAP 1--------"""
map_1_data = [
    {"type":"scattergeo",
    "lon":lons1,
    "lat":lats1,
    "text":list_of_univs1,
    "marker": {
        "size":[0.2*grad for grad in grad_rate_women],
        "color":grad_rate_women,
        "colorscale":"viridis",
        "colorbar":{"title":"Percentage"},
    },
    }]

map_1_layout = Layout(title = "Graduation Rate for Women - Above 50%")

fig = {"data":map_1_data, "layout": map_1_layout}

offline.plot(fig, filename = "Graduation_Rate_For_Women.html")





"""--------MAP 2--------"""
map_2_data = [
    {"type":"scattergeo",
    "lon":lons2,
    "lat":lats2,
    "text":list_of_univs2,
    "marker": {
        "size":[2*enroll for enroll in black_aa_enroll],
        "color":black_aa_enroll,
        "colorscale":"magenta",
        "colorbar":{"title":"Percentage of Total Enrollment"},
    },
    }]

map_2_layout = Layout(title = "Black and African American Enrollment - Above 10%")

fig = {"data":map_2_data, "layout": map_2_layout}

offline.plot(fig, filename = "Black_And_African_American_Enrollment.html")






"""--------MAP 3--------"""
map_3_data = [
    {"type":"scattergeo",
    "lon":lons3,
    "lat":lats3,
    "text":list_of_univs3,
    "marker": {
        "size":[1*price for price in total_price_instate],
        "color":total_price_instate,
        "colorscale":"magenta",
        "colorbar":{"title":"Cost of Living"},
    },
    }]

map_3_layout = Layout(title = "In-State, Off-Campus Student Cost of Living - Above $50,000")

fig = {"data":map_3_data, "layout": map_3_layout}

offline.plot(fig, filename = "Off_Campus_Price_Above_50000.html")