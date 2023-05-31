numbers = str(input())
n = int(input())

new_lst = []
final_lst = []

a, counter = 0, 0

initial_lst = numbers.split(' ')


for element in initial_lst:
    new_lst.append(int(element))

for _ in range(n):
    new_lst.remove(min(new_lst))

for element in new_lst:
    final_lst.append(str(element))

print(', '.join(final_lst))
