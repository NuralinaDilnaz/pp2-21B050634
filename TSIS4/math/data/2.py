# Write a Python program to print yesterday, today, tomorrow.

from datetime import date, timedelta              


yesterday = date.today()-timedelta(1)   # today() -> method
today = date.today()
tomorrow = date.today()+timedelta(1)

# print(yesterday, today, tomorrow)  
print("Yesterday :", yesterday.strftime('%d-%m-%Y'))    
print("Today :", today.strftime('%d-%m-%Y'))    
print("Tomorrow :", tomorrow.strftime('%d-%m-%Y'))
