import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

mul = list(str(a*b*c))

for _ in range(0, 10):
    sys.stdout.write("%d\n" % mul.count(str(_)))
