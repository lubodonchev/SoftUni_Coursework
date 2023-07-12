lst = input().split()

keys = [element for element in lst if (lst.index(element) + 1) % 2 != 0]
values = [int(element) for element in lst if (lst.index(element) + 1) % 2 == 0]

final = dict(zip(keys, values))

print(final)
