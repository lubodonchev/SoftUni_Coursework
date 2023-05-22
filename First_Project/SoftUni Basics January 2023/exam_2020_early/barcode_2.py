mini = int(input())
maxi = int(input())

for i in range(mini, maxi + 1):
    flag = True
    i = str(i)
    mini = str(mini)
    maxi = str(maxi)

    for n in range(4):
        if int(i[n]) > int(maxi[n]) or int(i[n]) < int(mini[n]):
            flag = False

        if int(i[n]) % 2 == 0:
            flag = False

    if flag:
        print(i, end=" ")
