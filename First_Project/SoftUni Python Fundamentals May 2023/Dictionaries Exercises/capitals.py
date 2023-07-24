lst_country = input().split(", ")
lst_capital = input().split(", ")

dic = dict(zip(lst_country, lst_capital))

for key, value in dic.items():
    print(f'{key} -> {value}')
