import re

travel_points = 0
lst = []

text = input()
regex = r'=[A-Z][A-Za-z]{2,}=|/[A-Z][A-Za-z]{2,}/'

matches = re.findall(regex, text)

for element in matches:
    if '=' in element:
        clean_word = element.strip('=')
    else:
        clean_word = element.strip('/')

    lst.append(clean_word)
    travel_points += len(clean_word)

destinations_output = ', '.join(lst)

print(f'Destinations: {destinations_output}')
print(f'Travel Points: {travel_points}')
