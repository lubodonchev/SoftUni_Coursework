number_of_electrons = int(input())
lst = []
counter = 1

while True:
    current_shell = 2 * counter ** 2
    if number_of_electrons <= current_shell:
        lst.append(number_of_electrons)
        break
    else:
        lst.append(current_shell)
        number_of_electrons -= current_shell
    counter += 1

print(lst)
