import sys

n, k = map(int, sys.stdin.readline().split())

num_str = list(sys.stdin.readline().strip())

stack = list(-1 for _ in range(500005))
stack_size = 0

for c in num_str:
    c = int(c)
    if stack_size == 0 or k == 0:
        stack[stack_size] = c
        stack_size += 1
    else:
        while stack_size > 0 and stack[stack_size - 1] < c and k > 0:
            k -= 1
            stack_size -= 1
            stack[stack_size] = -1
        stack[stack_size] = c
        stack_size += 1

while k > 0:
    stack_size -= 1
    k -= 1

for i in range(stack_size):
    stack[i] = str(stack[i])

if stack_size == 0:
    print(0)
    exit()

result = ''.join(stack[0:stack_size])
print(result)

