# class Email:
#     def __init__(self, sender, receiver, content, is_sent=False):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = is_sent
#
#     def send(self, is_sent):
#         self.is_sent = True
#
#     def get_info(self, sender, receiver, content, is_sent):
#         return f'{sender} says to {receiver}: {content}. Sent: {is_sent}'
#
#
# master_lst = []
#
# while True:
#     command_lst = str(input()).split()
#
#     if command_lst[0] == 'Stop':
#         indices = [int(element) for element in input().split(', ')]
#         for element in indices:
#             master_lst[element].send(master_lst[element].is_sent)
#         break
#     else:
#         s = command_lst[0]
#         r = command_lst[1]
#         c = command_lst[2]
#         email = Email(s, r, c)
#         master_lst.append(email)
# for element in master_lst:
#     print(element.get_info(element.sender, element.receiver, element.content, element.is_sent))

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


master_lst = []

while True:
    command_lst = str(input()).split()

    if command_lst[0] == 'Stop':
        break
    else:
        s, r, c = command_lst
        email = Email(s, r, c)
        master_lst.append(email)

indices = [int(element) for element in input().split(', ')]

for element in indices:
    master_lst[element].send()

for element in master_lst:
    print(element.get_info())
