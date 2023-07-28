import re

n = int(input())
valid_checker = r'^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$'
digit_checker = r'\d'

for _ in range(n):
    text = input()
    valid_lst = re.findall(valid_checker, text)
    if not valid_lst:
        print('Invalid barcode')
    else:
        for element in valid_lst:
            product_group = ''
            digit_lst = re.findall(digit_checker, element)
            if digit_lst:
                for num in digit_lst:
                    product_group += num
            else:
                product_group = '00'
            print(f'Product group: {product_group}')
