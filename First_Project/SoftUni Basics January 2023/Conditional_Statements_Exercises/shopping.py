budget = float(input())
video_amount = int(input())
processor_amount = int(input())
ram_amount = int(input())

VIDEO_PRICE = 250
PROCESSOR_PRICE = 0.35 * VIDEO_PRICE * video_amount
RAM_PRICE = 0.1 * VIDEO_PRICE * video_amount

cost = video_amount * VIDEO_PRICE + processor_amount * PROCESSOR_PRICE + ram_amount * RAM_PRICE

if video_amount > processor_amount:
    cost *= 0.85

difference = abs(budget - cost)

if budget < cost:
    print(f"Not enough money! You need {difference:.2f} leva more!")
else:
    print(f"You have {difference:.2f} leva left!")
