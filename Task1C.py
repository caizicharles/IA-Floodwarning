from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

stations = build_station_list()
x = stations_within_radius(stations, (52.2053, 0.1218) , 10)

#x is a list of all stations within 10km range
print(x)