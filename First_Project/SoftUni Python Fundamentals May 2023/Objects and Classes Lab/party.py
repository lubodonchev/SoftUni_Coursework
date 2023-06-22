class Party:
    def __init__(self):
        self.people = []


party_one = Party()

while True:
    command = str(input())
    if command == 'End':
        break
    else:
        party_one.people.append(command)

print(f'Going: {", ".join(party_one.people)}')
print(f'Total: {len(party_one.people)}')
