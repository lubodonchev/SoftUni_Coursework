import re

text = input()

while text:

    regex = r'\d+'
    matches = re.findall(regex, text)
    if matches:
        print(' '.join(matches), end=' ')
    text = input()
