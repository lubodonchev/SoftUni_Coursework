import math

area = int(input())
grape_per_meter = float(input())
wine_needed = int(input())
workers = int(input())

liters_wine = 0.4 * area * grape_per_meter / 2.5

if liters_wine < wine_needed:
    print(f'It will be a tough winter! More {math.floor(wine_needed - liters_wine)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(liters_wine)} liters.')
    print(f'{math.floor(liters_wine - wine_needed)} liters left -> {math.floor((liters_wine - wine_needed) / workers)}'
          f' liters per person.”')
