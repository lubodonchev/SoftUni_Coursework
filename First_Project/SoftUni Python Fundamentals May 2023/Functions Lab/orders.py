COFFEE_PRICE = 1.5
WATER_PRICE = 1
COKE_PRICE = 1.4
SNACKS_PRICE = 2


def calculator():
    product = str(input())
    quantity = int(input())

    if product == 'coffee':
        fin = COFFEE_PRICE * quantity
    elif product == 'water':
        fin = WATER_PRICE * quantity
    elif product == 'coke':
        fin = COKE_PRICE * quantity
    elif product == 'snacks':
        fin = SNACKS_PRICE * quantity
    else:
        fin = None

    print(f'{fin:.2f}')


calculator()
