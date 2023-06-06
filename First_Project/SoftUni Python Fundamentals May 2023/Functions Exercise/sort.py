initial_list = input().split()

final_list = []

for element in initial_list:
    final_list.append(int(element))

result = sorted(final_list)

print(result)
