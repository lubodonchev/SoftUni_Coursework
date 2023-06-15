chest_lst = input().split('|')

while True:
    command_lst = input().split()
    if command_lst[0] == 'Yohoho!':
        break
    elif command_lst[0] == 'Loot':
        for i in range(1, len(command_lst)):
            if command_lst[i] not in chest_lst:
                chest_lst.insert(0, command_lst[i])
    elif command_lst[0] == 'Drop':
        try:
            n = chest_lst.pop(int(command_lst[1]))
            chest_lst.append(n)
        except IndexError:
            continue
    elif command_lst[0] == 'Steal':
        printed = []
        for i in range(- int(command_lst[1]), 0):
            try:
                n = chest_lst.pop(i)
                printed.append(n)
            except IndexError:
                continue

        print(', '.join(printed))
if not chest_lst:
    print('Failed treasure hunt.')
else:
    summ = 0
    for element in chest_lst:
        summ += len(element)
    average = summ / len(chest_lst)
    print(f'Average treasure gain: {average:.2f} pirate credits.')
