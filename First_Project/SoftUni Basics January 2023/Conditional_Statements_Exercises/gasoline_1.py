gas_type = str(input())
liters = int(input())

if gas_type == "Diesel" or gas_type == "Gasoline" or gas_type == "Gas":
    if liters < 25:
        print(f'Fill your tank with {gas_type}')
    else:
        print(f'You have enough {gas_type}')
else:
    print('Invalid fuel type!')
