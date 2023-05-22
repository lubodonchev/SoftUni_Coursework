word = str(input())
total = 0

for i in range(len(word)):
    if word[i] == 'a':
        total += 1
    if word[i] == 'e':
        total += 2
    if word[i] == 'i':
        total += 3
    if word[i] == 'o':
        total += 4
    if word[i] == 'u':
        total += 5

print(total)
