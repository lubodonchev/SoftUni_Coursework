goal = str(input())

counter = 0

while True:
    book = str(input())

    if book == goal:
        print(f"You checked {counter} books and found it.")
        break
    elif book == "No More Books":
        print(f"The book you search is not here!\nYou checked {counter} books.")
        break
    else:
        counter += 1
