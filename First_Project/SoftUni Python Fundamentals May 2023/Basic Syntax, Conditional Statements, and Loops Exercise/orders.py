n = int(input())
total = 0

for _ in range(n):
    price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not 0.01 <= price <= 100 or not 1 <= days <= 31 or not 1 <= capsules_per_day <= 2000:
        continue

    order_sum = price * days * capsules_per_day

    total += order_sum

    print(f'The price for the coffee is: ${order_sum:.2f}')

print(f'Total: ${total:.2f}')
