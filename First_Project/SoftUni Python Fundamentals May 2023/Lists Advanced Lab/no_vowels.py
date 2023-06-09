word = str(input())

vowels_lst = ['a', 'o', 'u', 'e', 'i']

new_lst = [element for element in word if not element.lower() in vowels_lst]

print("".join(new_lst))

# for element in word:
#     if element.lower() in vowels_lst:
#         continue
#     else:
#         print(element, end='')
