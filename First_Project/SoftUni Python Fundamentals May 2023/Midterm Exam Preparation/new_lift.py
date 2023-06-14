#doesn't work; other solution is final

# people_waiting = int(input())
# int_lift_lst = [int(element) for element in input().split()]
# counter = 0
# result = ''
#
# while True:
#     if counter == len(int_lift_lst):
#         counter = 0
#         continue
#
#     if int_lift_lst[counter] == 4:
#         counter += 1
#         continue
#
#     int_lift_lst[counter] += 1
#     people_waiting -= 1
#
#     counter += 1
#
#     if people_waiting == 0 and int_lift_lst.count(4) == len(int_lift_lst):
#         str_lift_lst = [str(element) for element in int_lift_lst]
#         print(' '.join(str_lift_lst))
#         break
#     elif people_waiting == 0:
#         str_lift_lst = [str(element) for element in int_lift_lst]
#         print('The lift has empty spots!')
#         print(' '.join(str_lift_lst))
#         break
#     elif people_waiting > 0 and int_lift_lst.count(4) == len(int_lift_lst):
#         str_lift_lst = [str(element) for element in int_lift_lst]
#         print(f'There isn\'t enough space! {people_waiting} people in a queue!')
#         print(' '.join(str_lift_lst))
#         break
