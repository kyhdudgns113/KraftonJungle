from heapq import heappush, heappop
import sys

n, k = map(int, sys.stdin.readline().split())
coins = list(int(sys.stdin.readline()) for _ in range(n))
counts = list(0x7fffffff for _ in range(k + 1))

coins.sort(key=lambda x: -x)
visit_pq = []

for coin in coins:
    heappush(visit_pq, [coin, 1])

while visit_pq:
    popped = heappop(visit_pq)
    now_cost = popped[0]
    now_count = popped[1]
    counts[now_cost] = min(
        counts[now_cost],
        now_count
    )
    if now_cost == k:
        print(now_count)
        exit()
    for coin in coins:
        next_cost = now_cost + coin
        if next_cost <= k and counts[next_cost] > now_count + 1:
            counts[next_cost] = now_count + 1
            heappush(visit_pq, [next_cost, now_count + 1])

print(-1)



