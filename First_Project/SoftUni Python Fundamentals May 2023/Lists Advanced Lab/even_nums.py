strings_lst = input().split(', ')

int_lst = list(map(int, strings_lst))

result = []

for element in int_lst:
    if element % 2 == 0:
        index = int_lst.index(element)
        if index in result:
            index = int_lst.index(element, index + 1)
        result.append(index)

print(result)
