# Write a Python program to drop microseconds from datetime.


from datetime import datetime
date = datetime.now().replace(microsecond=0)
print(date)

# another version of code
# from datetime import date
# date = date.today()
# print(date)