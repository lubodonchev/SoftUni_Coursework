# length = int(input())
# width = int(input())
#
# pieces = length * width

pieces = int(input()) * int(input())

total_taken = 0

while total_taken < pieces:
    command = input()
    if command == "STOP":
        print(f'{pieces - total_taken} pieces are left.')
        break
    else:
        total_taken += int(command)
else:
    print(f'No more cake left! You need {total_taken - pieces} pieces more.')
