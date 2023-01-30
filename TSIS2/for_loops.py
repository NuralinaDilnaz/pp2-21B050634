fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":  # looping through a string, each letter 
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break    # output: apple banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break   #stops
  print(x) # only 1 output: apple

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue  # without banana
  print(x)   # output: apple cherry

for x in range(6): #[0, 6)
  print(x)  # from 0 to 5

for x in range(2, 6):  #[2, 6)
  print(x)     # 2 3 4 5

for x in range(2, 30, 3):  #(starting point, boundary-1, adding element)
  print(x)   # 2 5 8 11...26 29

for x in range(6):
  print(x)
else:
  print("Finally finished!")  

for x in range(6):
  if x == 3: break   # 0 1 2 
  print(x)
else:   # loop broke, else can't be executed
  print("Finally finished!")  

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)  

for x in [0, 1, 2]:  # if empty loop
  pass    # with pass -> no error


