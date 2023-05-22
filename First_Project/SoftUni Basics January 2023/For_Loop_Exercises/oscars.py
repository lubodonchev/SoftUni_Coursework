actor = str(input())
initial_points = float(input())
n = int(input())

for _ in range(n):
    rater = str(input())
    points = float(input())
    initial_points += len(rater) * points / 2

    if initial_points > 1250.5:
        result = f"Congratulations, {actor} got a nominee for leading role with {initial_points:.1f}!"
        break
else:
    result = f"Sorry, {actor} you need {1250.5 - initial_points:.1f} more!"

print(result)
