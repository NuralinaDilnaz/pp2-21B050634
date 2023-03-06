# Write a Python program to write a list to a file.
list = input() #[one, two, three]
with open('filename.txt', "a") as f:
    for x in list:
        f.write("\n%s"% x)

b = open('filename.txt')
print(b.read())

