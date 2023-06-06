def even_nums(a):
    if a % 2 == 0:
        return a


numbers_as_str_list = input().split()

numbers_as_int_list = []

for element in numbers_as_str_list:
    numbers_as_int_list.append(int(element))

result = list(filter(even_nums, numbers_as_int_list))

print(result)
