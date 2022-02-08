from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def show():
    
    #Variables
    stations = build_station_list()
    show_list_0 = stations_by_distance(stations, (0, 0))  #Calls function that calculates distance
    show_list_closest_0 = []                                          #List of tuples of 10 names and closest distances
    closest = []                                                      #10 closest by station, town, distance
    show_list_furthest_0 = []                                         #List of tuples of 10 names and furthest distances
    furthest = []                                                     #10 furthest by station, town, distance

    #Create list of tuples with 10 closest items
    for items in range(0,10):
        show_list_closest_0.append(show_list_0[items])

    #Create list of tuples with 10 furthest items
    for objects in range(len(show_list_0)-10, len(show_list_0)):
        show_list_furthest_0.append(show_list_0[objects])

    #add in closest town names
    for i in show_list_closest_0:
        temp = []
        for x in stations:
            if x.name == i[0]:
                temp.append((i[0], x.town, i[1]))
                closest.append(temp[0])
    
    #Add in furthest town names
    for j in show_list_furthest_0:
        temp_0 = []
        for x in stations:
            if x.name == j[0]:
                temp_0.append((j[0], x.town, j[1]))
                furthest.append(temp_0[0])

    return furthest

print(show())