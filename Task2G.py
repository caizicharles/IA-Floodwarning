from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels

def run():

    stations = build_station_list()
    update_water_levels(stations)
    name_ratio = stations_level_over_threshold(stations, 1.3)
    dates, levels = fetch_measure_levels(i.measure_id , dt = 10)
    poly, d0 = polyfit(dates, levels, 4)




'''if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()'''