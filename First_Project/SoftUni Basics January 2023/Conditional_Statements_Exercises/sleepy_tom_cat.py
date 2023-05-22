days_off = int(input())

play_time = (365 - days_off) * 63 + days_off * 127

hours = abs(30000 - play_time) // 60
minutes = abs(30000 - play_time) % 60

if play_time > 30000:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
