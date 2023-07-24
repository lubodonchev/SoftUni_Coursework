data = input()
index = 0

for ch in data:
    if ch == ':':
        print(ch, end='')
        print(data[data.index(ch) + 1])
        data = data.replace(':', '', 1)
