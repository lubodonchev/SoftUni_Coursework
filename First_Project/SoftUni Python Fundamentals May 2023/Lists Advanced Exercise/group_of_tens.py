str_initial_lst = input().split(', ')
int_initial_lst = list(map(int, str_initial_lst))

max_group = max(int_initial_lst) // 10 + 1

for i in range(1, max_group + 1):
    current_lst = list(filter(lambda x: 10 * (i - 1) < x <= 10 * i, int_initial_lst))
    if i == max_group and current_lst == []:
        break
    print(f'Group of {10 * i}\'s: {current_lst}')
