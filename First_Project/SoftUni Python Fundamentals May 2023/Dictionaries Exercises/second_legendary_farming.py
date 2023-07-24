master_dic = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}
flag = False

while True:
    data = input().split()

    for key in range(0, len(data), 2):
        if data[key + 1].lower() in master_dic:
            master_dic[data[key + 1].lower()] += int(data[key])
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
            master_dic[data[key + 1].lower()] = int(data[key])
    if flag:
        break
for key, value in master_dic.items():
    print(f'{key}: {value}')
