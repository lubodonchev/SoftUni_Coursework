counter = 0

while True:
    command = str(input())

    if command == 'END':
        break

    if command in ['coding', 'dog', 'cat', 'movie']:
        counter += 1
    elif command in ['CODING', 'DOG', 'CAT', 'MOVIE']:
        counter += 2
    else:
        continue

if counter > 5:
    print('You need extra sleep')
else:
    print(counter)
