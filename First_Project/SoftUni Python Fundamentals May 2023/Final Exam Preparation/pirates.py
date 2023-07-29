def plunder(dic, town, people, gold):
    if town in master_dic.keys():
        master_dic[town]['population'] -= people
        master_dic[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if master_dic[town]['population'] <= 0 or master_dic[town]['gold'] <= 0:
            del master_dic[town]
            print(f"{town} has been wiped off the map!")
    return dic


def prosper(dic, town, gold):
    if gold <= 0:
        print('Gold added cannot be a negative number!')
    else:
        dic[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {dic[town]['gold']} gold.")
    return dic


master_dic = {}

while True:
    data = input().split('||')
    if data[0] == 'Sail':
        break
    if data[0] not in master_dic.keys():
        master_dic[data[0]] = {'population': int(data[1]), 'gold': int(data[2])}
    else:
        master_dic[data[0]]['population'] += int(data[1])
        master_dic[data[0]]['gold'] += int(data[2])

while True:
    command = input().split('=>')
    if command[0] == 'End':
        break
    elif command[0] == 'Plunder':
        master_dic = plunder(master_dic, command[1], int(command[2]), int(command[3]))
    elif command[0] == 'Prosper':
        master_dic = prosper(master_dic, command[1], int(command[2]))

if master_dic:
    print(f"Ahoy, Captain! There are {len(master_dic)} wealthy settlements to go to:")
    for key, value in master_dic.items():
        print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
