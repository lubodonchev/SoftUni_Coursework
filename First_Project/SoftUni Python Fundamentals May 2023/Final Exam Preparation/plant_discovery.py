def rate(dic, name, new_rating):
    dic[name]['ratings'].append(new_rating)
    return dic


def update(dic, name, new_rarity):
    dic[name]['rarity'] = new_rarity
    return dic


def reset(dic, name):
    dic[name]['ratings'] = []
    return dic


n = int(input())
master_dic = {}

for _ in range(n):
    data = input().split('<->')
    master_dic[data[0]] = {'rarity': int(data[1]), 'ratings': []}

while True:
    command = input().split(': ')
    if command[0] == 'Exhibition':
        break
    elif command[0] == 'Rate':
        plant, rating = command[1].split(' - ')
        if plant not in master_dic.keys():
            print('error')
            continue
        master_dic = rate(master_dic, plant, int(rating))
    elif command[0] == 'Update':
        plant, rarity = command[1].split(' - ')
        if plant not in master_dic.keys():
            print('error')
            continue
        master_dic = update(master_dic, plant, int(rarity))
    elif command[0] == 'Reset':
        if command[1] not in master_dic.keys():
            print('error')
            continue
        master_dic = reset(master_dic, command[1])


print(f'Plants for the exhibition:')
for key, value in master_dic.items():
    try:
        avg = sum(value['ratings']) / len(value['ratings'])
    except ZeroDivisionError:
        avg = 0
    print(f" - {key}; Rarity: {value['rarity']}; Rating: {avg:.2f}")
