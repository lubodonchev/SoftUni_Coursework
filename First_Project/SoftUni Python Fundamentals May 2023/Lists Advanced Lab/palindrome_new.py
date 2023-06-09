words_lst = str(input()).split()
palindrome = str(input())

palindrome_lst = [element for element in words_lst if element == element[::-1]]

count = words_lst.count(palindrome)

print(palindrome_lst)
print(f'Found palindrome {count} times')
