import sys, math

a = int(sys.stdin.readline())

b = list(sys.stdin.readline().strip())
mul = a * int(''.join(b))
b.reverse()
for bb in b:
    print(a * int(bb))
print(mul)

