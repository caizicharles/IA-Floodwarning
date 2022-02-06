
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
    
stations_test = build_station_list()
print(stations_within_radius(stations_test, (52.2053, 0.1218) , 10))
