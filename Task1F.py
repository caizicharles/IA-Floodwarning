from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()
x = inconsistent_typical_range_stations(stations)
print(x)

#returns a list of stations with inconsistent data

def stations_with_inconsistent_data_test(x):
    list_of_stations = ['Airmyn', 'Blacktoft', 'Braunton', 'Brentford', 
    'Broomfleet Weighton Lock', 'East Hull Hedon Road', 'Eastbourne Harbour', 
    'Fleetwood', 'Goole', 'Hedon Thorn Road Bridge', 'Hedon Westlands Drain', 
    'Hempholme Pumping Station Roam Drain', 'Hull Barrier Victoria Pier', 
    'Hull High Flaggs, Lincoln Street', 'Littlehampton', 'Medmerry', 
    'North America', 'Paull', 'Salt End', 'Sandwich Quay', 
    'Sindlesham Mill', 'Stone Creek', 'Templers Road', 'Tickton Pumping Station', 
    'Topsham', 'Totnes', 'Truro Harbour', 'Wilfholme Pumping Station']
    assert x == list_of_stations
    #this is the updated list

stations_with_inconsistent_data_test(x)


