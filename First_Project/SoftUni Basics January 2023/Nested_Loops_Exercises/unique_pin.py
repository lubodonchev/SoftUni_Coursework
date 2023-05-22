max_n1 = int(input())
max_n2 = int(input())
max_n3 = int(input())

for n1 in range(2, max_n1 + 1):
    if n1 % 2 != 0:
        continue
    for n2 in range(2, max_n2 + 1):
        flag = False
        if n2 > 7:
            continue
        for i in range(2, n2):
            if n2 % i == 0:
                flag = True
                break
        if flag:
            continue
        for n3 in range(2, max_n3 + 1):
            if n3 % 2 != 0:
                continue
            print(f'{n1} {n2} {n3}')
