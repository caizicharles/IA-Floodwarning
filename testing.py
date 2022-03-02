from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime
import numpy as np

x = build_station_list()
y = x[0]
dt = 2
dates, levels = fetch_measure_levels(y.measure_id , dt = datetime.timedelta(days = dt))
poly, d0 = polyfit(dates, levels, 4)
print(poly, d0)