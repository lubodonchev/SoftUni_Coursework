n = int(input())
current = 0
flag = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        current += 1
        if row == col:
            print(current)
        else:
            print(current, end=" ")
        if current == n:
            flag = True
            break
    if flag:
        break
