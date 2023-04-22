from queue import Queue
import sys

n, m = map(int, sys.stdin.readline().split())

connection_list = list([] for _ in range(n + 1))
num_fathers = list(0 for _ in range(n + 1))
answer = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    connection_list[a].append(b)
    num_fathers[b] += 1

visit_queue = Queue()
topology_queue = Queue()

for i in range(1, n + 1):
    if num_fathers[i] == 0:
        visit_queue.put(i)

while visit_queue.qsize() > 0:
    now = visit_queue.get()
    answer.append(now)

    for next_node in connection_list[now]:
        num_fathers[next_node] -= 1
        if num_fathers[next_node] == 0:
            visit_queue.put(next_node)

for res in answer:
    sys.stdout.write(f'{res} ')


