def histogram(l):
    for n in l:
        for i in range(n):
            print('*', end ='')
        print()
num = list(map(int, input().split()))
histogram(num)
