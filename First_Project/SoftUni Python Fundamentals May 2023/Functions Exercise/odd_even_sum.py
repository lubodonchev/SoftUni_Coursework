def calculator(a: str):
    even_sum, odd_sum = 0, 0
    for i in range(len(a)):
        current_num = int(a[i])
        if current_num % 2 == 0:
            even_sum += current_num
        else:
            odd_sum += current_num
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


n = str(input())
print(calculator(n))
