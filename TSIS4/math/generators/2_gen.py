# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
n = int(input())
def evens(n):
    for i in range(n):
        if i%2 ==0 :
            yield i
list = []
for num in evens(n):
    list.append(num)
s = str(list)
print(s[1:len(s)-1])



 