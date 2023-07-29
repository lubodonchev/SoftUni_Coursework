def take_odd(data):
    new_data = ''
    counter = 1
    for ch in data:
        if counter % 2 == 0:
            new_data += ch
        counter += 1
    print(new_data)
    return new_data


def cut(data, index, length):
    end = index + length
    substring = data[index:end]
    data = data.replace(substring, '', 1)
    print(data)
    return data


def substitute(data, old_string, new_string):
    if old_string in data:
        data = data.replace(old_string, new_string)
        print(data)
    else:
        print('Nothing to replace!')
    return data


password = input()

while True:
    command = input().split()
    if command[0] == 'Done':
        break
    elif command[0] == 'TakeOdd':
        password = takeodd(password)
    elif command[0] == 'Cut':
        password = cut(password, int(command[1]), int(command[2]))
    elif command[0] == 'Substitute':
        password = substitute(password, command[1], command[2])

print(f'Your password is: {password}')
