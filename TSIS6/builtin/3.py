# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

string = input()
f = "".join(reversed(string))
if string == f:
    print("Yes")
else:
    print("No")

