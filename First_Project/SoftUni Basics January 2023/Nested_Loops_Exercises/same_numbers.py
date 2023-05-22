a, b = int(input()), int(input())

for i in range(a, b + 1):
    # i = str(i)
    odd_sum, even_sum = 0, 0
    # for n in range(0, 6, 2):
    #     odd_sum += int(i[n])
    # for k in range(1, 6, 2):
    #     even_sum += int(i[k])
    # if even_sum == odd_sum:
    #     print(i, end=" ")
    for index, digit in enumerate(str(i)):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(i, end=" ")
