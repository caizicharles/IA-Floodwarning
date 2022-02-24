from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import stations_highest_rel_level

def run():

    stations = build_station_list()
    update_water_levels(stations)
    station = stations_highest_rel_level(stations, 20)

    return station

print(run())