from math import ceil

series_name = str(input())
episode_length = int(input())
break_length = int(input())

lunch = break_length / 8
chill = break_length / 4

total_time = episode_length + lunch + chill

difference = abs(break_length - total_time)

if break_length < total_time:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(difference)} more minutes.")
else:
    print(f"You have enough time to watch {series_name} and left with {ceil(difference)} minutes free time.")
