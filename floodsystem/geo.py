# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

"""Task 1B"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    
    #Variables
    s_n_dis = []         #Final list of tuples with names and distances to p
    s_name = []          #List of station names
    s_dis = []           #List of distances
    
    for location in stations:
        s_name.append(location.name)                 #Get station names
        s_dis.append(haversine(location.coord, p))   #Calculate distances

    #Create the list of tuples
    for i in range(len((s_name))):
        s_n_dis.append((s_name[i], s_dis[i]))

    return sorted_by_key(s_n_dis, 1)

"""------------------------------------------"""

"""Task 1C"""

def stations_within_radius(stations, centre, r):
    from haversine import haversine
    distance_from_position = []
    names_1 = []
    names_2 = []
    station_coordinates = []

    for i in stations:
        station_coordinates.append(i.coord)
        names_1.append(i.name)
        distance = haversine(i.coord, centre)
        distance_from_position.append(distance)

    for i in range(len(distance_from_position)):
        if distance_from_position[i] < r:
            names_2.append(names_1[i])
    
    names_2.sort()
    return names_2
  

"""------------------------------------------"""

"""Task 1D"""

def rivers_with_station(stations):
    
    #Variable
    river_name = set()        #River names, use set to prevent repetition
    
    #Get river names
    for river in stations:
        river_name.add(river.river)

    #Eliminate rivers with no stations
    for name in river_name:
        for station in stations:
            if name == station.river:
                if station.name == None:
                    river_name.remove(name)

    return river_name


def stations_by_river(stations):

    #Variables
    river_name = set()        #River names, use set to prevent repetition
    s_on_river = set()        #Station names on a given river
    s_dict = {}               #Dictionary of river name to stations on that river
    
    #Get river names
    for location in stations:
        river_name.add(location.river)
    
    #Get the names of the stations on a river
    for names in river_name:
        for items in stations:
            if items.river == names:
                s_on_river.add(items.name)
        s_dict.update({names:s_on_river})
        #Empties the set
        s_on_river = set()
 
    return s_dict

"""------------------------------------------"""

"""Task 1E"""

def rivers_by_station_number(stations, N):

    #Varaibles
    name_of_rivers = set()      #Ensure no repeting names
    name_n_num = []             #Unsorted
    name_n_num_1 = []           #Sorted
    name_n_num_N = []           #Final list WITH repetition check
    n = 0                       #Number of stations count

    #Get river names
    for names in stations:
        name_of_rivers.add(names.river)

    #Get number of stations n on each river
    for river in name_of_rivers:
        for object in stations:
            if river == object.river:
                n += 1
        #Creating the list of tuples
        name_n_num.append((river,n))
        n = 0
    
    #Sort the list of tuples with the largest key first
    name_n_num_1 = sorted_by_key(name_n_num, 1, reverse=True)
    
    #More variables
    temp_0 = name_n_num_1[N]    #Get [N]
    temp_1 = []                 #Final list but WITHOUT repetition check
    
    #First print from [0] to [N]
    for i in range(0, N-1):
        temp_1.append(name_n_num_1[i])
    
    #Add [N] and subsequent elements if n is the same
    [temp_1.append(item) for item in name_n_num_1 if item[1] == temp_0[1]]

    #Check for repetitionn
    [name_n_num_N.append(j) for j in temp_1 if j not in name_n_num_N]

    return name_n_num_N

"""------------------------------------------"""