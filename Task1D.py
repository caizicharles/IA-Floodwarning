from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def execute_0():  #Number of rivers with at least one station and prints first 10
    
    #Variables
    stations = build_station_list()                       #Initialize list
    rivers = rivers_with_station(build_station_list())    #Calls function and stores values
    river_list0 = []                                      #List of UNSORTED river names
    river_list = []                                       #Final list of 10 SORTED river names
    x = 0                                                 #Number count when iterating through list to ch
    n = 0                                                 #Total number count

    #Check the number of times a river appeared in overall list
    for river in rivers:
        for station in stations:
            if river == station.river:
                x += 1
        #Increment n and stores river name
        if x >= 1:
            n += 1
            river_list0.append(river)
            x = 0

    #Sort river names in alphabetical order
    river_list0.sort()
    
    #Create final list with 10 river names
    for i in range(10):
        river_list.append(river_list0[i])
        
    return n, river_list

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