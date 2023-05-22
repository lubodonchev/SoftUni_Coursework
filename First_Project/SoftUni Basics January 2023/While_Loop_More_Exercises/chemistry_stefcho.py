c_atoms = int(input())
h_atoms = int(input())

if h_atoms == 2 * c_atoms + 2:
    result = f'The hydrocarbon is an alkane\nThe formula of the alkane is C{c_atoms}H{h_atoms}'
elif h_atoms == 2 * c_atoms:
    result = f'The hydrocarbon is an alkene\nThe formula of the alkene is C{c_atoms}H{h_atoms}'
elif h_atoms == 2 * c_atoms - 2:
    result = f'The hydrocarbon is an alkyne\nThe formula of the alkyne is C{c_atoms}H{h_atoms}'
elif h_atoms == 2 * c_atoms - 6 and c_atoms >= 6:
    result = f'The hydrocarbon is an arene\nThe formula of the arene is C{c_atoms}H{h_atoms}'
else:
    result = 'The compound does not exist!'

print(result)
