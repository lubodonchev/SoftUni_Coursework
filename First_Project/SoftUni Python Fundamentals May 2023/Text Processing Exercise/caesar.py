data = input()
encrypted = ''

for ch in data:
    encrypted += chr(ord(ch) + 3)

print(encrypted)
