food, hay, cover, weight = float(input()), float(input()), float(input()), float(input())

for i in range(1, 31):
    food -= 0.3
    if i % 2 == 0:
        hay -= 0.05 * food
    if i % 3 == 0:
        cover -= 1/3 * weight
    if food <= 0 or hay <= 0 or cover <= 0:
        print('Merry must go to the pet store!')
        quit()
print(f'Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.')
