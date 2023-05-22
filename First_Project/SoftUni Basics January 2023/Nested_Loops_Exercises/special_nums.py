number = int(input())

for n in range(1111, 10000):
    flag = False
    for index, digit in enumerate(str(n)):
        if int(digit) == 0:
            flag = True
            continue
        if number % int(digit) != 0:
            flag = True
            break
    if flag:
        continue
    else:
        print(n, end=" ")

# number = int(input())

# for n in range(1111, 10000):
#     for a in str(n):
#         if int(a) == 0:
#             break
#         if number % int(a) != 0:
#             break
#     else:
#         print(n, end=" ")
