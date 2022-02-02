from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def execute_0():
    
    stations = build_station_list()
    rivers = rivers_with_station(build_station_list())
    river_list0 = []
    river_list = []
    x = 0
    n = 0

    for river in rivers:
        for station in stations:
            if river == station.river:
                x += 1
        if x >= 1:
            n += 1
            river_list0.append(river)
            x = 0

    river_list0.sort()
    
    for i in range(10):
        river_list.append(river_list0[i])
        
    return n, river_list

print(execute_0())

"""------------------------------------------"""

def execute_1():
    
    dict = stations_by_river(build_station_list())

    river_1 = list(dict.get('River Aire'))
    river_1.sort()

    river_2 = list(dict.get('River Cam'))
    river_2.sort()

    river_3 = list(dict.get('River Thames'))
    river_3.sort()

    return river_1, river_2, river_3

print(execute_1())