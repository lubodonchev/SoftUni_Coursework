factor = int(input())
count = int(input())

new_multiple = 2

lst = [factor]

for _ in range(count - 1):
    new_number = new_multiple * factor
    lst.append(new_number)
    new_multiple += 1

print(lst)
