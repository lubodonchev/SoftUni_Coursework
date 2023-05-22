from math import floor

number_of_tournaments = int(input())
initial_points = int(input())
points = 0
count = 0

for _ in range(number_of_tournaments):
    result = str(input())

    if result == "W":
        points += 2000
        count += 1
    elif result == "F":
        points += 1200
    elif result == "SF":
        points += 720

total = initial_points + points
avg = points / number_of_tournaments
percent = count / number_of_tournaments * 100

print(f"Final points: {total}\nAverage points: {floor(avg)}\n{percent:.2f}%")
