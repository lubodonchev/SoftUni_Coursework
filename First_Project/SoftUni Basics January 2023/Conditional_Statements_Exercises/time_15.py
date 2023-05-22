# hour = int(input())
# minutes = int(input())
#
# minutes += 15
#
# if minutes >= 60:
#     hour += 1
#     minutes -= 60
#     if hour > 23:
#         hour -= 24
#         if minutes < 10:
#             print(f'{hour}:0{minutes}')
#         else:
#             print(f'{hour}:{minutes}')
#     else:
#         if minutes < 10:
#             print(f'{hour}:0{minutes}')
#         else:
#             print(f'{hour}:{minutes}')
# else:
#     print(f'{hour}:{minutes}')

hours = int(input())
minutes = int(input()) + 15

if minutes > 59:
    hours += 1
    minutes -= 60

if hours > 23:
    hours -= 24

print(f'{hours}:{minutes:02d}')
