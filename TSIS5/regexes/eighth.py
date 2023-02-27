# Write a Python program to split a string at uppercase letters.
import re
text = input()
#text = 'AlmaBananAnanas'
pattern = '[A-Z][^A-Z]*'
print(re.findall(pattern, text))
