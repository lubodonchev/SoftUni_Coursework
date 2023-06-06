def palindrome(a):
    lst = a.split(', ')

    for element in lst:
        if element == element[::-1]:
            print('True')
        else:
            print('False')


numbers = str(input())

palindrome(numbers)
