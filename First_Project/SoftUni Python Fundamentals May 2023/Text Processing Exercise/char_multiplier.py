data = input().split()
word_one = []
word_two = []
total = 0

for ch in data[0]:
    word_one.append(ord(ch))
for ch in data[1]:
    word_two.append(ord(ch))

if len(word_one) < len(word_two):
    for i in range(len(word_one)):
        total += word_one[i] * word_two[i]
    for i in range(len(word_one), len(word_two)):
        total += word_two[i]
else:
    for i in range(len(word_two)):
        total += word_two[i] * word_one[i]
    for i in range(len(word_two), len(word_one)):
        total += word_one[i]

print(total)
