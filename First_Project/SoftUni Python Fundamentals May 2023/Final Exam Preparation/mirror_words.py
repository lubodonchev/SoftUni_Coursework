import re

master_lst = []

text = input()
pair_identifier = r'@[A-Za-z]{3,}@@[A-Za-z]{3,}@|#[A-Za-z]{3,}##[A-Za-z]{3,}#'
valid_pairs = re.findall(pair_identifier, text)

n = len(valid_pairs)

if valid_pairs:
    print(f'{n} word pairs found!')
else:
    print('No word pairs found!')

for element in valid_pairs:
    if '@' in element:
        clean = element.strip('@')
        temp_lst = [element for element in clean.split('@@')]
    else:
        clean = element.strip('#')
        temp_lst = [element for element in clean.split('##')]

    word_one = temp_lst[0]
    word_two = temp_lst[1]

    if word_one == word_two[::-1]:
        master_lst.append(temp_lst)

if master_lst:
    print('The mirror words are:')
    output = []
    for element in master_lst:
        output.append(' <=> '.join(element))
    print(', '.join(output))
else:
    print('No mirror words!')
