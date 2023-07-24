import re

dates = input()
regex = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'

matches = re.findall(regex, dates)

for element in matches:
    print(f'Day: {element[0]}, Month: {element[2]}, Year: {element[3]}')
