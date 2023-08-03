def new_follower(dic, username):
    if username not in dic.keys():
        dic[username] = {'likes': 0, 'comments': 0}
    return dic


def like(dic, username, count):
    if username in dic.keys():
        dic[username]['likes'] += count
    else:
        dic[username] = {'likes': 0, 'comments': 0}
        dic[username]['likes'] = count
    return dic


def comment(dic, username):
    if username in dic.keys():
        dic[username]['comments'] += 1
    else:
        dic[username] = {'likes': 0, 'comments': 0}
        dic[username]['comments'] = 1
    return dic


def blocked(dic, username):
    if username in dic.keys():
        del dic[username]
    else:
        print(f'{username} doesn\'t exist.')
    return dic


master_dic = {}

while True:
    command = input().split(': ')

    if command[0] == 'Log out':
        break
    elif command[0] == 'New follower':
        master_dic = new_follower(master_dic, command[1])
    elif command[0] == 'Like':
        master_dic = like(master_dic, command[1], int(command[2]))
    elif command[0] == 'Comment':
        master_dic = comment(master_dic, command[1])
    elif command[0] == 'Blocked':
        master_dic = blocked(master_dic, command[1])

print(f"{len(master_dic)} followers")
for key, value in master_dic.items():
    print(f"{key}: {int(value['comments']) + int(value['likes'])}")
