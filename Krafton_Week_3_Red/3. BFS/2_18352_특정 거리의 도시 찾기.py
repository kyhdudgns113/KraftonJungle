from queue import Queue
import sys

n, m, k, x = map(int, sys.stdin.readline().split())

connection_list = list([] for _ in range(n + 1))

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    connection_list[a].append(b)


is_visit = list(False for _ in range(n + 1))
next_visit_queue = Queue()

if len(connection_list[x]) == 0:
    print(-1)
    exit()

next_visit_queue.put([x, 0])
is_visit[x] = True
k_list = []

while not next_visit_queue.empty():
    now_node, now_distance = next_visit_queue.get()
    if now_distance == k:
        k_list.append(now_node)
    for next_node in connection_list[now_node]:
        if not is_visit[next_node]:
            is_visit[next_node] = True
            next_visit_queue.put([next_node, now_distance + 1])

if len(k_list) == 0:
    print(-1)
else:
    k_list.sort()
    for ks in k_list:
        sys.stdout.write(f'{ks}\n')



