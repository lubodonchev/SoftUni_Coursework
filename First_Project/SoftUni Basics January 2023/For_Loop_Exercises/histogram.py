n = int(input())

r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0

# r1, r2, r3, r4, r5 = 0, 0, 0, 0, 0

for _ in range(n):
    current_number = int(input())

    if current_number < 200:
        r1 += 1
    elif current_number <= 399:
        r2 += 1
    elif current_number <= 599:
        r3 += 1
    elif current_number <= 799:
        r4 += 1
    else:
        r5 += 1

p1 = r1 / n * 100
p2 = r2 / n * 100
p3 = r3 / n * 100
p4 = r4 / n * 100
p5 = r5 / n * 100

print(f'{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%')
