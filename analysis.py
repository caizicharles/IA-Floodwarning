import numpy as np
import matplotlib as plt
from datetime import datetime , timedelta

def polyfit(dates, levels, p):
    times = []
    x = plt.dates.date2num(dates)

    shift = x[-1]       # The last entry (the longest ago) in x
    times = x - shift

    print(times)

    p_coeff = np.polyfit(times , levels , p)
    poly = np.poly1d(p_coeff)
    
    return poly, shift


"""dates = []
levels = []

for i in range(10):
    jg = datetime(2022, 1, 11-i)
    dates.append(jg)

for i in range(10):
    levels.append(i**2 + 5)
print(dates , levels)
x = polyfit(dates , levels , p = 2)

print(x)

shifted_list = original_list[1:]"""

