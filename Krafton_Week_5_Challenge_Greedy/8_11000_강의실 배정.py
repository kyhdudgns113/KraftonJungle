from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())

sts = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
sts
pq = []

for st in sts:
    if len(pq) == 0:
        heappush(pq, st[1])
    else:
        popped = heappop(pq)
        heappush(pq, st[1])
        if popped > st[0]:
            heappush(pq, popped)

print(len(pq))


