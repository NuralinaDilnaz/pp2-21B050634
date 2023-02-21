# Write a Python program to calculate the area of regular polygon.
import math
sides = int(input())
len_sides = int(input())
s = int((sides*len_sides*len_sides)/(4*math.tan(math.pi/sides)))
print('The area of the polygon is:' , s)