n = int(input())

positive = []
negative = []
sum_of_negatives = 0

for _ in range(n):
    a = int(input())
    if a < 0:
        negative.append(a)
    else:
        positive.append(a)

print(positive)
print(negative)

# unnecessary:
while negative:
    sum_of_negatives += negative[0]
    del negative[0]

print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum_of_negatives}')

# print(f'Sum of negatives: {sum(negative)}')
