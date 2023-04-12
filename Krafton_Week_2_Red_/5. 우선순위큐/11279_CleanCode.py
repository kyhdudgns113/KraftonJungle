import sys
from heapq import heappush, heappop, heapify


n = int(sys.stdin.readline())

heap = []

ords = list(int(sys.stdin.readline()) for _ in range(n))

for ord in ords:
    if ord == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, -ord)


