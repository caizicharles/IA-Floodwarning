from .station import inconsistent_typical_range_stations
from .station import MonitoringStation
from .utils import sorted_by_key    #Task 2C

"""Task 2B"""

def stations_level_over_threshold(stations, tol):
    
    inconsistent_names = inconsistent_typical_range_stations(stations)
    out = set()
    out_2 = []
    out_3 = []

    for i in stations:
        for j in inconsistent_names:
            if i.name != j and i.typical_range != None and i.latest_level != None:
                out.add((i.name, MonitoringStation.relative_water_level(i)))

    for k in out:
        out_2.append(k)

    for l in out_2:
        if l[1] >= tol:
            out_3.append(l)

    output = sorted_by_key(out_3, 1, reverse=True)
                
    return output

"""------------------------------------------"""

"""Task 2C"""

def stations_highest_rel_level(stations, N):

    inconsistent_names = inconsistent_typical_range_stations(stations)
    out = set()
    out_2 = []
    out_3 = []

    for i in stations:
        for j in inconsistent_names:
            if i.name != j and i.typical_range != None and i.latest_level != None:
                out.add((i.name, MonitoringStation.relative_water_level(i)))

    for k in out:
        out_2.append(k)

    out_3 = sorted_by_key(out_2, 1, reverse=True)

    output = [out_3[l] for l in range(0, N)]

    return output

"""------------------------------------------"""