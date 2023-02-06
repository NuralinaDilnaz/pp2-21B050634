def solve(numheads, numlegs):
    cnt = 0
    for i in range(numheads):
        cnt = i
        if(numlegs-2*i)/(numheads-i)==4:
            r = numheads - cnt
            x = [cnt, r]
            return (x)
a = solve(35, 94)
print("chickens =", a[0])
print("rabbits =", a[1])