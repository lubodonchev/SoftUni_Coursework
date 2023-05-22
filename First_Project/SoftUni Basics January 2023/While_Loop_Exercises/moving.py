volume = int(input()) * int(input()) * int(input())

boxes_total = 0

while boxes_total < volume:
    command = input()
    if command == 'Done':
        print(f'{volume - boxes_total} Cubic meters left.')
        break
    else:
        boxes_total += int(command)
else:
    print(f'No more free space! You need {boxes_total - volume} Cubic meters more.')
