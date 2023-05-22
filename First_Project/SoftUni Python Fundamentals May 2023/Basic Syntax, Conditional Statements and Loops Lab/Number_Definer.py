a = float(input())

if a == 0:
    print('zero')
elif abs(a) < 1:
    print('small', end=' ')
elif abs(a) > 1000000:
    print('large', end=' ')

if a > 0:
    print('positive')
elif a < 0:
    print('negative')
