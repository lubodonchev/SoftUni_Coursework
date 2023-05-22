while True:
    command = str(input())

    if command == 'End':
        break
    elif command == 'SoftUni':
        continue

    for ch in command:
        print(2 * ch, end='')
    print()
    