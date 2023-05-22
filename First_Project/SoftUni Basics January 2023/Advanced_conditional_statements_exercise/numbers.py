n1 = int(input())
n2 = int(input())
operator1 = input()

result = 0

if (operator1 == "/" or operator1 == "%") and n2 == 0:
    print(f"Cannot divide {n1} by zero")
else:
    if operator1 == "+":
        result = n1 + n2
    elif operator1 == "-":
        result = n1 - n2
    elif operator1 == "*":
        result = n1 * n2
    elif operator1 == "/":
        result = n1 / n2
    elif operator1 == "%":
        result = n1 % n2

    if operator1 == "+" or operator1 == "-" or operator1 == "*":
        if result % 2 == 0:
            print(f"{n1} {operator1} {n2} = {result} - even")
        else:
            print(f"{n1} {operator1} {n2} = {result} - odd")
    elif operator1 == "%":
        print(f"{n1} % {n2} = {n1 % n2}")
    elif operator1 == "/":
        print(f"{n1} / {n2} = {result:.2f}")
