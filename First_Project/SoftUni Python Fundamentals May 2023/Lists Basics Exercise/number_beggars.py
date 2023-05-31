givings = str(input())
beggars = int(input())

final_lst = []
givings_int = []

lst_givings = givings.split(', ')

for element in lst_givings:
    givings_int.append(int(element))

counter = 0

while counter < beggars:
    sum_current_beggar = 0
    for i in range(counter, len(givings_int), beggars):
        sum_current_beggar += givings_int[i]
    final_lst.append(sum_current_beggar)
    counter += 1

print(final_lst)
