amount = float(input())

counter = 0
domain = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]

while amount != 0:
    for i in range(7, -1, -1):
        test = domain[i]
        while test <= round(amount, 2):
            amount = round(amount, 2)
            amount -= test
            counter += 1
else:
    print(counter)
