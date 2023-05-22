from math import floor

current_record = float(input())
distance_meters = float(input())
time_per_meter = float(input())

time_lost = floor(distance_meters / 15) * 12.5

time = distance_meters * time_per_meter + time_lost

if time < current_record:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time - current_record:.2f} seconds slower.")
