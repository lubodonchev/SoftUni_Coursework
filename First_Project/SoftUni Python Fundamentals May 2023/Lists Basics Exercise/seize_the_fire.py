def validity_check(lst):
    if lst[0] == 'High' and int(lst[1]) in range(81, 126) or \
            lst[0] == 'Medium' and int(lst[1]) in range(51, 81) or \
            lst[0] == 'Low' and int(lst[1]) in range(1, 51):
        return True


fire_lst = input().split('#')
water = int(input())
effort = 0
final_lst = []


for element in fire_lst:
    individual_lst = element.split(' = ')
    if validity_check(individual_lst):
        if water < int(individual_lst[1]):
            continue
        else:
            water -= int(individual_lst[1])
            effort += 0.25 * int(individual_lst[1])
            final_lst.append(int(individual_lst[1]))

print('Cells:')
for element in final_lst:
    print(f'- {element}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(final_lst)}')
