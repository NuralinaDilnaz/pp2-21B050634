# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
text = input()
#text = 'Almaty'
pattern = '^[A-Z]{1}([a-z]+)'
match = re.search(pattern, text)
if match:
    print('match found: ', match.group())
else:
    print('no match')
