# Write a Python program to count the number of lines in a text file.

with open('filename.txt') as f:
    x = len(f.readlines())
    print(x)
