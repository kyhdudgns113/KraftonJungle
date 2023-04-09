import sys

a, b = map(int, sys.stdin.readline().split())

a = list(str(a))
b = list(str(b))

a.reverse()
b.reverse()

a = int(''.join(a))
b = int(''.join(b))

sys.stdout.write(str(max(a, b)))


