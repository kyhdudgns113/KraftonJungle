import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

for b in a:
    if b < x:
        sys.stdout.write(str(b) + ' ')
