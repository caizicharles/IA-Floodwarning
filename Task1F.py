from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
import test_geo

stations = build_station_list()
x = inconsistent_typical_range_stations(stations)
print(x)
y = test_geo.test_stations_with_inconsistent_data()
print(y)
