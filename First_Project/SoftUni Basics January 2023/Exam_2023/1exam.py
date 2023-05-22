number_of_students = int(input())

five_counter, four_counter, three_counter, two_counter, total_counter = 0, 0, 0, 0, 0


for _ in range(number_of_students):
    grade = float(input())
    total_counter += grade
    if grade >= 5:
        five_counter += 1
    elif grade >= 4:
        four_counter += 1
    elif grade >= 3:
        three_counter += 1
    else:
        two_counter += 1

print(f"Top students: {five_counter / number_of_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {four_counter / number_of_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {three_counter / number_of_students * 100:.2f}%")
print(f"Fail: {two_counter / number_of_students * 100:.2f}%")
print(f"Average: {total_counter / number_of_students:.2f}")
