initial_lst = input().split()
final_lst = []

for element in initial_lst:
    current_lst = [ch for ch in element]
    ascii_lst = list(filter(lambda x: x.isnumeric(), current_lst))
    first_letter = chr(int(''.join(ascii_lst)))

    word_lst = [first_letter]
    for n in current_lst:
        if not n.isnumeric():
            word_lst.append(n)

    word_lst[1], word_lst[-1] = word_lst[-1], word_lst[1]

    final_lst.append(''.join(word_lst))

print(' '.join(final_lst))
