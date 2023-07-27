def flip(text, key, start_index, end_index):
    substitute = ''

    if key == 'Upper':
        substitute += text[start_index:end_index].upper()
    else:
        substitute += text[start_index:end_index].lower()

    end_text = text[:start_index] + substitute + text[end_index:]
    return end_text


def my_slice(text, start_index, end_index):
    new_text = text[:start_index] + text[end_index:]
    return new_text


activation_key = input()

while True:
    command = input().split('>>>')

    if command[0] == 'Generate':
        break
    elif command[0] == 'Contains':
        if command[1] in activation_key:
            print(f'{activation_key} contains {command[1]}')
        else:
            print(f'Substring not found!')
    elif command[0] == 'Flip':
        activation_key = flip(activation_key, command[1], int(command[2]), int(command[3]))
        print(activation_key)
    elif command[0] == 'Slice':
        activation_key = my_slice(activation_key, int(command[1]), int(command[2]))
        print(activation_key)

print(f'Your activation key is: {activation_key}')
