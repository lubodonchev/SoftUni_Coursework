# destination = None
# flag = False
#
# while destination != "End":               idk how this can happen
#     destination = input()
#     budget = float(input())
#     saved = 0
#     while saved < budget:
#         saved += float(input())
#     else:
#         print(f'Going to {destination}!')
# else:
#     flag = True

while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    saved = 0
    while True:
        saved += float(input())
        if saved >= budget:
            print(f'Going to {destination}!')
            break

