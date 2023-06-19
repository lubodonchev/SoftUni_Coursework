def outofstock(lst, item):
    while item in lst:
        lst[lst.index(item)] = 'None'
    return lst


def required(lst, item, index):
    if index in range(len(lst)):
        lst[index] = item
    return lst


def justincase(lst, item):
    lst[-1] = item
    return lst


gift_list = input().split()

while True:
    command_lst = input().split()

    if command_lst[0] == 'No':
        break
    elif command_lst[0] == 'OutOfStock':
        gift_list = outofstock(gift_list, command_lst[1])
    elif command_lst[0] == 'Required':
        gift_list = required(gift_list, command_lst[1], int(command_lst[2]))
    elif command_lst[0] == 'JustInCase':
        gift_list = justincase(gift_list, command_lst[1])

result = [element for element in gift_list if element != 'None']
print(*result, sep=' ')
