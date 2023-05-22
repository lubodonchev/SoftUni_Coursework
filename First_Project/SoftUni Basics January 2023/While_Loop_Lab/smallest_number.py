from sys import maxsize

smallest = maxsize

while True:
    current_number = input()
    if current_number == "Stop":
        break
    else:
        current_number = int(current_number)
        if current_number < smallest:
            smallest = current_number
print(smallest)
