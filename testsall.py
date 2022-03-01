"""                      Task 2B                          """


from floodsystem.stationdata import update_water_levels, build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()
update_water_levels(stations)


def stations_level_over_threshold(stations, tol = 0.8):
    station_names = []
    latest_level_stations = []
    typical_range_stations = []
    relative_ratio = []
    stations_exceeding_limit = []
    
    for i in stations:
        if i.typical_range != None:
            typical_range_stations.append(i.typical_range)
            station_names.append(i.name)
            latest_level_stations.append(i.latest_level)            
    
    inconsistent_typical_stations = inconsistent_typical_range_stations(stations)
    
    
    print(typical_range_stations[0][0])
    print(typical_range_stations[0][1])
    for i in range(len(station_names)):
        for j in inconsistent_typical_stations:
            if j == station_names[i]:
                latest_level_stations[i] = None
    
    for i in range(len(typical_range_stations)):
        a = typical_range_stations[i][0]
        b = typical_range_stations[i][1]
        x = (latest_level_stations[0] - a)/(b - a)
        relative_ratio.append(x)
    
    for i in range(len(latest_level_stations)):
        if latest_level_stations[i] == None:
            continue
        elif relative_ratio[i] > tol:
            x = station_names[i] , relative_ratio[i]
            stations_exceeding_limit.append(x)
    
    stations_exceeding_limit.sort(key=lambda x: x[1] , reverse=True)
    return stations_exceeding_limit

stations_above_limit = stations_level_over_threshold(stations , 0.8)

print(stations_above_limit)