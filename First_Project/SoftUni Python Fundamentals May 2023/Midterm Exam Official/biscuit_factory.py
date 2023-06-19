from math import floor

biscuits_per_day_per_worker = int(input())
workers = int(input())
competitor_biscuits_per_month = int(input())
total_production = 0

for i in range(1, 31):
    capacity = biscuits_per_day_per_worker * workers
    if i % 3 == 0:
        capacity = floor(capacity * 0.75)
    total_production += capacity

print(f'You have produced {total_production} biscuits for the past month.')

if total_production > competitor_biscuits_per_month:
    print(f'You produce {(total_production - competitor_biscuits_per_month)/competitor_biscuits_per_month * 100:.2f}'
          f' percent more biscuits.')
else:
    print(f'You produce {-(total_production - competitor_biscuits_per_month)/competitor_biscuits_per_month * 100:.2f}'
          f' percent less biscuits.')
