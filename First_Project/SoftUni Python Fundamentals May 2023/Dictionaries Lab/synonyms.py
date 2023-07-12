n = int(input())

dic = {}

for _ in range(n):
    current_word = str(input())
    current_synonym = str(input())

    if current_word in dic.keys():
        dic[current_word].append(current_synonym)
    else:
        dic[current_word] = [current_synonym]

for key, value in dic.items():
    print(f'{key} - {", ".join(value)}')
