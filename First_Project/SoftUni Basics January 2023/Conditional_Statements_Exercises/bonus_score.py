a = int(input())
bonus = 0

if a <= 100:
    bonus = 5
elif a <= 1000:
    bonus = 0.2 * a
else:
    bonus = 0.1 * a

if a % 2 == 0:
    bonus += 1
elif a % 10 == 5:
    bonus += 2

print(bonus)
print(a + bonus)
