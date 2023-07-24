master_dic = {}

while True:
    data = input().split(' : ')
    if data[0] == 'end':
        break
    if data[0] not in master_dic.keys():
        master_dic[data[0]] = []
    master_dic[data[0]].append(data[1])

for key, value in master_dic.items():
    print(f'{key}: {len(value)}')
    for element in value:
        print(f'-- {element}')
