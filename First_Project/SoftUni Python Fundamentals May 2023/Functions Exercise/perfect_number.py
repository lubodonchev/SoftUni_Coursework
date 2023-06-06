def perfect_checker(a):
    lst = []

    flag = False

    for i in range(1, a):
        if a % i == 0:
            lst.append(i)

    if a == sum(lst):
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


num = int(input())

perfect_checker(num)
