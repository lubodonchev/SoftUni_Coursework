v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

pipe_one = p1 * h
pipe_two = p2 * h

percentage = (pipe_one + pipe_two) / v * 100

contribution_pipe_one = pipe_one / (pipe_one + pipe_two) * 100
contribution_pipe_two = pipe_two / (pipe_one + pipe_two) * 100

if v >= (pipe_one + pipe_two):
    print(f"The pool is {percentage:.2f}% full. Pipe 1: {contribution_pipe_one:.2f}%. Pipe 2: {contribution_pipe_two:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {pipe_one + pipe_two - v:.2f} liters.")
