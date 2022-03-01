from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np

def run():

    stations = build_station_list()
    update_water_levels(stations)
    name_ratio = stations_level_over_threshold(stations, 1)

    temp = set()


    for i in name_ratio:
        for j in stations:
            if i[0] == j.name and j.latest_level != None and j.typical_range != None:
                temp.add(j)

    for k in temp:
        dates, levels = fetch_measure_levels(k.measure_id , dt = 10)
        poly, d0 = polyfit(dates, levels, 4)

        temp = []
        for x in poly:
            temp.append(x)
        
        d = np.poly1d(temp)
        d.deriv()



'''if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()'''