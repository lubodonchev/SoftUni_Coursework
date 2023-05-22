number_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours = (number_pages // pages_per_hour) // days

print(hours)
