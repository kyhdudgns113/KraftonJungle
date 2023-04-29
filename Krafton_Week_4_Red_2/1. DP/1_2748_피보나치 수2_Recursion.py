import sys

n = int(sys.stdin.readline())


dp_fibonacci = list(-1 for r_ in range(n + 1))


def fibonacci(n):

    if n == 0:
        dp_fibonacci[0] = 0
        return 0
    if n == 1:
        dp_fibonacci[1] = 1
        return 1

    if dp_fibonacci[n] != -1:
        return dp_fibonacci[n]
    else:
        dp_fibonacci[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return dp_fibonacci[n]


fibonacci(n)

print(dp_fibonacci[3])

