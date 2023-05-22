most_goals = 0
best_player = ""

while True:
    name = str(input())
    if name == "END":
        break
    goals = int(input())

    if goals > most_goals:
        most_goals = goals
        best_player = name

    if goals > 9:
        break

print(f'{best_player} is the best player!')
if most_goals > 2:
    print(f'He has scored {most_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {most_goals} goals.')
