n = int(input())
time = str(input())
# taxi = 99999999999999999999999999999999999
# train = 9999999999999999999999999999999999
# bus = 999999999999999999999999999999999999

if n >= 100:
    if time == "day":
        taxi = 0.7 + 0.79 * n
        bus = 0.09 * n
        train = 0.06 * n
    elif time == "night":
        taxi = 0.7 + 0.9 * n
        bus = 0.09 * n
        train = 0.06 * n
elif n >= 20:
    if time == "day":
        taxi = 0.7 + 0.79 * n
        bus = 0.09 * n
    elif time == "night":
        taxi = 0.7 + 0.9 * n
        bus = 0.09 * n
else:
    if time == "day":
        taxi = 0.7 + 0.79 * n
    elif time == "night":
        taxi = 0.7 + 0.9 * n

print(f'{min(taxi, bus, train):.2f}')
