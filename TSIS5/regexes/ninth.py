# Write a Python program to insert spaces between words starting with capital letters.
import re
text = input()
#text = 'AlmaBananAnanas'
print(re.sub(r'([a-z])([A-Z])', r'\1 \2', text))