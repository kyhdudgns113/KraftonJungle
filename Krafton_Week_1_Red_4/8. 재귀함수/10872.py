import sys


def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)


n = int(sys.stdin.readline())

print(fact(n))