people_waiting = int(input())
int_lift_lst = [int(element) for element in input().split()]
result = ''

for i in range(len(int_lift_lst)):

    initial_people = int_lift_lst[i]

    if int_lift_lst[i] == 4:
        continue

    if people_waiting >= 4 - initial_people:
        int_lift_lst[i] += 4 - initial_people
        people_waiting -= int_lift_lst[i] - initial_people

    else:
        int_lift_lst[i] += people_waiting
        people_waiting = 0

    if people_waiting == 0 and int_lift_lst.count(4) == len(int_lift_lst):
        str_lift_lst = [str(element) for element in int_lift_lst]
        print(' '.join(str_lift_lst))
        break
    elif people_waiting == 0:
        str_lift_lst = [str(element) for element in int_lift_lst]
        print('The lift has empty spots!')
        print(' '.join(str_lift_lst))
        break
    elif people_waiting > 0 and int_lift_lst.count(4) == len(int_lift_lst):
        str_lift_lst = [str(element) for element in int_lift_lst]
        print(f'There isn\'t enough space! {people_waiting} people in a queue!')
        print(' '.join(str_lift_lst))
        break
