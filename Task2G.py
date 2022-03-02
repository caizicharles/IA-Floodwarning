from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def warning():

    stations = build_station_list()
    update_water_levels(stations)
    name_ratio = stations_level_over_threshold(stations, 1)
    t = 10

    station_name = []
    station_data = set()
    station_list = []
    value = []
    severity = []
    output = []
    
    for i in name_ratio:
        for j in stations:
            if i[0] == j.name and j.latest_level != None and j.typical_range != None and j.measure_id != None:
                station_data.add(j)

    for x in station_data:
        if x.name == "Bissoe" or x.name == "Letcombe Bassett":
            continue
        else:
            station_list.append(x)

    for k in station_list:
        station_name.append(k.name)
        dates, levels = fetch_measure_levels(k.measure_id , dt = timedelta(days = t))
        poly, d0 = polyfit(dates, levels, 4)
        derivative = np.polyder(poly)
        value.append(derivative(9))

    for gradient in value:
        if gradient < 0.1:
            severity.append("Low")
        elif gradient >= 0.1 and gradient < 0.2:
            severity.append("Moderate")
        elif gradient >= 0.2 and gradient < 0.3:
            severity.append("High")
        else:
            severity.append("Severe")

    for y in range(0, len(severity)):
        output.append((station_name[y], severity[y]))
    
    print(output)



if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    warning()