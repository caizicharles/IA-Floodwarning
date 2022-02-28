
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.station import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from Plot import plot_water_levels

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import datetime


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
stations = build_station_list()
update_water_levels(stations)




 