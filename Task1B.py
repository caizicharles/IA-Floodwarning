from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def show():
    
    #Variables
    show_list0 = stations_by_distance(build_station_list(), (0, 0))  #Calls function that calculates distance
    show_list = []                                                   #Final list of tuples of 10 names and distances

    #Create list of tuples with 10 items
    for items in range(0,10):
        show_list.append(show_list0[items])
    
    return show_list

print(show())