from sys import maxsize

lines = int(input())
preliminary = 0
biggest = - maxsize

for i in range(lines):
    current_number = int(input())
    if current_number > biggest:
        biggest = current_number
    preliminary += current_number

total = preliminary - biggest

if biggest == total:
    print(f'Yes\nSum = {biggest}')
else:
    print(f'No\nDiff = {abs(biggest - total)}')
