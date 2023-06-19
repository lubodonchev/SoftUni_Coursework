def addition(lst, item):
    if item not in lst:
        lst.append(item)
        print('Card successfully added')
    else:
        print('Card is already in the deck')
    return lst


def poppy(lst, index):
    if index in range(len(lst)):
        lst.pop(index)
        print('Card successfully removed')
    else:
        print('Index out of range')
    return lst


def removal(lst, item):
    if item in lst:
        lst.remove(item)
        print('Card successfully removed')
    else:
        print('Card not found')
    return lst


def insertion(lst, index, item):
    if index in range(len(lst)):
        if item not in lst:
            lst.insert(index, item)
            print('Card successfully added')
        else:
            print('Card is already added')
    else:
        print('Index out of range')
    return lst


card_lst = input().split(', ')
n = int(input())

for _ in range(n):
    command_lst = input().split(', ')
    if command_lst[0] == 'Add':
        card_lst = addition(card_lst, command_lst[1])
    elif command_lst[0] == 'Remove At':
        card_lst = poppy(card_lst, int(command_lst[1]))
    elif command_lst[0] == 'Remove':
        card_lst = removal(card_lst, command_lst[1])
    elif command_lst[0] == 'Insert':
        card_lst = insertion(card_lst, int(command_lst[1]), command_lst[2])

print(*card_lst, sep=', ')
