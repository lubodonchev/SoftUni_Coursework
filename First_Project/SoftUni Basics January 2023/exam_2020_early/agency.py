name = str(input())
adult_tickets = int(input())
kid_tickets = int(input())
adult_price = float(input())
tax = float(input())

kid_price = 0.3 * adult_price

profit = 0.2 * (adult_tickets * (adult_price + tax) + (kid_price + tax) * kid_tickets)

print(f'The profit of your agency from {name} tickets is {profit:.2f} lv.')
