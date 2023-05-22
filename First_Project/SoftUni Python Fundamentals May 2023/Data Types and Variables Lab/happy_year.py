year = int(input())

while True:
    year += 1
    year = str(year)
    lst = []

    for ch in year:
        if ch in lst:
            break
        else:
            lst += ch

    if len(lst) == len(year):
        print(year)
        break

    year = int(year)
