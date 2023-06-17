def jump(lst, value, initial_index):
    land_index = initial_index + value
    if land_index not in range(len(lst)):
        land_index = 0
    if lst[land_index] == 0:
        print(f'Place {land_index} already had Valentine\'s day.')
    elif lst[land_index] == 2:
        lst[land_index] -= 2
        print(f'Place {land_index} has Valentine\'s day.')
    else:
        lst[land_index] -= 2
    return lst, land_index


houses_lst = [int(element) for element in input().split('@')]
index = 0

while True:
    command = input().split()
    if command[0] == 'Love!':
        break
    elif command[0] == 'Jump':
        houses_lst, index = jump(houses_lst, int(command[1]), index)

print(f'Cupid\'s last position was {index}.')
if houses_lst.count(0) == len(houses_lst):
    print('Mission was successful.')
else:
    failed_houses = len(houses_lst) - houses_lst.count(0)
    print(f'Cupid has failed {failed_houses} places.')
