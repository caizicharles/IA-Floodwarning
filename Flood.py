
from distutils.command.build import build

from sqlalchemy import false
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol = 0.8):
    station_names = []
    latest_level_stations = []
    stations_exceeding_limit = []
    
    for i in stations:
        station_names.append(i.name)
        latest_level_stations.append(i.latest_level)            
    inconsistent_typical_stations = inconsistent_typical_range_stations(stations)
    for i in range(len(station_names)):
        for j in inconsistent_typical_stations:
            if j == station_names[i]:
                latest_level_stations[i] = None
    
    for i in range(len(latest_level_stations)):
        if latest_level_stations[i] == None:
            continue
        elif latest_level_stations[i] > tol:
            x = (station_names[i] , latest_level_stations[i])
            stations_exceeding_limit.append(x)
    
    stations_exceeding_limit.sort(key=lambda x: x[1] , reverse=True)
    return stations_exceeding_limit
