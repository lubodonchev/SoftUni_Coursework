a = int(input())
b = int(input())
c = int(input())

# a, b, c = int(input()), int(input()), int(input())

if a > b and a > c:
    result = a
elif b > a and b > c:
    result = b
else:
    result = c

print(result)

# print(max(a, b, c))
