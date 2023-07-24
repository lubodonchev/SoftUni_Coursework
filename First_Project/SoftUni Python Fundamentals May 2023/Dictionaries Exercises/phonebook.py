data = input()
phone_lst = []
while True:
    if data.isdigit():
        break

    lst = data.split('-')
    for element in lst:
        phone_lst.append(element)

    data = input()

keys = [element for element in phone_lst if (phone_lst.index(element) + 1) % 2 != 0]
values = [element for element in phone_lst if (phone_lst.index(element) + 1) % 2 == 0]

dic = dict(zip(keys, values))

for _ in range(int(data)):
    name = input()
    if name in dic.keys():
        print(f'{name} -> {dic[name]}')
    else:
        print(f'Contact {name} does not exist.')
