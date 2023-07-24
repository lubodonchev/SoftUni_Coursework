data = input().split(', ')
invalid_lst = []

for element in data:
    if len(element) < 3 or len(element) > 16:
        invalid_lst.append(element)

for element in data:
    if element not in invalid_lst:
        for ch in element:
            if not ch.isalnum() and not ch == '-' and not ch == '_':
                invalid_lst.append(element)
                break

for element in data:
    if element not in invalid_lst:
        print(element)
