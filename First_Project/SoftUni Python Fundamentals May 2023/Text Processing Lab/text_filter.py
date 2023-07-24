banned_lst = input().split(', ')
text = input()

for element in banned_lst:
    text = text.replace(element, '*' * len(element))

print(text)
