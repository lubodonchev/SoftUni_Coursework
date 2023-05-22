quantity = int(input())
vid = str(input())
delivery = str(input())

price = 0

if quantity < 10:
    print("Invalid order")
else:
    if vid == "90X130":
        price = 110
        if quantity > 60:
            price *= 0.92
        elif quantity > 30:
            price *= 0.95
    elif vid == "100X150":
        price = 140
        if quantity > 80:
            price *= 0.90
        elif quantity > 40:
            price *= 0.94
    elif vid == "130X180":
        price = 190
        if quantity > 50:
            price *= 0.88
        elif quantity > 20:
            price *= 0.93
    elif vid == "200X300":
        price = 250
        if quantity > 50:
            price *= 0.86
        elif quantity > 25:
            price *= 0.91

    preliminary = quantity * price

    if delivery == "With delivery":
        preliminary += 60

    if quantity > 90:
        preliminary *= 0.96

    print(f'{preliminary:.2f} BGN')
