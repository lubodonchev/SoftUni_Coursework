todo_lst = [0 for i in range(10)]

while True:
    command_lst = input().split('-')

    if command_lst[0] == 'End':
        break

    todo_lst.pop(int(command_lst[0]) - 1)
    todo_lst.insert(int(command_lst[0]) - 1, command_lst[1])

result = [element for element in todo_lst if element != 0]

print(result)


