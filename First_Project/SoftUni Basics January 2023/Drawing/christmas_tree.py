n = int(input())

for i in range(n + 1):
    for _ in range(n - i):
        print(' ', end='')
    for _ in range(i):
        print('*', end='')
    print(' | ', end='')
    for _ in range(i):
        print('*', end='')
    for _ in range(n - i):
        print(' ', end='')
    print()

