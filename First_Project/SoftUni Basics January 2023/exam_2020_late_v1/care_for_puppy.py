available_food = int(input()) * 1000

food_eaten = 0

while True:
    command = input()
    if command == "Adopted":
        break
    else:
        food_eaten += int(command)

if food_eaten > available_food:
    print(f"Food is not enough. You need {food_eaten - available_food} grams more.")
else:
    print(f"Food is enough! Leftovers: {available_food - food_eaten} grams.")
