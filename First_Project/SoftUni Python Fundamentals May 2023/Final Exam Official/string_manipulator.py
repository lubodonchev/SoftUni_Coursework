def translate(string, char, replacement):
    if char in string:
        string = string.replace(char, replacement)
    print(string)
    return string


def includes(string, substring):
    if substring in string:
        return True
    else:
        return False


def start(string, substring):
    if substring in string and string.index(substring) == 0:
        return True
    else:
        return False


def lowercase(string):
    string = string.lower()
    print(string)
    return string


def find_index(string, char):
    if char in string:
        return string.rfind(char)


def remove(string, start_index, count):
    end_index = start_index + count
    new_string = string[:start_index] + string[end_index:]
    print(new_string)
    return new_string


text = input()

while True:
    command = input().split()
    if command[0] == 'End':
        quit()
    elif command[0] == 'Translate':
        text = translate(text, command[1], command[2])
    elif command[0] == 'Includes':
        print(includes(text, command[1]))
    elif command[0] == 'Start':
        print(start(text, command[1]))
    elif command[0] == 'Lowercase':
        text = lowercase(text)
    elif command[0] == 'FindIndex':
        print(find_index(text, command[1]))
    elif command[0] == 'Remove':
        text = remove(text, int(command[1]), int(command[2]))
