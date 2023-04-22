from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())
connection_list = list([] for _ in range((n + 1)))
child_num = [0] * (n + 1)

for v in range(1, n + 1):
    temp = [0] + list(map(int, sys.stdin.readline().strip()))
    for i in range(1, n + 1):
        if temp[i] == 1:
            connection_list[i].append(v)
            child_num[v] += 1


def topology_sort():
    global child_num, n, connection_list
    pq = []
    for i in range(1, n + 1):
        if child_num[i] == 0:
            heappush(pq, -i)

    temp_num = n
    while pq:
        now = -heappop(pq)
        answer[now] = temp_num

        for i in connection_list[now]:
            child_num[i] -= 1
            if child_num[i] == 0:
                heappush(pq, -i)
        temp_num -= 1


answer = [0] * (n + 1)

topology_sort()
if answer.count(0) > 1:
    print(-1)
else:
    print(*answer[1:])
