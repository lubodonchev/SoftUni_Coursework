n = int(input())

for i in range(n):
    a = int(input())
    if a % 2 != 0:
        print(f"{a} is odd!")
        break
else:
    print("All numbers are even.")
