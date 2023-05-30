n = int(input())
word = str(input())
full_lst = []
small_lst = []

for _ in range(n):
    strings = str(input())
    full_lst.append(strings)

    test_lst = strings.split(' ')

    if word in test_lst:
        small_lst.append(strings)

print(full_lst)
print(small_lst)
