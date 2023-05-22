from sys import maxsize

biggest = - maxsize

while True:
    current_number = input()
    if current_number == "Stop":
        break
    else:
        current_number = int(current_number)
        if current_number > biggest:
            biggest = current_number
print(biggest)
