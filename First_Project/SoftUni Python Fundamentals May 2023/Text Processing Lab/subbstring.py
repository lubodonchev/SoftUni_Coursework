remover = str(input())
word = str(input())

while remover in word:
    word = word.replace(remover, '')

print(word)
