GOAL = 10_000
total_steps = 0

while True:
    steps = input()
    if steps == "Going home":
        steps = int(input())
        total_steps += steps
        if total_steps >= GOAL:
            print(f"Goal reached! Good job!\n{total_steps - GOAL} steps over the goal!")
            break
        else:
            print(f"{GOAL - total_steps} more steps to reach goal.")
            break
    else:
        total_steps += int(steps)
    if total_steps >= GOAL:
        print(f"Goal reached! Good job!\n{total_steps - GOAL} steps over the goal!")
        break
