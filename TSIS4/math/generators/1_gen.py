# Create a generator that generates the squares of numbers up to some number N.
N = int(input())
def square_generator(n):
    i = 0
    while i < N:
        yield i**2
        i+=1
for x in square_generator(N):
    print(x)

another interpretation of code

N = int(input())
def square_generator(N):
    for i in range(N):
        yield i**2
for n in square_generator(N):
    print(n)
