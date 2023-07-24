import re

text = input()
regex = r'\b_[A-Za-z]+\b|\d+\b'

matches = re.findall(regex, text)

new_text = ', '.join(matches)

new_regex = r'[A-Za-z]+'

final = re.findall(new_regex, new_text)

print(','.join(final))
