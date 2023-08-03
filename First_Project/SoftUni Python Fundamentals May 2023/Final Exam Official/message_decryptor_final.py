import re

n = int(input())
validity_checker = r'^(\$|%)[A-Z][a-z]{2,}\1: \[\d+\]\|\[\d+\]\|\[\d+\]\|$'
valid_lst = []

for _ in range(n):
    valid_lst = []
    text = input()
    matches = re.finditer(validity_checker, text)

    for match in matches:
        valid_lst.append(match.group())

    if valid_lst:
        for element in valid_lst:
            element_lst = element.split(': ')
            if '$' in element_lst[0]:
                tag = element_lst[0].strip('$')
            else:
                tag = element_lst[0].strip('%')
            numbers = element_lst[1]
            numbers_lst = element_lst[1].split(']|[')
            n1 = numbers_lst[0]
            n1_lst = [r for r in numbers_lst[0] if r.isdigit()]
            final_n1 = ''.join(n1_lst)
            ascii_n1 = chr(int(final_n1))
            n2 = numbers_lst[1]
            n2_lst = [r for r in numbers_lst[1] if r.isdigit()]
            final_n2 = ''.join(n2_lst)
            ascii_n2 = chr(int(final_n2))
            n3 = numbers_lst[2]
            n3_lst = [r for r in numbers_lst[2] if r.isdigit()]
            final_n3 = ''.join(n3_lst)
            ascii_n3 = chr(int(final_n3))
            print(f'{tag}: {ascii_n1}{ascii_n2}{ascii_n3}')
    else:
        print('Valid message not found!')


