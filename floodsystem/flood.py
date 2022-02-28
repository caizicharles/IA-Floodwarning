
from distutils.command.build import build

from sqlalchemy import false
from .stationdata import build_station_list
from .station import inconsistent_typical_range_stations
from .station import MonitoringStation

from .utils import sorted_by_key

"""Task 2B"""

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

"""------------------------------------------"""

"""Task 2C"""

def stations_highest_rel_level(stations, N):

    dif = []
    station_names = []
    combine = []
    output_0 = []
    output = []

    for station in stations:
        if station.typical_range and station.latest_level != None:
            a = station.typical_range
            b = (a[0] + a[1])/2
            c = station.latest_level - b
            
            if c >= 0:
                station_names.append(station.name)
                dif.append(c)

    combine = [(station_names[i], dif[i]) for i in range(0, len(station_names)) ]
        
    output_0 = sorted_by_key(combine, 1, reverse=True)

    output = [output_0[j] for j in range(0, N)]

    return output

"""------------------------------------------"""