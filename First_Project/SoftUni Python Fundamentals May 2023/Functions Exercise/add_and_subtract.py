def sum_numbers(a, b):
    return a + b


def subtract(x, y):
    return x - y


def add_and_subtract(n1, n2, n3):
    sum_first_two = sum_numbers(n1, n2)
    return subtract(sum_first_two, n3)


one, two, three = int(input()), int(input()), int(input())

print(add_and_subtract(one, two, three))
