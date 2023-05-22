total_student, total_standard, total_kid = 0, 0, 0
movie = None
flag = False

while movie != "Finish":
    if flag:
        break
    movie = input()
    places = int(input())
    student_count, standard_count, kid_count = 0, 0, 0
    while True:
        ticket = input()
        if ticket == "student":
            student_count += 1
            total_student += 1
        elif ticket == "standard":
            standard_count += 1
            total_standard += 1
        elif ticket == "kid":
            kid_count += 1
            total_kid += 1
        elif ticket == "End":
            percentage = (student_count + standard_count + kid_count) / places * 100
            print(f'{movie} - {percentage:.2f}% full')
            break
        elif ticket == "Finish":
            flag = True
            break
        if student_count + standard_count + kid_count == places:
            percentage = (student_count + standard_count + kid_count) / places * 100
            print(f'{movie} - {percentage:.2f}% full')
            break
else:
    total = total_student + total_standard + total_kid
    student_percentage = total_student / total * 100
    standard_percentage = total_standard / total * 100
    kid_percentage = total_standard / total * 100
    print(f'Total tickets: {total}\n{student_percentage:.2f}% student tickets.\n{standard_percentage:.2f}% '
          f'standard tickets.\n{kid_percentage:.2f}% kids tickets.')
