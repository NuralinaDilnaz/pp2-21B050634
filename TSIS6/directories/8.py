# Write a Python program to delete file by specified path.
#  Before deleting check for access
#  and whether a given path exists or not.

import os
path = input()
print(os.path.exists(path))
if os.path.exists(path):
    os.remove("new.txt")
