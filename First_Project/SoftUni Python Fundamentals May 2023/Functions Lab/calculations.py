def calculator():
    operator = str(input())
    a = int(input())
    b = int(input())

    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        if b != 0:
            return int(a / b)
        else:
            return 'Error!'
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
    else:
        return 'Error!'


print(calculator())
