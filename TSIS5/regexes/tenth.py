# Write a Python program to convert a given camel case string to snake case.
import re
text = input()
#text = 'camelCase'
answer = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', answer).lower())




