import sys

n = int(sys.stdin.readline())

for _ in range(n):
    inp = list(sys.stdin.readline().strip())
    score = 0
    stack = 1
    for c in inp:
        if c == 'O':
            score += stack
            stack += 1
        else:
            stack = 1
    print(score)

