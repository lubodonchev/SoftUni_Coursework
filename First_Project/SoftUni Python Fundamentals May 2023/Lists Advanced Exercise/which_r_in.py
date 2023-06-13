string_one_lst = input().split(', ')
string_two_lst = input().split(', ')

final_lst = []

for element in string_one_lst:
    for word in string_two_lst:
        if element in word:
            final_lst.append(element)
            break

print(final_lst)
