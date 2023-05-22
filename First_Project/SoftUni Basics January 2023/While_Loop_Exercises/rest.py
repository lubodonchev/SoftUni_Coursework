price = float(input())
money = float(input())
spend_counter = 0
total_counter = 0

while True:
    action = str(input())
    amount = float(input())
    
    total_counter += 1

    if action == "spend":
        money -= amount
        if money < 0:
            money = 0
        spend_counter += 1
    elif action == "save":
        money += amount
        spend_counter = 0
    if money >= price:
        print(f"You saved the money for {total_counter} days.")
        break
    if spend_counter == 5:
        print(f"You can't save the money.\n{total_counter}")
        break
