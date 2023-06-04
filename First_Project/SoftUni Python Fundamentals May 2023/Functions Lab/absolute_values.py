lst = input().split()

new_lst = []

for n in lst:
    new_lst.append(abs(float(n)))

print(new_lst)
