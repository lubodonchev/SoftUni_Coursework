n = int(input())

# for a in range(1, n + 1):
#     for _ in range(1, a + 1):
#         print('*', end='')
#     print()
# for a in range(n - 1, -1, -1):
#     for _ in range(a - 1, -1, -1):
#         print('*', end='')
#     print()

for i in range(1, n + 1):
    print(i * '*')
for i in range(n - 1, 0, -1):
    print(i * '*')
