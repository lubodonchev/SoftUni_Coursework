start = int(input())
end = int(input())
magic = int(input())

counter = 0
flag = False

for a in range(start, end + 1):
    for b in range(start, end + 1):
        counter += 1
        if a + b == magic:
            flag = True
            print(f'Combination N:{counter} ({a} + {b} = {magic})')
            break
    if flag:
        break
if not flag:
    print(f'{counter} combinations - neither equals {magic}')
