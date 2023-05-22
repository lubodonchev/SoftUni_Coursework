members_of_jury = int(input())
presentation_name = None
total_grade_sum = 0
counter = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        print(f'Student\'s final assessment is {total_grade_sum / members_of_jury / counter:.2f}.')
        break
    sum_grade = 0
    counter += 1
    for _ in range(members_of_jury):
        grade = float(input())
        sum_grade += grade
        total_grade_sum += grade
    average_grade = sum_grade / members_of_jury
    print(f'{presentation_name} - {average_grade:.2f}.')
