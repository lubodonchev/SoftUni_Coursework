def cast_spell(dic, hero_name, mp_needed, spell_name):
    if dic[hero_name]['mp'] >= mp_needed:
        dic[hero_name]['mp'] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {dic[hero_name]['mp']} MP!")
    else:
        print(f'{hero_name} does not have enough MP to cast {spell_name}!')
    return dic


def take_damage(dic, hero_name, damage, attacker):
    dic[hero_name]['hp'] -= damage
    if dic[hero_name]['hp'] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {dic[hero_name]['hp']} HP left!")
    else:
        del dic[hero_name]
        print(f'{hero_name} has been killed by {attacker}!')
    return dic


def recharge(dic, hero_name, amount):
    initial_mp = dic[hero_name]['mp']
    dic[hero_name]['mp'] += amount
    if dic[hero_name]['mp'] > 200:
        dic[hero_name]['mp'] = 200
        print(f"{hero_name} recharged for {200 - initial_mp} MP!")
    else:
        print(f"{hero_name} recharged for {amount} MP!")
    return dic


def heal(dic, hero_name, amount):
    initial_hp = dic[hero_name]['hp']
    dic[hero_name]['hp'] += amount
    if dic[hero_name]['hp'] > 100:
        dic[hero_name]['hp'] = 100
        print(f"{hero_name} healed for {100 - initial_hp} HP!")
    else:
        print(f"{hero_name} healed for {amount} HP!")
    return dic


master_dic = {}

n = int(input())

for _ in range(n):
    data = input().split()
    master_dic[data[0]] = {'hp': int(data[1]), 'mp': int(data[2])}

while True:
    command = input().split(' - ')

    if command[0] == 'End':
        break
    elif command[0] == 'CastSpell':
        master_dic = cast_spell(master_dic, command[1], int(command[2]), command[3])
    elif command[0] == 'TakeDamage':
        master_dic = take_damage(master_dic, command[1], int(command[2]), command[3])
    elif command[0] == 'Recharge':
        master_dic = recharge(master_dic, command[1], int(command[2]))
    elif command[0] == 'Heal':
        master_dic = heal(master_dic, command[1], int(command[2]))

for key, value in master_dic.items():
    print(key)
    print(f"    HP: {value['hp']}")
    print(f"    MP: {value['mp']}")
