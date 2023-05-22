# V1: version without uniqueness check
#
# word1 = str(input())
# word2 = str(input())
#
# for a in range(len(word1) - 1):
#     for ch in range(0, a + 1):
#         print(word2[ch], end='')
#     for sh in range(ch + 1, len(word1)):
#         print(word1[sh], end='')
#     print()
#
# V2: final version
#
# word1 = str(input())
# word2 = str(input())
#
# old = word1
#
# for a in range(len(word1) - 1):
#     new = ''
#     for ch in range(0, a + 1):
#         new += f'{word2[ch]}'
#     for sh in range(ch + 1, len(word1)):
#         new += f'{word1[sh]}'
#     if new == old:
#         continue
#     print(new)
#     old = new
# if old != word2:
#     print(f'{word2}')
#
# V3 tutor's version:

word1 = str(input())
word2 = str(input())

old = word1

for a in range(len(word1)):
    left_part = word2[:a + 1]
    right_part = word1[a + 1:]
    new = left_part + right_part

    if new == old:
        continue

    print(new)
    old = new
