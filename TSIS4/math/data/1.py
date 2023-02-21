# Write a Python program to subtract five days from current date.

from datetime import date, timedelta
day = date.today()-timedelta(5)
print(day)
