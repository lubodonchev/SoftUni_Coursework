a = str(input())

final_lst = []

initial_lst = a.split(' ')

for element in initial_lst:
    number = int(element) * -1
    final_lst.append(number)

print(final_lst)
