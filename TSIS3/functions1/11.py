s = input()
def palindrome(s):
    answer = True
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            answer = False
    return answer
print(palindrome(s))