from math import floor, ceil

days_gone = int(input())
food_available = int(input())
deer1_food = float(input())
deer2_food = float(input())
deer3_food = float(input())

food_needed = (deer1_food + deer2_food + deer3_food) * days_gone

if food_available >= food_needed:
    print(f'{floor(food_available - food_needed)} kilos of food left.')
else:
    print(f'{ceil(food_needed - food_available)} more kilos of food are needed.')
