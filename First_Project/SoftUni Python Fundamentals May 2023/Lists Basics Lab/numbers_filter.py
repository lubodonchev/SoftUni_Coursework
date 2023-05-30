n = int(input())

full_lst = []
final_lst = []

for _ in range(n):
    a = int(input())
    full_lst.append(a)

command = str(input())

if command == 'even':
    for i in full_lst:
        if i % 2 == 0:
            final_lst.append(i)
elif command == 'odd':
    for i in full_lst:
        if i % 2 != 0:
            final_lst.append(i)
elif command == 'negative':
    for i in full_lst:
        if i < 0:
            final_lst.append(i)
elif command == 'positive':
    for i in full_lst:
        if i >= 0:
            final_lst.append(i)

print(final_lst)
