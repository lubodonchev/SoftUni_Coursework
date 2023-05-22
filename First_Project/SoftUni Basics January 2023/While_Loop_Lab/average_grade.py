student_name = str(input())

total_of_grades = 0
failed_counter = 0
grades_counter = 0

while True:
    current_grade = float(input())
    if current_grade < 4:
        failed_counter += 1
        if failed_counter == 2:
            print(f"{student_name} has been excluded at {grades_counter + 1} grade")
            break
    else:
        grades_counter += 1
        total_of_grades += current_grade
        if grades_counter == 12:
            print(f"{student_name} graduated. Average grade: {total_of_grades / 12:.2f}")
            break

