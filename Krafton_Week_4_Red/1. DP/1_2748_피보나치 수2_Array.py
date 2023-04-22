import sys

n = int(sys.stdin.readline())

dp_fibonacci = list(0 for _ in range(n + 1))

dp_fibonacci[1] = 1

for i in range(2, n + 1):
    dp_fibonacci[i] = dp_fibonacci[i - 1] + dp_fibonacci[i - 2]

print(dp_fibonacci[n])
