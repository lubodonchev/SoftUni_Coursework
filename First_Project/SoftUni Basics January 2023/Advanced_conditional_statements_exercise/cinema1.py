type1 = str(input())
r = int(input())
c = int(input())

price = 0

if type1 == 'Premiere':
    price = 12
elif type1 == 'Normal':
    price = 7.5
elif type1 == 'Discount':
    price = 5

total = price * r * c

print(f'{total:.2f} leva')
