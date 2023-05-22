days = int(input())
total_available_food = float(input())

cat_total_eaten = 0
dog_total_eaten = 0
total_biscuits = 0

for i in range(1, days + 1):
    dog_food_current_day = int(input())
    dog_total_eaten += dog_food_current_day
    cat_food_current_day = int(input())
    cat_total_eaten += cat_food_current_day

    if i % 3 == 0:
        total_biscuits += (dog_food_current_day + cat_food_current_day) * 0.1


print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{(cat_total_eaten + dog_total_eaten) / total_available_food * 100:.2f}% of the food has been eaten.")
print(f"{dog_total_eaten / (cat_total_eaten + dog_total_eaten) * 100:.2f}% eaten from the dog.")
print(f"{cat_total_eaten / (cat_total_eaten + dog_total_eaten) * 100:.2f}% eaten from the cat.")


