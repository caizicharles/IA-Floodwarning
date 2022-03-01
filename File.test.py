import numpy as np
import matplotlib as plt
from datetime import datetime , timedelta


dates = [datetime(2022 , 2 , 1) , datetime(2022 , 2 , 2)]
x = plt.dates.date2num(dates)

print(x)

y = np.poly1d([1 , 2 , 3])
print(y)

z =  np.polyder(y)
print(z)

output = z(0.5)
print(output)

