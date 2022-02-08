from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius #C
from floodsystem.station import inconsistent_typical_range_stations #F


"""Task 1C"""

stations_test = build_station_list()
x = stations_within_radius(stations_test, (52.2053, 0.1218) , 10)

def stations_within_radius_test(x):
    list_of_stations = ['Bin Brook', 
    'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton',
     'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
    assert list_of_stations == x
     #this is the list of the stations on moodle 
   
#stations_within_radius_test(x)

"""------------------------------------------"""

"""Task 1F"""

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

#stations_with_inconsistent_data_test(x)
