# Write a Python program that matches a string that has an 'a' followed by 2 to 3 'b'
# has a and {2,3} times b
import re
text = input()
#text = 'abbbbc'
pattern = 'ab{2,3}?'  #'^ab{2,3}$'
match = re.search(pattern, text)
if match:
    print('match found: ', match.group())
else:
    print('no match')