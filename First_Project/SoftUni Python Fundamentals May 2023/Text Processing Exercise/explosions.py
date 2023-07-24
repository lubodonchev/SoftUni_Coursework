data = input()
new_data = ''
prev_char = ''

for ch in data:
    if prev_char == '>':

        hit_strength = data[data.index(ch) + 1]
