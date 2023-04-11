import sys

stack = list(0 for _ in range(100005))
stack_size = 0
final_sum = 0

k = int(sys.stdin.readline())

for _ in range(k):
    n = int(sys.stdin.readline())
    match n:
        case 0:
            stack_size -= 1
            final_sum -= stack[stack_size]
        case _:
            stack[stack_size] = n
            stack_size += 1
            final_sum += n

print(final_sum)



