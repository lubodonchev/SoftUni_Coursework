def urgent(lst, item):
    if item not in lst:
        lst.insert(0, item)
    return lst


def unnecessary(lst, item):
    if item in lst:
        lst.remove(item)
    return lst


def correct(lst, item_old, item_new):
    if item_old in lst:
        lst[lst.index(item_old)] = item_new
    return lst


def rearrange(lst, item):
    if item in lst:
        lst.remove(item)
        lst.append(item)
    return lst


groceries_lst = input().split('!')

while True:
    command_lst = input().split()

    if command_lst[0] == 'Go':
        break
    elif command_lst[0] == 'Urgent':
        groceries_lst = urgent(groceries_lst, command_lst[1])
    elif command_lst[0] == 'Unnecessary':
        groceries_lst = unnecessary(groceries_lst, command_lst[1])
    elif command_lst[0] == 'Correct':
        groceries_lst = correct(groceries_lst, command_lst[1], command_lst[2])
    elif command_lst[0] == 'Rearrange':
        groceries_lst = rearrange(groceries_lst, command_lst[1])

print(*groceries_lst, sep=', ')
