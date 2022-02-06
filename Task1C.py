
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def stations_within_radius(stations, centre, r):
    from haversine import haversine
    distance_from_position = []
    names_1 = []
    names_2 = []
    station_coordinates = []

    for i in stations:
        station_coordinates.append(i.coord)
        names_1.append(i.name)
        distance = haversine(i.coord, centre)
        distance_from_position.append(distance)

    for i in range(len(distance_from_position)):
        if distance_from_position[i] < r:
            names_2.append(names_1[i])
    
    names_2.sort()
    return names_2
  
    
stations_test = build_station_list()
print(stations_within_radius(stations_test, (52.2053, 0.1218) , 10))
