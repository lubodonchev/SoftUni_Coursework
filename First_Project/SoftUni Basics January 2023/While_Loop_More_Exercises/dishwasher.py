detergent = 750 * int(input())

total_plates, total_pots = 0, 0
counter = 1

while detergent >= 0:
    command = input()
    if command == "End":
        print(f"Detergent was enough!\n{total_plates} dishes and {total_pots} pots were washed.\nLeftover detergent"
              f" {detergent} ml.")
        break

    if counter % 3 != 0:
        total_plates += int(command)
        detergent -= 5 * int(command)
    else:
        total_pots += int(command)
        detergent -= 15 * int(command)

    counter += 1
else:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
