from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()
x = inconsistent_typical_range_stations(stations)
print(x)
#returns a list of stations with inconsistent data