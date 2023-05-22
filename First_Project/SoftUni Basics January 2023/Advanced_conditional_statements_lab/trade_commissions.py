city = str(input())
sales = float(input())
commissions = 0
correct_data = True

if city == "Sofia":
    if 0 <= sales <= 500:
        commissions = sales * 0.05
    elif 500 < sales <= 1000:
        commissions = sales * 0.07
    elif 1000 < sales <= 10000:
        commissions = sales * 0.08
    elif sales > 10000:
        commissions = sales * 0.12
    else:
        correct_data = False
elif city == "Varna":
    if 0 <= sales <= 500:
        commissions = sales * 0.045
    elif 500 < sales <= 1000:
        commissions = sales * 0.075
    elif 1000 < sales <= 10000:
        commissions = sales * 0.1
    elif sales > 10000:
        commissions = sales * 0.13
    else:
        correct_data = False
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commissions = sales * 0.055
    elif 500 < sales <= 1000:
        commissions = sales * 0.08
    elif 1000 < sales <= 10000:
        commissions = sales * 0.12
    elif sales > 10000:
        commissions = sales * 0.145
    else:
        correct_data = False
else:
    correct_data = False

if correct_data:
    print(f'{commissions:.2f}')
else:
    print('error')

