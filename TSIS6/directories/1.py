# Write a Python program to list only directories,
#  files and all directories,
#  files in a specified path

import os
path = '/Users/Lenovo/Desktop/pp2-21B050634/tsis6'
# path = input()
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])
