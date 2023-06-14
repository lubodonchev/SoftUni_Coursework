energy = int(input())
battles_won = 0

while True:
    command = str(input())
    if command == 'End of battle':
        print(f'Won battles: {battles_won}. Energy left: {energy}')
        break
    distance = int(command)
    if distance > energy:
        print(f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
        break
    energy -= distance
    battles_won += 1
    if battles_won % 3 == 0:
        energy += battles_won
