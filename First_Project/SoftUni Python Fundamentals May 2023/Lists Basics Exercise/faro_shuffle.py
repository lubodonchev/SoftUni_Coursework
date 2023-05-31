cards = str(input())
count = int(input())

lst_cards = cards.split(' ')

for _ in range(count):
    lst_a = []
    lst_b = []
    new_final_lst = []

    for i in range(len(lst_cards)):
        if i < len(lst_cards)/2:
            lst_a.append(lst_cards[i])
        else:
            lst_b.append(lst_cards[i])

    for i in range(len(lst_a)):
        new_final_lst.append(lst_a[i])
        new_final_lst.append(lst_b[i])

    lst_cards = new_final_lst

print(lst_cards)
