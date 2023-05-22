n = int(input())

outer = ''

for _ in range(n - 2):
    outer += '- '

print('+ ' + outer + '+ ')

for _ in range(n-2):
    print('| ' + outer + '|')

print('+ ' + outer + '+ ')
