from math import floor

n = int(input())
points = 0
red, orange, yellow, white, black, other = 0, 0, 0, 0, 0, 0
for _ in range(n):
    color = str(input())

    if color == "red":
        points += 5
        red += 1
    elif color == "orange":
        points += 10
        orange += 1
    elif color == "yellow":
        points += 15
        yellow += 1
    elif color == "white":
        points += 20
        white += 1
    elif color == "black":
        points = floor(points / 2)
        black += 1
    else:
        other += 1
        continue

print(f"Total points: {points}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black}")
