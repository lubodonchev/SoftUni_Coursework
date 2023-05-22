days = int(input())
room = str(input())
review = str(input())

total = 0

if room == "room for one person":
    total = (days - 1) * 18
elif room == "apartment":
    total = (days - 1) * 25
    if days < 10:
        total *= 0.7
    elif days < 16:
        total *= 0.65
    else:
        total *= 0.5
elif room == "president apartment":
    total = (days - 1) * 35
    if days < 10:
        total *= 0.9
    elif days < 16:
        total *= 0.85
    else:
        total *= 0.8

if review == "positive":
    total *= 1.25
else:
    total *= 0.9

print(f'{total:.2f}')
