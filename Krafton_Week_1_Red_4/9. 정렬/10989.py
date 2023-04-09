import sys

n = int(sys.stdin.readline())

cnt = list(0 for i in range(10002))

for i in range(n):
    inp = int(sys.stdin.readline())
    cnt[inp] += 1

for i in range(10001):
    for j in range(cnt[i]):
        sys.stdout.write(str(i) + '\n')
