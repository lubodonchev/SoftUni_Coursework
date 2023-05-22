balance = 0

while True:
    current_sum = input()

    if current_sum == "NoMoreMoney":
        break

    current_sum = float(current_sum)

    if current_sum >= 0:
        print(f'Increase: {current_sum:.2f}')
        balance += current_sum
    else:
        print("Invalid operation!")
        break
print(f'Total: {balance:.2f}')
