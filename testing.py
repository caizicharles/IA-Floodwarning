from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.station import inconsistent_typical_range_stations

def testing(stations, tol):
    
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

def run():
    stations = build_station_list()
    update_water_levels(stations)
    station = testing(stations, 0.9)
    for n in station:
        print(n[0], " ", n[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()