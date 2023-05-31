cards = str(input())

lst_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
lst_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

lst = cards.split(' ')

for element in lst:
    if element in lst_a:
        lst_a.remove(element)
    elif element in lst_b:
        lst_b.remove(element)

    if len(lst_a) < 7 or len(lst_b) < 7:
        break

print(f'Team A - {len(lst_a)}; Team B - {len(lst_b)}')

if len(lst_a) < 7 or len(lst_b) < 7:
    print('Game was terminated')
