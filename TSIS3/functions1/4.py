def filter_prime(list):
    def prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
            return True
    for i in list:
        if prime(int(i)):
            print(i, end = " ") 
n=input().split()
filter_prime(n)