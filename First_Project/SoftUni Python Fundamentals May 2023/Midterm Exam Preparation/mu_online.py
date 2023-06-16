health = 100
bitcoins = 0


def potion(health_points, heal):
    if health_points + heal > 100:
        heal = 100 - health_points
        health_points = 100
    else:
        health_points += heal
    print(f'You healed for {heal} hp.')
    print(f'Current health: {health_points} hp.')
    return health_points


def chest(bit_points, value):
    bit_points += value
    print(f'You found {value} bitcoins.')
    return bit_points


def fight(health_points, strength):
    health_points -= strength
    return health_points


room_lst = input().split('|')

for element in room_lst:
    split_lst = element.split()
    if split_lst[0] == 'potion':
        health = potion(health, int(split_lst[1]))
    elif split_lst[0] == 'chest':
        bitcoins = chest(bitcoins, int(split_lst[1]))
    else:
        health = fight(health, int(split_lst[1]))
        if health <= 0:
            print(f'You died! Killed by {split_lst[0]}.')
            print(f'Best room: {room_lst.index(element) + 1}')
            quit()
        else:
            print(f'You slayed {split_lst[0]}.')

print('You\'ve made it!')
print(f'Bitcoins: {bitcoins}')
print(f'Health: {health}')
