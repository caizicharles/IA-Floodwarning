
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def stations_within_radius(stations, centre, r):
    distance_from_position = []
    names = []
    station_coordinates = []
    station_x_coordinate = []
    station_y_coordinate = []
    for i in stations:
        station_coordinates.append(i.coord)
        names.append(i.name)

    for i in range(len(station_coordinates)):
        station_x_coordinate.append(station_coordinates[i][0])
    
    for i in range(len(station_coordinates)):
        station_y_coordinate.append(station_coordinates[i][1])


    for i in range(len(station_coordinates)):
        a = station_x_coordinate[i]
        b = station_y_coordinate[i]
        distance = ((a - centre[0])**2 + b**2)**0.5
        distance_from_position.append(distance)
    
    print(distance_from_position)

    for i in range(len(distance_from_position) - 1):
        if distance_from_position[i] > r:
            names.remove(i)
        else:
            continue
    return len(names)
    
    

print(stations_within_radius(build_station_list(), (52.2053, 0.1218) , 10))
