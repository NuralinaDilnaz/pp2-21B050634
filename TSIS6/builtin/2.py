# Write a Python program with builtin function that accepts a 
string and calculate the number of upper case letters and lower case letters

a = input()
upper_case = 0
lower_case = 0
for i in a:
    if i.isupper():
        upper_case+=1
    if i.islower():
        lower_case+=1
print(upper_case)
print(lower_case)