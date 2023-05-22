temp = int(input())
time = str(input())

outfit = 0
shoes = 0

# outfit = None
# shoes = None

if time == "Morning":
    if 10 <= temp <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < temp <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif temp >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time == "Afternoon":
    if 10 <= temp <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < temp <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif temp >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif time == "Evening":
    if 10 <= temp <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < temp <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif temp >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {temp} degrees, get your {outfit} and {shoes}.")
