lst = input().split()

keys = [element for element in lst if (lst.index(element) + 1) % 2 != 0]
values = [int(element) for element in lst if (lst.index(element) + 1) % 2 == 0]

final = dict(zip(keys, values))

query_lst = input().split()

for element in query_lst:
    if element in final.keys() and final[element] > 0:
        print(f'We have {final[element]} of {element} left')
    else:
        print(f'Sorry, we don\'t have {element}')
