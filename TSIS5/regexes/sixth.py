# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
text = input()
#text = 'd,. .b, a'
match = re.sub('[ ,.]', ':',  text)
print(match)