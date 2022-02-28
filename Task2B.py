from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
"""update_water_levels(stations)
stations_above_limit = stations_level_over_threshold(stations , 0.8)

print(stations_above_limit)"""

y = MonitoringStation.relative_water_level(stations)

print(y)