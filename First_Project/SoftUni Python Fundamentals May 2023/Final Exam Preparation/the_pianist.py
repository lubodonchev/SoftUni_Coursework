def add(dic, piece, composer, key):
    if piece not in dic.keys():
        dic[piece] = {'composer': composer, 'key': key}
        print(f'{piece} by {composer} in {key} added to the collection!')
    else:
        print(f'{piece} is already in the collection!')
    return dic


def remove(dic, piece):
    if piece in dic.keys():
        del dic[piece]
        print(f'Successfully removed {piece}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return dic


def change_key(dic, piece, new_key):
    if piece in dic.keys():
        dic[piece]['key'] = new_key
        print(f'Changed the key of {piece} to {new_key}!')
    else:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    return dic


n = int(input())
master_dic = {}

for _ in range(n):
    data = input().split('|')

    master_dic[data[0]] = {'composer': data[1], 'key': data[2]}

while True:
    command = input().split('|')

    if command[0] == 'Stop':
        break
    elif command[0] == 'Add':
        master_dic = add(master_dic, command[1], command[2], command[3])
    elif command[0] == 'Remove':
        master_dic = remove(master_dic, command[1])
    elif command[0] == 'ChangeKey':
        master_dic = change_key(master_dic, command[1], command[2])

for keys, values in master_dic.items():
    pie = keys
    comp = values['composer']
    k = values['key']
    print(f'{pie} -> Composer: {comp}, Key: {k}')

