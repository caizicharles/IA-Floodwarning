from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def execute_0():  #Number of rivers with at least one station and prints first 10
    
    #Variables
    rivers = list(rivers_with_station(build_station_list()))    #Calls function and stores values as a list
    river_list = []                                             #Final list of 10 SORTED river names

    #Sort river names in alphabetical order
    rivers.sort()
    
    #Create final list with 10 river names
    for i in range(10):
        river_list.append(rivers[i])
        
    return len(rivers), river_list

#print(execute_0())

"""------------------------------------------"""

def execute_1():  #Prints the names of stations on given rivers
    
    dict = stations_by_river(build_station_list())
    
    #River 1
    river_1 = list(dict.get('River Aire'))
    river_1.sort()   #Sort in alphabetical order
    
    #River 2
    river_2 = list(dict.get('River Cam'))
    river_2.sort()   #Sort in alphabetical order

    #River 3
    river_3 = list(dict.get('River Thames'))
    river_3.sort()   #Sort in alphabetical order

    return river_1, river_2, river_3

#print(execute_1())