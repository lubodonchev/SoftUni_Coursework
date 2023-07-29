import re

text = input()
cool_threshold = 1
emoji_lst = []
clean_lst = []
cool_emojis_lst = []

digit_checker = r'\d'
emoji_checker = r'(::|\*\*)[A-Z][a-z]{2,}\1'

digit_lst = re.findall(digit_checker, text)

for digit in digit_lst:
    cool_threshold *= int(digit)

matches = re.finditer(emoji_checker, text)

for match in matches:
    emoji_lst.append(match.group())

for element in emoji_lst:
    if ':' in element:
        clean_emoji = element.strip('::')
    else:
        clean_emoji = element.strip('**')
    clean_lst.append(clean_emoji)

for element in emoji_lst:
    coolness = 0
    for ch in element:
        if ch.isalpha():
            coolness += ord(ch)
    if coolness > cool_threshold:
        cool_emojis_lst.append(element)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emoji_lst)} emojis found in the text. The cool ones are:')
for element in cool_emojis_lst:
    print(element)
