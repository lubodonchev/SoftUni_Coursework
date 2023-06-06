def chars(a, b):
    a_ascii = ord(a)
    b_ascii = ord(b)
    for i in range(a_ascii + 1, b_ascii):
        print(chr(i), end=' ')


first, second = str(input()), str(input())

chars(first, second)
