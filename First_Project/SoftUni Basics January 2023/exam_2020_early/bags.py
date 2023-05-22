price_above_20 = float(input())
kg_luggage = float(input())
days_left = int(input())
bags = int(input())

if kg_luggage < 10:
    price = 0.2 * price_above_20
elif kg_luggage <= 20:
    price = 0.5 * price_above_20
else:
    price = price_above_20

if days_left > 30:
    price *= 1.1
elif days_left >= 7:
    price *= 1.15
else:
    price *= 1.4

total = bags * price
print(f'The total price of bags is: {total:.2f} lv.')
