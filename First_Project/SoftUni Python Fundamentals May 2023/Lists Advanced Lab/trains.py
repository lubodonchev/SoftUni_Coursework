n_wagons = int(input())

train_lst = [0 for i in range(n_wagons)]

while True:
    command_lst = input().split()

    if command_lst[0] == 'End':
        break
    elif command_lst[0] == 'add':
        train_lst[-1] += int(command_lst[1])
    elif command_lst[0] == 'insert':
        train_lst[int(command_lst[1])] += int(command_lst[2])
    elif command_lst[0] == 'leave':
        train_lst[int(command_lst[1])] -= int(command_lst[2])

print(train_lst)
