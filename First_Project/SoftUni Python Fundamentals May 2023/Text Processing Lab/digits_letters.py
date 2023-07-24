data = input()
digit_data, letter_data, other_data = data, data, data

for ch in data:
    if not ch.isdigit():
        digit_data = digit_data.replace(ch, '')
print(digit_data)

for ch in data:
    if not ch.isalpha():
        letter_data = letter_data.replace(ch, '')
print(letter_data)

for ch in data:
    if ch.isalnum():
        other_data = other_data.replace(ch, '')
print(other_data)
