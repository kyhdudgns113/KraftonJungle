import sys

t = int(sys.stdin.readline())

stack = list(0 for __ in range(52))

for _ in range(t):
    data = sys.stdin.readline().strip()
    stack_size = 0

    for c in data:
        if c == '(':
            stack_size += 1
        elif stack_size:
            stack_size -= 1
        else:
            stack_size = None
            break

    if stack_size == 0:
        sys.stdout.write('YES\n')
    else:
        sys.stdout.write('NO\n')
