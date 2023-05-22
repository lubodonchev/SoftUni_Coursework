days = int(input())
accommodation = str(input())
review = str(input())
result = None

nights = days - 1
room = 18 * nights

if nights < 9:
    apartment = 25 * nights * 0.7
    president = 35 * nights * 0.9
elif nights <= 14:
    apartment = 25 * nights * 0.65
    president = 35 * nights * 0.85
else:
    apartment = 25 * nights * 0.5
    president = 35 * nights * 0.8

if review == "positive":
    room *= 1.25
    apartment *= 1.25
    president *= 1.25
elif review == "negative":
    room *= 0.9
    apartment *= 0.9
    president *= 0.9

if accommodation == "room for one person":
    result = room
elif accommodation == "apartment":
    result = apartment
elif accommodation == "president apartment":
    result = president

print(f"{result:.2f}")
