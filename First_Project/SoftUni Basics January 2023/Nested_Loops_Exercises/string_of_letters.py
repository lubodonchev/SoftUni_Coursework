n_counter, o_counter, c_counter = 0, 0, 0
word = ""

while True:
    letter = input()
    if letter == "End":
        break

    if letter == "n" and n_counter == 0:
        n_counter += 1
    elif letter == "o" and o_counter == 0:
        o_counter += 1
    elif letter == "c" and c_counter == 0:
        c_counter += 1
    else:
        if letter.isalpha():
            word += letter
    if n_counter == 1 and o_counter == 1 and c_counter == 1:
        n_counter, o_counter, c_counter = 0, 0, 0
        print(word, end=" ")
        word = " "

