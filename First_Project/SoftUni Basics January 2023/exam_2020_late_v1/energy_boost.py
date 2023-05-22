fruit = str(input())
size = str(input())
amount_of_sets = int(input())

price = 0

if fruit == "Watermelon":
    if size == "small":
        price = 2 * 56
    elif size == "big":
        price = 5 * 28.7
elif fruit == "Mango":
    if size == "small":
        price = 2 * 36.66
    elif size == "big":
        price = 5 * 19.6
elif fruit == "Pineapple":
    if size == "small":
        price = 2 * 42.1
    elif size == "big":
        price = 5 * 24.8
elif fruit == "Raspberry":
    if size == "small":
        price = 2 * 20
    elif size == "big":
        price = 5 * 15.2

total = amount_of_sets * price

if 400 <= total <= 1000:
    total *= 0.85
elif total > 1000:
    total *= 0.5

print(f'{total:.2f} lv.')
