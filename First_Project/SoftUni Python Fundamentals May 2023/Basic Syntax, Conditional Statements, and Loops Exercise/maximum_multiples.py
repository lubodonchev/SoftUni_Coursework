# a, b = int(input()), int(input())
# highest = 0
#
# for i in range(b + 1):
#     if i % a == 0:
#         highest = i
#
# print(highest)

a, b = int(input()), int(input())
i = 0

for i in range(b, a - 1, - 1):
    if i % a == 0:
        break

print(i)
