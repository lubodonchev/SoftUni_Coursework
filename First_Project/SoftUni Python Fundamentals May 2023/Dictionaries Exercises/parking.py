n = int(input())
master_dic = {}

for _ in range(n):
    data = input().split()
    if data[0] == 'register':
        if data[1] not in master_dic.keys():
            master_dic[data[1]] = data[2]
            print(f'{data[1]} registered {data[2]} successfully')
        else:
            print(f'ERROR: already registered with plate number {master_dic[data[1]]}')
    else:
        if data[1] not in master_dic.keys():
            print(f'ERROR: user {data[1]} not found')
        else:
            master_dic.pop(data[1])
            print(f'{data[1]} unregistered successfully')

for key, value in master_dic.items():
    print(f'{key} => {value}')
