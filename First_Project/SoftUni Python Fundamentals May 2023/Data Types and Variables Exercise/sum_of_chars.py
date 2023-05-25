n = int(input())
total = 0

for _ in range(n):
    a = str(input())
    total += int(ord(a))

print(f'The sum equals: {total}')
