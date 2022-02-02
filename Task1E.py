from floodsystem.stationdata import build_station_list

print('-----------------------\n-----------------------')

def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()
    rivers = []
    for station in stations:
        rivers.append(station.river)

    river = sorted(rivers)
    return river


print(run())