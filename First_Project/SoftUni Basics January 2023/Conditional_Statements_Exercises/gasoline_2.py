gas_type = str(input())
quantity = float(input())
card = str(input())
total = 0

GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93

if card == "Yes":
    if gas_type == "Gasoline":
        GASOLINE_PRICE -= 0.18
    elif gas_type == "Diesel":
        DIESEL_PRICE -= 0.12
    elif gas_type == "Gas":
        GAS_PRICE -= 0.08

if gas_type == "Gasoline":
    total = quantity * GASOLINE_PRICE
elif gas_type == "Diesel":
    total = quantity * DIESEL_PRICE
elif gas_type == "Gas":
    total = quantity * GAS_PRICE

if 20 <= quantity <= 25:
    total *= 0.92
elif quantity > 25:
    total *= 0.9

print(f'{total:.2f} lv.')
