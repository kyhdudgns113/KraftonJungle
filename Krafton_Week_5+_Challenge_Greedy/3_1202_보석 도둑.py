from heapq import heappush, heappop
from queue import Queue
import sys

n, k = map(int, sys.stdin.readline().split())

gems = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
bags = list(int(sys.stdin.readline()) for _ in range(k))
bags.sort()
gems.sort()

pq = []

idx_gems = 0
result_value = 0
for idx_bags in range(k):
    bag_weight = bags[idx_bags]
    for i in range(idx_gems, n):
        if gems[i][0] > bag_weight:
            break
        heappush(pq, -gems[i][1])
        idx_gems = i + 1
    if len(pq):
        first_value = heappop(pq)
        result_value -= first_value

print(result_value)







