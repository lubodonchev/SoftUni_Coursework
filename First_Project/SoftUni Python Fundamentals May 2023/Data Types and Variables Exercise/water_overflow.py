n = int(input())
total = 0

for i in range(n):
    liters = int(input())
    if liters > 255 - total:
        print('Insufficient capacity!')
        continue
    else:
        total += liters

print(total)
