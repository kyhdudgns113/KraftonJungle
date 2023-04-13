import sys

n = int(sys.stdin.readline())
tower_heights = list(map(int, sys.stdin.readline().split()))

stack = list([0, 0] for i in range(500002))

stack_size = 0

for i, tower in enumerate(tower_heights):
    while stack_size and tower > stack[stack_size - 1][1]:
        stack_size -= 1
    if stack_size:
        sys.stdout.write(str(stack[stack_size - 1][0]) + ' ')
    else:
        sys.stdout.write('0 ')
    stack[stack_size] = [i + 1, tower]
    stack_size += 1
