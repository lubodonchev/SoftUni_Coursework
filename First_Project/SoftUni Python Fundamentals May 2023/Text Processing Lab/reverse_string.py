while True:
    data = str(input())
    reverse = ''
    if data == 'end':
        quit()
    for i in range(len(data) - 1, -1, -1):
        reverse += data[i]
    print(f'{data} = {reverse}')

# print(f'{data[::-1]}')