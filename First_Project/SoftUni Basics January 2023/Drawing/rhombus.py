n = int(input())

for a in range(1, n + 1):
    for _ in range(n - a):
        print(' ', end='')
    for _ in range(a):
        print('*', end=' ')
    for _ in range(n - a):
        print(' ', end='')
    print()

for b in range(n - 1, 0, -1):
    for _ in range(n - b):
        print(' ', end='')
    for _ in range(b):
        print('*', end=' ')
    for _ in range(n - b):
        print(' ', end='')
    print()
