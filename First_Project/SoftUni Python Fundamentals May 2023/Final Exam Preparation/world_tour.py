def addition(data, index, string):
    if len(data) > index >= 0:
        data = data[:index] + string + data[index:]
    return data


def removal(data, start_index, end_index):
    if len(data) > end_index >= 0 and len(data) > start_index >= 0:
        data = data[:start_index] + data[end_index + 1:]
    return data


def switch(data, old, new):
    if old in data:
        data = data.replace(old, new)
    return data


text = input()

while True:
    command = input().split(':')
    if command[0] == 'Travel':
        break
    elif command[0] == 'Add Stop':
        text = addition(text, int(command[1]), command[2])
        print(text)
    elif command[0] == 'Remove Stop':
        text = removal(text, int(command[1]), int(command[2]))
        print(text)
    elif command[0] == 'Switch':
        text = switch(text, command[1], command[2])
        print(text)

print(f'Ready for world tour! Planned stops: {text}')
