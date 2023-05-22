import math

magnoliq_count = int(input())
zumbul_count = int(input())
rose_count = int(input())
cactus_count = int(input())
gift_price = float(input())

MAGNOLIQ_PRICE = 3.25
ZUMBUL_PRICE = 4
ROSE_PRICE = 3.5
CACTUS_PRICE = 8

income = magnoliq_count * MAGNOLIQ_PRICE + \
         zumbul_count * ZUMBUL_PRICE + \
         rose_count * ROSE_PRICE + \
         cactus_count * CACTUS_PRICE

income *= 0.95

difference = abs(income - gift_price)

if income < gift_price:
    print(f'She will have to borrow {math.ceil(difference)} leva.')
else:
    print(f'She is left with {math.floor(difference)} leva.')
