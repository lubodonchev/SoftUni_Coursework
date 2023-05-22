n = int(input())

for _ in range(n):
    flag = False
    string = str(input())
    for ch in string:
        if ch == ',' or ch == '.' or ch == '_':
            flag = True
    if flag:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')
