budget = float(input())
season = str(input())
destination = None
rest = None
spend = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spend = 0.3 * budget
        rest = "Camp"
    elif season == "winter":
        spend = 0.7 * budget
        rest = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spend = 0.4 * budget
        rest = "Camp"
    elif season == "winter":
        spend = 0.8 * budget
        rest = "Hotel"
elif budget > 1000:
    destination = "Europe"
    spend = 0.9 * budget
    rest = "Hotel"

print(f"Somewhere in {destination}")
print(f"{rest} - {spend:.2f}")
