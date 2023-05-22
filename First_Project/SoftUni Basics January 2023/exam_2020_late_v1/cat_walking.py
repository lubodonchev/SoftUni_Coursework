minutes_walk = int(input())
number_of_walks = int(input())
calorie_intake = int(input())

if minutes_walk * 5 * number_of_walks >= 0.5 * calorie_intake:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {minutes_walk * 5 * number_of_walks}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {minutes_walk * 5 * number_of_walks}.')
