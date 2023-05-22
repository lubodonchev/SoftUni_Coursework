month = str(input())
nights = int(input())

studio = None
apartment = None

if month == "May" or month == "October":
    studio = 50 * nights
    if nights > 14:
        studio *= 0.7
    elif nights > 7:
        studio *= 0.95
    apartment = 65 * nights
elif month == "June" or month == "September":
    studio = 75.2 * nights
    if nights > 14:
        studio *= 0.8
    apartment = 68.7 * nights
elif month == "July" or month == "August":
    studio = 76 * nights
    apartment = 77 * nights

if nights > 14:
    apartment *= 0.9

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
