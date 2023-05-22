length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = (length * width * height) * (100 - percentage) / 100000

print(volume)
