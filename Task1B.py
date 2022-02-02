from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def show():
    
    show_list0 = stations_by_distance(build_station_list(), (1, 2))
    show_list = []

    for items in range(0,10):
        show_list.append(show_list0[items])
    
    return show_list

print(show())