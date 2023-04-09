import sys

T = int(sys.stdin.readline())

for _ in range(T):

    S = list(sys.stdin.readline().strip())

    R = int(S.pop(0))
    S.pop(0)
    for c in S:
        sys.stdout.write(c * R)
    sys.stdout.write('\n')