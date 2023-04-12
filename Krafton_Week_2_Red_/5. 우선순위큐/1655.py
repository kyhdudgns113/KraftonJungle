import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
integers = list(int(sys.stdin.readline()) for _ in range(n))

mid_val = integers[0]
lower_heap = []
higher_heap = []
sys.stdout.write(f'{mid_val}\n')

for i in range(1, len(integers)):
    if mid_val < integers[i]:
        heappush(higher_heap, integers[i])
    else:
        heappush(lower_heap, -integers[i])

    if len(lower_heap) > len(higher_heap):
        heappush(higher_heap, mid_val)
        mid_val = -heappop(lower_heap)
    elif len(lower_heap) + 1 < len(higher_heap):
        heappush(lower_heap, -mid_val)
        mid_val = heappop(higher_heap)
    sys.stdout.write(f'{mid_val}\n')
