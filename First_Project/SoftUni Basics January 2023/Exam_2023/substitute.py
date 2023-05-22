k = int(input())
el = int(input())
m = int(input())
n = int(input())

num1, num2 = 0, 0

counter = 0
flag = False
test = False

while True:
    for a in range(k, 9):
        if counter == 6:
            flag = True
            break
        if a % 2 != 0:
            continue
        for b in range(9, el - 1, -1):
            if b % 2 == 0:
                continue
            num1 = f'{a}{b}'

            for c in range(m, 9):
                if c % 2 != 0:
                    continue
                for d in range(9, n - 1, -1):
                    if d % 2 == 0:
                        continue
                    num2 = f'{c}{d}'

                    if int(num1) == int(num2):
                        print("Cannot change the same player.")
                    else:
                        print(f"{num1} - {num2}")
                        counter += 1
        test = True
    if flag or test:
        break
