# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
text = input()
#text = 'abb_bb'
pattern = 'a.+b$'
match = re.search(pattern, text)
if match:
    print('match found: ', match.group())
else:
    print('no match')