deposit_amount = float(input())
time = int(input())
percentage = float(input()) / 100

amount = deposit_amount + time * ((deposit_amount * percentage) / 12)

print(amount)
