trip_price = float(input())
puzzle_amount = int(input())
doll_amount = int(input())
bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())
difference = 0

PUZZLE_PRICE = 2.6
DOLL_PRICE = 3
BEAR_PRICE = 4.1
MINION_PRICE = 8.2
TRUCK_PRICE = 2

total_income = puzzle_amount * PUZZLE_PRICE + doll_amount * DOLL_PRICE + bear_amount * BEAR_PRICE + minion_amount * \
               MINION_PRICE + truck_amount * TRUCK_PRICE

total_amount = puzzle_amount + doll_amount + bear_amount + minion_amount + truck_amount

if total_amount >= 50:
    total_income *= 0.75

total_income *= 0.9

difference = abs(trip_price - total_income)

if total_income >= trip_price:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')
