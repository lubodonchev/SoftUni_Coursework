master_dic = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}
flag = False

while True:
    temporary_dic = {}
    data = input().split()
    keys = [element for element in data if (data.index(element) + 1) % 2 == 0]
    values = [int(element) for element in data if (data.index(element) + 1) % 2 != 0]

    a = 0
    for key in keys:
        if key.lower() in temporary_dic.keys():
            temporary_dic[key.lower()] += values[a]
        else:
            temporary_dic[key.lower()] = values[a]
        a += 1

    for key, value in temporary_dic.items():
        if key.lower() in master_dic:
            master_dic[key.lower()] += value
            if master_dic['shards'] >= 250:
                master_dic['shards'] -= 250
                print('Shadowmourne obtained!')
                flag = True
                break
            elif master_dic['fragments'] >= 250:
                master_dic['fragments'] -= 250
                print('Valanyr obtained!')
                flag = True
                break
            elif master_dic['motes'] >= 250:
                master_dic['motes'] -= 250
                print('Dragonwrath obtained!')
                flag = True
                break
        else:
            master_dic[key.lower()] = value
    if flag:
        break
for key, value in master_dic.items():
    print(f'{key}: {value}')
