data = input()
replaced_string = ''
prev_char = ''

for ch in data:
    if ch == prev_char:
        continue

    replaced_string += ch
    prev_char = ch

print(replaced_string)
