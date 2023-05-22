w = float(input())
h = float(input())

n_of_rows = w // 1.2
n_of_seats_per_row = (h - 1) // 0.7

total = n_of_rows * n_of_seats_per_row - 3

print(int(total))
