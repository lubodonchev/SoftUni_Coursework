floors = int(input())
rooms = int(input())

result = ""

for i in range(floors, 0, -1):
    for z in range(rooms):
        if i == floors:
            result = f'L{i}{z}'
        elif i % 2 == 0:
            result = f'O{i}{z}'
        else:
            result = f'A{i}{z}'
        print(result, end=" ")
    print()
