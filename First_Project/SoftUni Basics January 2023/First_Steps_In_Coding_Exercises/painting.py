nylon = int(input())
paint = int(input())
liquid = int(input())
man_hours = int(input())

amount = ((nylon + 2) * 1.5 + 1.1 * paint * 14.5 + liquid * 5 + 0.4) * (1 + man_hours * 0.3)

print(amount)
