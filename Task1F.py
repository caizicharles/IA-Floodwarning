
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


stations = build_station_list()
x = inconsistent_typical_range_stations(stations)
print(x)


def stations_with_inconsistent_data