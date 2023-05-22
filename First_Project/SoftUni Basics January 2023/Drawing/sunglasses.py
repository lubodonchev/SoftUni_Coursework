from math import ceil, floor

n = int(input())

for _ in range(2 * n):
    print('*', end='')
for _ in range(n):
    print(' ', end='')
for _ in range(2 * n):
    print('*', end='')
print()

for _ in range(floor((n - 3) / 2)):
    print('*', end='')
    for _ in range(2 * n - 2):
        print('/', end='')
    print('*', end='')
    for _ in range(n):
        print(' ', end='')
    print('*', end='')
    for _ in range(2 * n - 2):
        print('/', end='')
    print('*')

print('*', end='')
for _ in range(2 * n - 2):
    print('/', end='')
print('*', end='')
for _ in range(n):
    print('|', end='')
print('*', end='')
for _ in range(2 * n - 2):
    print('/', end='')
print('*')

for _ in range(ceil((n - 3) / 2)):
    print('*', end='')
    for _ in range(2 * n - 2):
        print('/', end='')
    print('*', end='')
    for _ in range(n):
        print(' ', end='')
    print('*', end='')
    for _ in range(2 * n - 2):
        print('/', end='')
    print('*')

for _ in range(2 * n):
    print('*', end='')
for _ in range(n):
    print(' ', end='')
for _ in range(2 * n):
    print('*', end='')
