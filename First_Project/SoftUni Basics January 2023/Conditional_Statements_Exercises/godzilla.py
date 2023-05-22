budget = float(input())
statisti_count = int(input())
price_cloth = float(input())
decor = 0.1 * budget

if statisti_count > 150:
    price_cloth *= 0.9

total_cost = statisti_count * price_cloth + decor
difference = abs(budget - total_cost)

if total_cost > budget:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')
