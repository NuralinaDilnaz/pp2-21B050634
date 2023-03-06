# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string, os
for f in string.ascii_uppercase:
    with open(f + ".txt", "w") as new:
        new.writelines(f)