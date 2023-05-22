# prime_sum, composite_sum = 0, 0
#
# while True:
#     n = input()
#
#     if n == "stop":
#         print(f'Sum of all prime numbers is: {prime_sum}\nSum of all non prime numbers is: {composite_sum}')
#         break
#
#     n = int(n)
#
#     if n < 0:
#         print('Number is negative.')
#         continue
#
#     if (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0) and n != 1 and n != 2 and n != 3 and n != 5 and n != 7:
#         composite_sum += n
#     else:
#         prime_sum += n

prime_sum, composite_sum = 0, 0
is_prime = True

while True:
    n = input()

    if n == "stop":
        print(f'Sum of all prime numbers is: {prime_sum}\nSum of all non prime numbers is: {composite_sum}')
        break

    n = int(n)

    if n < 0:
        print('Number is negative.')
        continue

    for a in range(2, n):
        if n % a == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += n
    else:
        composite_sum += n
