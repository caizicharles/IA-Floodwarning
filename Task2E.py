from sre_constants import SRE_FLAG_UNICODE
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.station import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels


import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import datetime

stations = build_station_list()

def run():

    stations = build_station_list()
    update_water_levels(stations)
    station = stations_highest_rel_level(stations, 5)
    stations_high_risk_level = []
    for n in station:
        stations_high_risk_level.append(n[0])
    return stations_high_risk_level

stations_at_risk = run()
print(stations_at_risk)


for i in stations:
    if i.name == "Letcombe Bassett":
        dt = 5
        dates, levels = fetch_measure_levels(i.measure_id , dt = datetime.timedelta(days=dt))
        
    
print(dates, levels)










"""print(stations)    

def plot_water_levels(stations, dates, levels):
    typical_range_stations = []
    typical_range_high = []
    typical_range_low = []
    
    for i in stations:
        for j in stations_at_risk:
            if j == i.name:
                typical_range_stations.append(i.typical_range)
    
    
    
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
    
    plt.show()"""


 