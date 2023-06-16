from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_attendance = 0
max_bonus = 0

for _ in range(students):
    current_attendance = int(input())
    if current_attendance > max_attendance:
        max_attendance = current_attendance
        max_bonus = max_attendance / lectures * (5 + additional_bonus)

print(f'Max Bonus: {ceil(max_bonus)}.\nThe student has attended {max_attendance} lectures.')
