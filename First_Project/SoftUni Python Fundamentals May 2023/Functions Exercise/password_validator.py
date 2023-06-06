def validator(a):
    digit_counter = 0
    flag_len = False
    flag_digi = False
    flag_count = False

    if not 6 <= len(a) <= 10:
        flag_len = True

    for i in a:
        if not i.isdigit() and not i.isalpha():
            flag_digi = True
        if i.isdigit():
            digit_counter += 1

    if digit_counter < 2:
        flag_count = True

    if flag_len:
        print('Password must be between 6 and 10 characters')
    if flag_digi:
        print('Password must consist only of letters and digits')
    if flag_count:
        print('Password must have at least 2 digits')
    if not flag_count and not flag_digi and not flag_len:
        print('Password is valid')


password = str(input())

validator(password)
