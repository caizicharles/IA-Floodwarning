from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.station import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_levels

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import datetime