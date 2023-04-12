import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
decks = list(int(sys.stdin.readline()) for _ in range(n))
result = 0
heap = []

for deck in decks:
    heappush(heap, deck)

for i in range(n - 1):
    a, b = heappop(heap), heappop(heap)
    result += a + b
    heappush(heap, a + b)

print(result)