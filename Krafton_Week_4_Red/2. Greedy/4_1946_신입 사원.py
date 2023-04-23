import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    rankings = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
    rankings.sort()
    stack = list([] for _ in range(n))
    stack_size = 0

    for ranking in rankings:
        if stack_size == 0:
            stack[stack_size] = ranking
            stack_size += 1
        else:
            if ranking[1] < stack[stack_size - 1][1]:
                stack[stack_size] = ranking
                stack_size += 1

    print(stack_size)
