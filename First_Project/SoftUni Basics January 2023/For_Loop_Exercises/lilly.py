age = int(input())
washing_machine_price = float(input())
gift_price = int(input())
money = 0
even_count = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        even_count += 1
        money += even_count * 10 - 1
    else:
        money += gift_price

if money >= washing_machine_price:
    result = f'Yes! {money - washing_machine_price:.2f}'
else:
    result = f'No! {washing_machine_price - money:.2f}'

print(result)
