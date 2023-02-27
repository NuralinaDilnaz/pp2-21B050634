# Write a Python program that matches a string that has an 'a' followed by 0 or more 'b''s.
# has a and  {0,} times b
import re
text = input()
#text = 'abcdebfgbu'
pattern = 'ab*?'
match = re.search(pattern, text)
if match:
    print('match found: ', match.group())
else:
    print('no match')
