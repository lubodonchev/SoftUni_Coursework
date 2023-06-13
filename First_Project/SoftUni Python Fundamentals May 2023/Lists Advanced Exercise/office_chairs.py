rooms = int(input())
free_chairs = 0
flag = True

for i in range(rooms):
    lst = input().split()
    if len(lst[0]) < int(lst[1]):
        print(f'{int(lst[1]) - len(lst[0])} more chairs needed in room {i + 1}')
        flag = False
    else:
        free_chairs += len(lst[0]) - int(lst[1])

if flag:
    print(f'Game On, {free_chairs} free chairs left')
