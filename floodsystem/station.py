# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

from .utils import sorted_by_key

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        a = self.typical_range
        if a == None:
            return False
        elif a[1] < a[0]:
            return False
        else:
            return True
     
def inconsistent_typical_range_stations(stations):
    stations_inconsistent = []
    for i in stations:
        if MonitoringStation.typical_range_consistent(i) == False:
            stations_inconsistent.append(i.name)
        else:
            continue
    stations_inconsistent.sort()
    return stations_inconsistent
























def stations_highest_rel_level(stations, N):

    dif = []
    station_names = []
    combine = []
    output_0 = []
    output = []

    for station in stations:
        if station.typical_range and station.latest_level != None:
            a = station.typical_range
            b = (a[0] + a[1])/2
            c = station.latest_level - b
            
            if c >= 0:
                station_names.append(station.name)
                dif.append(c)

    combine = [(station_names[i], dif[i]) for i in range(0, len(station_names)) ]
        
    output_0 = sorted_by_key(combine, 1, reverse=True)

    output = [output_0[j] for j in range(0, N)]

    return output
