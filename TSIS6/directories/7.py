# Write a Python program to copy the contents of a file to another file
with open('filename.txt', 'r') as firstfile, open('new.txt', 'w') as secondfile:
    for line in firstfile:
        secondfile.write(line)