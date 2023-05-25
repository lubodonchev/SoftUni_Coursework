n = int(input())
highest = 0
weii = 0
tii = 0
quaa = 0

for i in range(n):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    grade = (weight / time_needed) ** quality

    if grade > highest:
        highest = grade
        weii = weight
        tii = time_needed
        quaa = quality

print(f'{weii} : {tii} = {int(highest)} ({quaa})')
