from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance #B
from floodsystem.geo import stations_within_radius #C
from floodsystem.geo import rivers_with_station #D
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number #E
from floodsystem.station import inconsistent_typical_range_stations #F

"""Task 1B"""

def test_B():

    a = stations_by_distance(build_station_list(), (1,1))
    b = a[0]
    c = a[1]

    assert b[1] <= c[1]   #test if distances are sorted by key
    
    for i in a:
        assert isinstance(i[0], str) == True   #test if station names are in the first index

"""------------------------------------------"""

"""Task 1C"""

def test_stations_within_radius():
    
    x = stations_within_radius(build_station_list(), (52.2053, 0.1218) , 10)
    list_of_stations = ['Bin Brook', 
    'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton',
     'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
    
    assert list_of_stations == x
     #this is the list of the stations on moodle 

"""------------------------------------------"""

"""Task 1D"""

def test_D_1():

    a = rivers_with_station(build_station_list())
    
    assert len(a) == len(set(a))   #test for no repetition

    for j in a:
        assert type(j) == str   #test for correct input

def test_D_2():

    a = stations_by_river(build_station_list())
    b = a.keys()
    
    assert len(b) == len(set(b))   #test for no repetition

"""------------------------------------------"""

"""Task 1E"""

def test_E():

    a = rivers_by_station_number(build_station_list(), 9)

    assert len(a) == len(set(a))   #test for no repetition

"""------------------------------------------"""

"""Task 1F"""

def test_stations_with_inconsistent_data():

    stations = build_station_list()
    x = inconsistent_typical_range_stations(stations)
    stations_name = []
    typical_range_stations = []
    stations_with_incorrect_data = []
    
    for i in stations:
        stations_name.append(i.name)
        typical_range_stations.append(i.typical_range)
    
    for i in range(len(typical_range_stations)):
        if typical_range_stations[i] == None:
            stations_with_incorrect_data.append(stations_name[i])
        elif typical_range_stations[i][0] > typical_range_stations[i][1]:
            stations_with_incorrect_data.append(stations_name[i])
        stations_with_incorrect_data.sort()
    assert x == stations_with_incorrect_data


"""------------------------------------------"""