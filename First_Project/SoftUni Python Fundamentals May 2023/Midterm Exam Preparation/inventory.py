def collect(lst, item):
    if item not in lst:
        lst.append(item)
    return lst


def drop(lst, item):
    if item in lst:
        lst.remove(item)
    return lst


def combine(lst, command):
    temporary_lst = command.split(':')
    if temporary_lst[0] in lst:
        lst.insert(lst.index(temporary_lst[0]) + 1, temporary_lst[1])
    return lst


def renew(lst, item):
    if item in lst:
        lst.remove(item)
        lst.append(item)
    return lst


journal_lst = input().split(', ')

while True:
    prompt_lst = input().split(' - ')
    if prompt_lst[0] == 'Craft!':
        break
    elif prompt_lst[0] == 'Collect':
        journal_lst = collect(journal_lst, prompt_lst[1])
    elif prompt_lst[0] == 'Drop':
        journal_lst = drop(journal_lst, prompt_lst[1])
    elif prompt_lst[0] == 'Combine Items':
        journal_lst = combine(journal_lst, prompt_lst[1])
    elif prompt_lst[0] == 'Renew':
        journal_lst = renew(journal_lst, prompt_lst[1])

print(*journal_lst, sep=', ')
