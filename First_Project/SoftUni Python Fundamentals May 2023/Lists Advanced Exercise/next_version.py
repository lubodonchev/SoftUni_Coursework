str_initial_version_lst = input().split('.')

int_initial_version_lst = list(map(int, str_initial_version_lst))

int_initial_version_lst[-1] += 1

if int_initial_version_lst[-1] == 10:
    int_initial_version_lst[-1] = 0
    int_initial_version_lst[-2] += 1
    if int_initial_version_lst[-2] == 10:
        int_initial_version_lst[-2] = 0
        int_initial_version_lst[-3] += 1

str_final_version_lst = list(map(str, int_initial_version_lst))

final_version = ".".join(str_final_version_lst)

print(final_version)
