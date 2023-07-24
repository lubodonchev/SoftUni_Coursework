master_dic = {}

while True:
    data = input().split()
    if data[0] == 'buy':
        break

    if data[0] not in master_dic.keys():
        master_dic[data[0]] = {'price': float(data[1]), 'quantity': int(data[2])}
    else:
        master_dic[data[0]]['price'] = float(data[1])
        master_dic[data[0]]['quantity'] += int(data[2])

for key, value in master_dic.items():
    total = value['price'] * value['quantity']
    print(f'{key} -> {total:.2f}')
