from .datafetcher import fetch_measure_levels
from .stationdata import build_station_list, update_water_levels
from .flood import stations_highest_rel_level
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.station import inconsistent_typical_range_stations
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

y = inconsistent_typical_range_stations(stations)
print(y)

update_water_levels(stations)

def plot_water_levels(station, dates, levels):
    typical_range_high = []
    typical_range_low = []
    for i in range(len(dates)):
        typical_range_high.append(typical_range[0])
        typical_range_low.append(typical_range[1])  
    
    
    plt.plot(dates , levels , label="water level")

    plt.xlabel("data")
    plt.ylabel("water level (m)")
    plt.xticks(rotation=45);
    plt.title(station)
    plt.tight_layout()
    
    plt.plot(dates , typical_range_high , "-b" , label="typical high")
    plt.plot(dates , typical_range_low , "-b" , label="typical low")
    
    plt.legend()
    plt.show()
counter = 0 
for i in stations:
    if i.name in stations_at_risk:
        dt = 10
        dates, levels = fetch_measure_levels(i.measure_id , dt = datetime.timedelta(days=dt))
        typical_range = i.typical_range
        plot_water_levels(i.name , dates , levels)
        counter = counter + 1
        if counter > 5:
            raise RuntimeError("All of the 5 stations have displayed the outputs")


def plot_water_level_with_fit(station, dates, levels, p): 
    x = dates
    y = levels
    p_coeff = np.polyfit(x , y , p)
    poly = np.poly1d(p_coeff)
    plt.plot(x , y , '.')
    plt.xlabel("time")
    plt.ylabel("water level")
    plt.xticks(rotation=45);
    plt.title(station)
    x1 = np.linspace(x[0] , x[-1] , 30)
    plt.plot(x1 , poly(x1))
    plt.show()
    return poly