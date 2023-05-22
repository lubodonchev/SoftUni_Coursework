skumriq_price = float(input())
caca_price = float(input())
amount_palamud = float(input())
amount_safrid = float(input())
amount_midi = int(input())

PALAMUD_PRICE = 1.6 * skumriq_price
SAFRID_PRICE = 1.8 * caca_price
MIDI_PRICE = 7.5

total = PALAMUD_PRICE * amount_palamud + SAFRID_PRICE * amount_safrid + MIDI_PRICE * amount_midi

print("%.2f" % total)
