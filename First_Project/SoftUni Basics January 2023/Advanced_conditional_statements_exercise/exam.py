hour_exam = int(input())
minute_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

time_exam = hour_exam * 60 + minute_exam
time_arrival = arrival_hour * 60 + arrival_minute

difference = time_exam - time_arrival

if difference < 0:
    print("Late")
elif difference > 30:
    print("Early")
else:
    print("On time")

if abs(difference) >= 1:
    if difference <= -60:
        difference = abs(difference)
        print(f"{difference // 60}:{difference % 60:02d} hours after the start")
    elif -60 < difference < 0:
        print(f"{abs(difference)} minutes after the start")
    elif 0 < difference < 60:
        print(f"{difference} minutes before the start")
    elif difference >= 60:
        print(f"{difference // 60}:{difference % 60:02d} hours before the start")
