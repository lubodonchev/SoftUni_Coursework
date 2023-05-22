quantity = int(input())
days_left = int(input())

counter = 1
cost = 0
spirit = 0

for _ in range(days_left):
    if counter % 11 == 0:
        quantity += 2

    if counter % 2 == 0:
        cost += quantity * 2
        spirit += 5
    if counter % 3 == 0:
        cost += quantity * 8
        spirit += 13
    if counter % 5 == 0:
        cost += quantity * 15
        spirit += 17
    if counter % 3 == 0 and counter % 5 == 0:
        spirit += 30

    if counter % 10 == 0:
        spirit -= 20
        cost += 23

    if counter == days_left and counter % 10 == 0:
        spirit -= 30

    counter += 1

print(f'Total cost: {cost}')
print(f'Total spirit: {spirit}')
