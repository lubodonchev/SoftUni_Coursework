lst = [element for element in input().split(', ')]

dic = {letter: ord(letter) for letter in lst}

print(dic)
