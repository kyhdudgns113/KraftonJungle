##################################################
#
#
#       때려쳐버리자 ㅎㅎㅎㅎ
#
#
##################################################

from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())

rcs = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
adjacent_list = list([0, 0, 0] for _ in range(n + 1))

pq = []

for i in range(1, n):
    rc = rcs[i]
    heappush(pq, [-rc[0], i])

for i in range(0, n + 1):
    adjacent_list[i][0] = i - 1
    adjacent_list[i][1] = i + 1
    if i < n:
        adjacent_list[i][2] = rcs[i][0]
    else:
        adjacent_list[i][2] = rcs[n - 1][1]

result = 0

while len(pq):
    now_val, now_idx = heappop(pq)
    now_val *= -1

    previous_idx = adjacent_list[now_idx][0]
    next_idx = adjacent_list[now_idx][1]

    previous_val = adjacent_list[previous_idx][2]
    next_val = adjacent_list[next_idx][2]

    result += now_val*previous_val*next_val

    adjacent_list[previous_idx][1] = next_idx
    adjacent_list[next_idx][0] = previous_idx

print(result)
