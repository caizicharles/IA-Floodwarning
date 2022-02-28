from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import stations_highest_rel_level

def run():

    stations = build_station_list()
    update_water_levels(stations)
    station = stations_highest_rel_level(stations, 10)
    for n in station:
        print(n[0], " ", n[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()