# no idea why it doesn't work

def valid_strike(index, radius, lst):
    if index - radius < 0:
        return False
    elif index + radius >= len(lst):
        return False
    else:
        return True


target_lst = [int(element) for element in input().split()]

while True:
    command_lst = input().split()
    if command_lst[0] == 'End':
        break
    elif command_lst[0] == 'Shoot':
        try:
            target_lst[int(command_lst[1])] -= int(command_lst[2])
            if target_lst[int(command_lst[1])] <= 0:
                target_lst.pop(int(command_lst[1]))
        except IndexError:
            continue
    elif command_lst[0] == 'Add':
        if int(command_lst[1]) in range(len(target_lst)):
            target_lst.insert(int(command_lst[1]), int(command_lst[2]))
        else:
            print('Invalid placement!')
            continue

    elif command_lst[0] == 'Strike':
        if valid_strike(int(command_lst[1]), int(command_lst[2]), target_lst):
            beginning = int(command_lst[1]) - int(command_lst[2])
            end = int(command_lst[1]) + int(command_lst[2])
            del target_lst[beginning:end+1]

        else:
            print('Strike missed!')
            continue

print(*target_lst, sep='|')
