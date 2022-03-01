
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels

from analysis import polyfit
                                                                                                     
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import timedelta
import datetime

stations = build_station_list()

def run():

    stations = build_station_list()
    update_water_levels(stations)
    station = stations_highest_rel_level(stations, 6)
    
    stations_high_risk_level = []
    for n in station:
        stations_high_risk_level.append(n[0])
    return stations_high_risk_level

stations_at_risk = run()
stations_at_risk.pop(0)


def plot_water_level_with_fit(station, dates, levels, p): 
    poly, d0 = polyfit(dates, levels, p)
    times = []
    
    x = matplotlib.dates.date2num(dates)
    shift = x[-1]
    times = x - shift
    
    typical_range_high = []
    typical_range_low = []
    

    for i in range(len(times)):
        typical_range_high.append(typical_range[1])
        typical_range_low.append(typical_range[0])

    plt.plot(times , levels , '.' , label="water level")
    plt.plot(times , typical_range_high , label="typical range high")
    plt.plot(times , typical_range_low , label="typical range low")
    plt.xlabel("time")
    plt.ylabel("water level")
    plt.xticks(rotation=45);
    
    plt.title(station)
    plt.plot(times , poly(times) , '.' , label="best fit function")
    plt.legend()
    
    plt.show()
    
for i in stations:
    if i.name in stations_at_risk:
        dt = 2
        dates , levels = fetch_measure_levels(i.measure_id , dt = datetime.timedelta(days = dt))
        typical_range = i.typical_range
        plot_water_level_with_fit(i.name , dates , levels , 4)
