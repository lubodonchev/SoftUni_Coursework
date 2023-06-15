# solution by lector; don't know why it works and mine doesn't

def shoot(lst, index, value):
    if index in range(len(lst)):
        if lst[index] <= value:
            lst.pop(index)
        else:
            lst[index] -= value
    return lst


def add(lst, index, value):
    if index in range(len(lst)):
        lst.insert(index, value)
    else:
        print('Invalid placement!')
    return lst


def strike(lst, index, value):
    if index - value in range(len(lst)) and index + value in range(len(lst)):
        lst = lst[0: index - value] + lst[index + value + 1:]
    else:
        print('Strike missed!')
    return lst


target_lst = [int(element) for element in input().split()]
command = input()
while command != 'End':
    command_lst = command.split()

    if command_lst[0] == 'Shoot':
        target_lst = shoot(target_lst, int(command_lst[1]), int(command_lst[2]))
    elif command_lst[0] == 'Strike':
        target_lst = strike(target_lst, int(command_lst[1]), int(command_lst[2]))
    elif command_lst[0] == 'Add':
        target_lst = add(target_lst, int(command_lst[1]), int(command_lst[2]))
    command = input()

print(*target_lst, sep='|')
