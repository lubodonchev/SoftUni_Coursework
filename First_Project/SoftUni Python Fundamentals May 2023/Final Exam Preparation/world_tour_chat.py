def manipulate_stops():
    stops = input()
    while True:
        command = input().split(":")
        action = command[0]

        if action == "Travel":
            break
        elif action == "Add Stop":
            index = int(command[1])
            new_string = command[2]
            if 0 <= index < len(stops):
                stops = stops[:index] + new_string + stops[index:]
        elif action == "Remove Stop":
            start_index = int(command[1])
            end_index = int(command[2])
            if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
                stops = stops[:start_index] + stops[end_index + 1:]
        elif action == "Switch":
            old_string = command[1]
            new_string = command[2]
            stops = stops.replace(old_string, new_string)

        print(stops)

    print(f"Ready for world tour! Planned stops: {stops}")


manipulate_stops()
