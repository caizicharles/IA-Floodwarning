from sre_constants import SRE_FLAG_UNICODE
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

import datetime


stations = build_station_list()

for i in stations:
    if i.name == "Bourton Dickler":
        dt = 0.75
        dates, levels = fetch_measure_levels(i.measure_id , dt = datetime.timedelta(days=dt))
        typical_range = i.typical_range
print(levels)

def plot_water_levels(stations, dates, levels):
    typical_range_high = []
    typical_range_low = []
    for i in range(len(dates)):
        typical_range_high.append(typical_range[0])
        typical_range_low.append(typical_range[1])  
    
    
    plt.plot(dates , levels)

    plt.xlabel("data")
    plt.ylabel("water level (m)")
    plt.xticks(rotation=45);
    plt.title("Bourton Dickler")
    plt.tight_layout()
    
    plt.plot(dates , typical_range_high)
    plt.plot(dates , typical_range_low)
    
    plt.show()

plot_water_levels(stations , dates , levels)