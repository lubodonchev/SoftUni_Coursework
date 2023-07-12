def stats(d):
    total_keys = 0
    total_quantity = 0

    print('Products in stock:')

    for key in d.keys():
        total_keys += 1
        total_quantity += d[key]
        print(f'- {key}: {d[key]}')

    print(f'Total Products: {total_keys}')
    print(f'Total Quantity: {total_quantity}')


dct = {}

while True:
    data = input()

    if data == 'statistics':
        stats(dct)
        quit()

    lst = data.split(': ')

    product = lst[0]
    quantity = int(lst[1])

    if product in dct.keys():
        dct[product] += quantity
    else:
        dct[product] = quantity
