import sys


stack = list(0 for i in range(10001))
stack_size = 0

n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    match command[0]:
        case 'push':
            stack[stack_size] = int(command[1])
            stack_size += 1
        case 'pop':
            if stack_size:
                sys.stdout.write(str(stack[stack_size - 1]) + '\n')
                stack_size -= 1
            else:
                sys.stdout.write('-1\n')
        case 'size':
            sys.stdout.write(str(stack_size) + '\n')
        case 'empty':
            sys.stdout.write('0\n' if stack_size else '1\n')
        case 'top':
            sys.stdout.write((str(stack[stack_size - 1]) if stack_size else '-1') + '\n')
