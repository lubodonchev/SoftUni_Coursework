int_lst = [int(element) for element in input().split(', ')]

positive_lst = [str(element) for element in int_lst if element >= 0]
negative_lst = [str(element) for element in int_lst if element < 0]
even_lst = [str(element) for element in int_lst if element % 2 == 0]
odd_lst = [str(element) for element in int_lst if element % 2 != 0]

positive_str = ", ".join(positive_lst)
negative_str = ", ".join(negative_lst)
even_str = ", ".join(even_lst)
odd_str = ", ".join(odd_lst)

print(f'Positive: {positive_str}')
print(f'Negative: {negative_str}')
print(f'Even: {even_str}')
print(f'Odd: {odd_str}')
