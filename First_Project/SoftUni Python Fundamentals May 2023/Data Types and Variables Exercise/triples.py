n = int(input())

for i in range(97, 97 + n):
    for c in range(97, 97 + n):
        for u in range(97, 97 + n):
            print(chr(i) + chr(c) + chr(u))
