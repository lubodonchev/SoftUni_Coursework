command = input()
counter = 1
dic = {}

while True:
    if command == 'stop':
        break
    if command in dic.keys():
        dic[command] += int(input())
    else:
        dic[command] = int(input())
    command = input()

for key, value in dic.items():
    print(f'{key} -> {value}')
