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


"""------------------------------------------"""
