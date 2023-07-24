lst = [char for char in input() if char != " "]

dic = {char: lst.count(char) for char in lst}

for key, value in dic.items():
    print(f'{key} -> {value}')
