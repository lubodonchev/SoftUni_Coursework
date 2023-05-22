day = str(input())
price = 0

if day in 'Monday, Tuesday, Friday':
    price = 12
elif day in 'Saturday, Sunday':
    price = 16
elif day in 'Wednesday, Thursday':
    price = 14

print(price)
