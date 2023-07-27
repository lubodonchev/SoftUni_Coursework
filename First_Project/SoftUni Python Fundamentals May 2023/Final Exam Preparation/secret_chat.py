def insert_space(text, index):
    text_one = text[0:index]
    text_two = text[index::]
    text = text_one + ' ' + text_two
    return text


def reverse(text, substring):
    if substring in text:
        text = text.replace(substring, '', 1)
        text += substring[::-1]
    else:
        print('error')
    return text


def change_all(text, substring, replacement):
    text = text.replace(substring, replacement)
    return text


message = input()

while True:
    command_lst = input().split(':|:')
    if command_lst[0] == 'Reveal':
        break
    elif command_lst[0] == 'InsertSpace':
        n = int(command_lst[1])
        message = insert_space(message, n)
        print(message)
    elif command_lst[0] == 'Reverse':
        new_message = reverse(message, command_lst[1])
        if message != new_message:
            print(new_message)
        message = new_message
    elif command_lst[0] == 'ChangeAll':
        message = change_all(message, command_lst[1], command_lst[2])
        print(message)

print(f'You have a new text message: {message}')
