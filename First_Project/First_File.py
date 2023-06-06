# def even(a):
#     if a % 2 == 0:
#         return a
#
#
# numbers = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
#
# result = filter(even, numbers)
# result = list(result)
#
# print(result)

# print([int(number) for number in input().split() if int(number) % 2 == 0])


# def even(a):
#     if a % 2 == 0:
#         return a
#
#
# scores = [1, 2, 3, 4, 5]
#
# filtered = filter(even, scores)
# print(list(filtered))

# lst = [0]
#
# print(list(lst))

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

# the lambda function returns True for even numbers
even_numbers_iterator = filter(lambda x: (x % 2 == 0), numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)
