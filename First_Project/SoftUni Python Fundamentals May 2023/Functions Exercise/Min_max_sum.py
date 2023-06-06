initial_list = input().split()

final_list = []

for element in initial_list:
    final_list.append(int(element))

print(f'The minimum number is {min(final_list)}\n'
      f'The maximum number is {max(final_list)}\n'
      f'The sum number is: {sum(final_list)}')
