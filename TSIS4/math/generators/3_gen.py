# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
n = int(input())
def generator(n):
    for i in range(n):
        if i%3==0 and i%4==0 : # only divisible by 3 and 4
            yield i
for num in generator(n):
    print(num)
