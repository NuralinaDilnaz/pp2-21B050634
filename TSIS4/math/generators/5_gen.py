# Implement a generator that returns all numbers from (n) down to 0.
n = int(input())
def decreasing_order(n):
    for i in range(n):
        yield n-i-1
for num in decreasing_order(n):
    print(num)