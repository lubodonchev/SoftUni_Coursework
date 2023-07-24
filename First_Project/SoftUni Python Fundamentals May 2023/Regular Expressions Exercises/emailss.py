import re

text = input()

regex = r'\s[a-z0-9]+[\-_\.]*[a-z0-9]*@[a-z]+[\-]*[a-z]*\.[a-z]\.*[a-z]*\.*[a-z]+'

# regex = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+(\.[a-z]+)+)\b'

matches = re.findall(regex, text, re.IGNORECASE)

for element in matches:
    print(element)
