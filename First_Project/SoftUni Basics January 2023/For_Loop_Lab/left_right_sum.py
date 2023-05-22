lines = int(input()) * 2
left = 0
right = 0

for i in range(lines):
    current_number = int(input())

    if i <= lines / 2 - 1:
        left += current_number
    else:
        right += current_number

if left == right:
    print(f'Yes, sum = {left}')
else:
    print(f'No, diff = {abs(left - right)}')
