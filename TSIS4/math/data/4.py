# Write a Python program to calculate two date difference in seconds.
from datetime import datetime, time, timedelta 

def func(dt1,dt2):
    timedelta=dt2-dt1
    return timedelta.days*24*3600 + timedelta.seconds
date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()

print("\n%d " %(func(date1, date2)))
print()
