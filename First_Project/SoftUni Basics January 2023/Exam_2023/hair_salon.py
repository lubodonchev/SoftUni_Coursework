goal = int(input())

total = 0

while True:
    command = str(input())
    if command == "closed":
        break
    elif command == "haircut":
        haircut = str(input())
        if haircut == "mens":
            total += 15
        elif haircut == "ladies":
            total += 20
        elif haircut == "kids":
            total += 10
    elif command == "color":
        color = str(input())
        if color == "touch up":
            total += 20
        elif color == "full color":
            total += 30

    if total >= goal:
        break

if total >= goal:
    print('You have reached your target for the day!')
else:
    print(f'Target not reached! You need {goal - total}lv. more.')
print(f'Earned money: {total}lv.')
