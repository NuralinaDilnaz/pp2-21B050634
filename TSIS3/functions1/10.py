#unique elements
def unique(n):
    unique_list = []
    while len(n) > 0:
        i = n[0]
        n.pop(0)
        if i not in n:
            unique_list.append(i)
    unique_list.sort()
    return unique_list       
n = list(map(int, input().split()))
print(*unique(n))