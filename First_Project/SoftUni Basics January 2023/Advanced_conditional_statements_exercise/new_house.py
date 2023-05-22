type_flower = str(input())
quantity_flower = int(input())
budget = int(input())
total = 0

ROSE = 5
DAHLIA = 3.8
TULIP = 2.8
NARCISSUS = 3
GLADIOLUS = 2.5

if type_flower == "Roses":
    if quantity_flower > 80:
        total = 0.9 * quantity_flower * ROSE
    else:
        total = quantity_flower * ROSE
elif type_flower == "Dahlias":
    if quantity_flower > 90:
        total = 0.85 * quantity_flower * DAHLIA
    else:
        total = quantity_flower * DAHLIA
elif type_flower == "Tulips":
    if quantity_flower > 80:
        total = 0.85 * quantity_flower * TULIP
    else:
        total = quantity_flower * TULIP
elif type_flower == "Narcissus":
    if quantity_flower < 120:
        total = 1.15 * quantity_flower * NARCISSUS
    else:
        total = quantity_flower * NARCISSUS
elif type_flower == "Gladiolus":
    if quantity_flower < 80:
        total = 1.2 * quantity_flower * GLADIOLUS
    else:
        total = quantity_flower * GLADIOLUS

if budget >= total:
    print(f"Hey, you have a great garden with {quantity_flower} {type_flower} and {budget - total:.2f} leva left.")
else:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")
