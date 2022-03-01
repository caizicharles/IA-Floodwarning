import matplotlib as plt
from datetime import datetime , timedelta


dates = [datetime(2022 , 2 , 1) , datetime(2022 , 2 , 2)]
x = plt.dates.date2num(dates)

print(x)