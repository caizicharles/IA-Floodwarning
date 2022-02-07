
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
    
stations_test = build_station_list()
x = stations_within_radius(stations_test, (52.2053, 0.1218) , 10)
#x is a list of all stations within 10km range

def stations_within_radius_test(x):
    list_of_stations = ['Bin Brook', 
    'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton',
     'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
    assert list_of_stations == x
     #this is the list of the stations on moodle    
stations_within_radius_test(x)

