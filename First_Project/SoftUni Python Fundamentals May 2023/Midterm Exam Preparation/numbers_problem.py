int_lst_nums = [int(element) for element in input().split()]

average = sum(int_lst_nums) / len(int_lst_nums)

above_average_lst = list(filter(lambda x: x > average, int_lst_nums))

sorted_lst = sorted(above_average_lst, reverse=True)

for i in range(len(sorted_lst) - 1, 4, -1):
    try:
        sorted_lst.pop(i)
    except IndexError:
        break

if not sorted_lst:
    print('No')
    quit()

str_lst_final = [str(element) for element in sorted_lst]

print(' '.join(str_lst_final))
