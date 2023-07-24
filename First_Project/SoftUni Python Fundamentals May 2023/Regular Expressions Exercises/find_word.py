import re

text = input()
word = input()

regex = f'\\b{word}\\b'

matches = re.findall(regex, text, re.IGNORECASE)

print(len(matches))
