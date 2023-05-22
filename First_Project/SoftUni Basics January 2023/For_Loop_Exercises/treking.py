groups = int(input())
musala, mont, kili, k2, everest = 0, 0, 0, 0, 0
total = 0

for _ in range(groups):
    people_in_current_group = int(input())

    if people_in_current_group < 6:
        musala += people_in_current_group
    elif people_in_current_group < 13:
        mont += people_in_current_group
    elif people_in_current_group < 26:
        kili += people_in_current_group
    elif people_in_current_group < 41:
        k2 += people_in_current_group
    else:
        everest += people_in_current_group

total = musala + mont + kili + k2 + everest

print(f'{musala / total * 100:.2f}%\n{mont / total * 100:.2f}%\n{kili / total * 100:.2f}%\n{k2 / total * 100:.2f}%\n'
      f'{everest / total * 100:.2f}%\n')
