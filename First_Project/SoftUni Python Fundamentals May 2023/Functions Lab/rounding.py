def rounding():
    numbers = str(input())
    lst = numbers.split()

    n_lst = []
    f_lst = []

    for element in lst:
        n_lst.append(float(element))

    for element in n_lst:
        f_lst.append(round(element))

    print(f_lst)


rounding()
