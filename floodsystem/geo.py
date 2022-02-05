# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations, p):

    name_n_dis = []
    s_name = []
    s_dis = []

    for location in stations:
        s_name.append(location.name)
        s_dis.append(haversine(location.coord, p))

    for i in range(len((s_name))):
        name_n_dis.append((s_name[i], s_dis[i]))

    return sorted_by_key(name_n_dis, 1)
    

"""------------------------------------------"""

"""Task 1C"""

def stations_within_radius(stations, centre, r):
    distance_from_position = []
    names = []
    station_coordinates = []
    station_x_coordinate = []
    station_y_coordinate = []
    for i in stations:
        station_coordinates.append(i.coord)
    for i in stations:
        names.append(i.name)

    for i in range(len(station_coordinates)):
        station_x_coordinate.append(station_coordinates[i][0])
    
    for i in range(len(station_coordinates)):
        station_y_coordinate.append(station_coordinates[i][1])
    
    for i in range(len(station_coordinates)):
        a = station_x_coordinate[i]
        b = station_y_coordinate[i]
        distance = ((a - centre)**2 + b**2)**0.5
        distance_from_position.append(distance)

    for i in distance_from_position:
        if i > r:
            names.pop(i)
        else:
            continue

"""------------------------------------------"""


"""Task 1D"""

def rivers_with_station(stations):

    river_name = set()

    for river in stations:
        river_name.add(river.river)

    return river_name


def stations_by_river(stations):

    river_name = set()
    s_on_river = set()
    s_dict = {}
    
    for location in stations:
        river_name.add(location.river)
    
    for names in river_name:
        for items in stations:
            if items.river == names:
                s_on_river.add(items.name)
        s_dict.update({names:s_on_river})
        s_on_river = set()
 
    return s_dict

"""------------------------------------------"""

"""Task 1E"""

def rivers_by_station_number(stations, N):

    name_of_rivers = set()
    name_n_num = []
    name_n_num_N = []
    n = 0

    for names in stations:
        name_of_rivers.add(names.river)

    for river in name_of_rivers:
        for object in stations:
            if river == object.river:
                n += 1
        name_n_num.append((river,n))
        n = 0

    sorted_by_key(name_n_num, 1, reverse=True)

    temp_0 = name_n_num[N]

    for i in range(0,N-1):
        name_n_num_N.append(name_n_num[i])

    for item in name_n_num:
        if item[1] == temp_0[1]:
            name_n_num_N.append(item)

    return name_n_num_N

"""------------------------------------------"""
