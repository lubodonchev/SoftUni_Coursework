n = int(input())
salary = float(input())
result = None

for _ in range(n):
    if salary <= 0:
        result = "You have lost your salary."
    else:
        site = str(input())
        if site == 'Facebook':
            salary -= 150
        elif site == 'Instagram':
            salary -= 100
        elif site == 'Reddit':
            salary -= 50
        if salary <= 0:
            result = "You have lost your salary."
        else:
            result = f'{salary:.0f}'

print(result)
