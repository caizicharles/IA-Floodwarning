from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels

from floodsystem.station import inconsistent_typical_range_stations

def testing(stations):
    
    inconsistent_names = inconsistent_typical_range_stations(stations)
    station_names = set()

    test = set()

    for i in stations:
        for j in inconsistent_names:
            if i.name != j and i.typical_range != None and i.latest_level != None:
                station_names.add(i.name)
                test.add(MonitoringStation.relative_water_level(i))
                
        
    return test

def run():
    stations = build_station_list()
    update_water_levels(stations)
    station = testing(stations)
    #for n in station:
        #print(n[0], " ", n[1])

    print(station)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()