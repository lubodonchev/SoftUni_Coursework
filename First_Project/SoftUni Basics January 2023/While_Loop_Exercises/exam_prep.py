threshold = int(input())
poor_counter = 0
total_from_grades = 0
counter = 0
last_problem = None

while True:
    name = str(input())

    if name == "Enough":
        print(f"Average score: {total_from_grades / counter:.2f}")
        print(f"Number of problems: {counter}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    if grade < 5:
        poor_counter += 1
    if poor_counter == threshold:
        print(f"You need a break, {poor_counter} poor grades.")
        break

    total_from_grades += grade
    counter += 1
    last_problem = name
