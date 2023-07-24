import re

lst = []
total = 0

while True:
    text = input()

    if text == 'Purchase':
        break

    valid_finder = r'>>[A-Za-z\s]+<<\d+\.?\d*!\d+'
    valid_input = re.findall(valid_finder, text)

    for element in valid_input:
        name_finder = r'[A-Za-z\s]+'
        names = re.findall(name_finder, element)
        for name in names:
            lst.append(name)

        num_find = r'[0-9\.]+'
        nums = re.findall(num_find, element)
        total += float(nums[0]) * float(nums[1])

print('Bought furniture:')
for element in lst:
    print(element)
print(f'Total money spend: {total:.2f}')
