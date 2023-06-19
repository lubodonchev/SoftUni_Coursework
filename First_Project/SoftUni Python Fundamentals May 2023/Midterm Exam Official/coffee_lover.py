def include(lst, item):
    lst.append(item)
    return lst


def remove(lst, code, number):
    if len(coffee_lst) >= int(number):
        if code == 'first':
            for _ in range(int(number)):
                lst.pop(0)
        else:
            for i in range(int(number)):
                lst.pop(-1)
    return lst


def prefer(lst, index_one, index_two):
    if int(index_one) in range(len(lst)) and int(index_two) in range(len(lst)):
        lst[int(index_one)], lst[int(index_two)] = lst[int(index_two)], lst[int(index_one)]
    return lst


coffee_lst = input().split()
n = int(input())

for _ in range(n):
    command_lst = input().split()
    if command_lst[0] == 'Include':
        coffee_lst = include(coffee_lst, command_lst[1])
    elif command_lst[0] == 'Remove':
        coffee_lst = remove(coffee_lst, command_lst[1], command_lst[2])
    elif command_lst[0] == 'Prefer':
        coffee_lst = prefer(coffee_lst, command_lst[1], command_lst[2])
    elif command_lst[0] == 'Reverse':
        coffee_lst.reverse()

print('Coffees:')
print(*coffee_lst, sep=' ')
