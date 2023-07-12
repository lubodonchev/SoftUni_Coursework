lst = [element.lower() for element in input().split()]
excluded = []

for element in lst:
    if element not in excluded:
        if lst.count(element) % 2 != 0:
            print(element, end=' ')
        excluded.append(element)
