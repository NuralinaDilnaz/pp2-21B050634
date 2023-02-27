# Write a Python program to find sequences of lowercase letters joined with a underscore
import re
text = input()
#text = 'abb_bbc'
pattern = '^[a-z]+_[a-z]+$'  
match = re.search(pattern, text)
if match:
    print('match found: ', match.group())
else:
    print('no match')