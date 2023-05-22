n = int(input())
result = 0

for i in range(1, n + 1):
    i = str(i)
    total = 0
    for a in range(len(i)):
        total += int(i[a])
    if total == 5 or total == 7 or total == 11:
        result = 'True'
    else:
        result = 'False'

    print(f'{i} -> {result}')
