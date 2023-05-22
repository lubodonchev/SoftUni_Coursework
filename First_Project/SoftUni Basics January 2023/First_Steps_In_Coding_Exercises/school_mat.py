pens = int(input())
markers = int(input())
liquid = int(input())
discount = int(input())

money = (pens * 5.8 + markers * 7.2 + liquid * 1.2) * (100 - discount) / 100

print(money)
