capacity_one, capacity_two, capacity_three = int(input()), int(input()), int(input())

student_count = int(input())

total_capacity = capacity_one + capacity_two + capacity_three

hours_needed = 0
counter = 0

while True:
    if student_count <= 0:
        break

    student_count -= total_capacity
    counter += 1
    hours_needed += 1

    if student_count <= 0:
        break

    if counter % 3 == 0:
        counter = 0
        hours_needed += 1

print(f'Time needed: {hours_needed}h.')
