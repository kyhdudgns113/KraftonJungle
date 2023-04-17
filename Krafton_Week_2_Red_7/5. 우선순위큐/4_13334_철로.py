import sys
import copy
from collections import deque
from heapq import heappush, heappop

n = int(sys.stdin.readline())

hos = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

d = int(sys.stdin.readline())

for ho in hos:
    if ho[0] > ho[1]:
        ho[0], ho[1] = ho[1], ho[0]

hos.sort(key=lambda x: (x[0], -x[1]))  # Tested

stack = copy.deepcopy(hos)
stack.sort(key=lambda x: (x[1], x[0]))

stack_idx = 0

pq = []
max_result = 0
for ho in hos:
    left = ho[0]
    right = left + d

    while len(pq) > 0:
        popped = heappop(pq)
        if left <= popped[0]:
            heappush(pq, popped)
            break

    #   pq 에 넣는다.
    while stack_idx < n and stack[stack_idx][1] <= right:
        if left <= stack[stack_idx][0]:
            heappush(pq, stack[stack_idx])
            stack_idx += 1
        else:
            stack_idx += 1

    max_result = max(max_result, len(pq))

print(max_result)



