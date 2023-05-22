days = int(input())
win_day_counter, money = 0, 0

for _ in range(days):
    win_count, lose_count, money_today = 0, 0, 0
    while True:
        sport = str(input())
        if sport == "Finish":
            break
        result = str(input())
        if result == "win":
            money_today += 20
            win_count += 1
        elif result == "lose":
            lose_count += 1
    if win_count > lose_count:
        money_today *= 1.1
        win_day_counter += 1
    money += money_today
if win_day_counter > days / 2:
    money *= 1.2
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")
