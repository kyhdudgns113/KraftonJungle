from heapq import heappush, heappop
import sys

n, k = map(int, sys.stdin.readline().split())
coins = list(int(sys.stdin.readline()) for _ in range(n))
counts = list(0x7fffffff for _ in range(k + 1))

for coin in coins:
    if coin <= k:
        counts[coin] = 1

for i in range(k + 1):
    if counts[i] != 0x7fffffff:
        for coin in coins:
            if i + coin <= k:
                counts[i + coin] = min(
                    counts[i + coin],
                    counts[i] + 1
                )

if counts[k] == 0x7fffffff:
    print(-1)
else:
    print(counts[k])



