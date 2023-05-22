n = int(input())

valid = 100 <= n <= 200 or n == 0

if not valid:
    print('invalid')
