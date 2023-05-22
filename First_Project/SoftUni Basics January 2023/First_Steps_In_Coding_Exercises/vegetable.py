n = float(input())
m = float(input())
veg_kg = float(input())
fru_kg = float(input())

total = (n * veg_kg + m * fru_kg) / 1.94

print("%.2f" % total)
