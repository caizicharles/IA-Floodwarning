from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():

    stations = build_station_list()
    update_water_levels(stations)
    station = stations_level_over_threshold(stations, 0.9)
    '''for n in station:
        print(n[0], " ", n[1])'''
    print(station)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()