happiness_lst = list(map(int, str(input()).split()))
factor = int(input())
factored_happiness_lst = list(map(lambda x: x * factor, happiness_lst))
average = sum(factored_happiness_lst) / len(factored_happiness_lst)
filtered_lst = list(filter(lambda x: x > average, factored_happiness_lst))

if len(filtered_lst) >= len(factored_happiness_lst) / 2:
    print(f'Score: {len(filtered_lst)}/{len(factored_happiness_lst)}. Employees are happy!')
else:
    print(f'Score: {len(filtered_lst)}/{len(factored_happiness_lst)}. Employees are not happy!')
