total_student_counter, total_standard_counter, total_kid_counter = 0, 0, 0

while True:
    movie = input()
    if movie == "Finish":
        break
    seats = int(input())
    student_counter, standard_counter, kid_counter = 0, 0, 0
    while True:
        ticket = input()
        if ticket == "End":
            break
        elif ticket == "student":
            student_counter += 1
            total_student_counter += 1
        elif ticket == "standard":
            standard_counter += 1
            total_standard_counter += 1
        elif ticket == "kid":
            kid_counter += 1
            total_kid_counter += 1
        if student_counter + standard_counter + kid_counter >= seats:
            break
    print(f'{movie} - {(student_counter + standard_counter + kid_counter) / seats * 100:.2f}% full.')

total = total_student_counter + total_standard_counter + total_kid_counter
print(f'Total tickets: {total}')
print(f'{total_student_counter / total * 100:.2f}% student tickets.')
print(f'{total_standard_counter / total * 100:.2f}% standard tickets.')
print(f'{total_kid_counter / total * 100:.2f}% kids tickets.')
