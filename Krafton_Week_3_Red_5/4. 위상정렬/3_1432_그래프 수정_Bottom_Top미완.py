from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())

matrix = list(list(sys.stdin.readline().strip()) for _ in range(n))
child_list = list([] for _ in range(n))
parent_list = list([] for _ in range(n))
num_parent = list(0 for _ in range(n))
is_visit = list(0 for _ in range(n))
check_cycle = list(0 for _ in range(n))

topology_list = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == '1':
            child_list[j].append(i)
            parent_list[i].append(j)
            num_parent[i] += 1


def find_cycle(now_node):
    global is_visit, child_list, check_cycle
    if is_visit[now_node] and check_cycle[now_node] == 0:
        print(-1)
        exit()
    is_visit[now_node] = 1

    for child in child_list[now_node]:
        find_cycle(child)

    check_cycle[now_node] = 1


for now_node in range(n):
    is_visit = list(0 for _ in range(n))
    check_cycle = list(0 for _ in range(n))
    find_cycle(now_node)


visit_pq = []
result_list = list(0 for _ in range(n))
is_pushed = list(0 for _ in range(n))


def find_pushed(now_node):
    global child_list, is_visit, visit_pq, is_pushed

    if is_visit[now_node]:
        return

    if not child_list[now_node] and is_pushed[now_node] == 0:
        is_pushed[now_node] = 1
        heappush(visit_pq, now_node)

    is_visit[now_node] = 1

    for child in child_list[now_node]:
        find_pushed(child)


temp_number = 1

while True:
    is_visit = list(0 for _ in range(n))
    for now_node in range(n):
        if num_parent[now_node] == 0:
            find_pushed(now_node)

    if not visit_pq:
        break

    while visit_pq:
        popped = heappop(visit_pq)
        result_list[popped] = temp_number
        temp_number += 1
        for parent in parent_list[popped]:
            child_list[parent].remove(popped)

print(*result_list)




