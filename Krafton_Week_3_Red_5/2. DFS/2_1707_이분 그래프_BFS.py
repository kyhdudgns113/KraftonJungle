from queue import Queue
import sys

sys.setrecursionlimit(10**6)

K = int(sys.stdin.readline())


def bfs(now, now_color):
    global isColored, result, connected_list
    isColored[now] = now_color
    next_color = 3 - now_color
    next_visit_q = Queue()
    next_visit_q.put(now)

    while not next_visit_q.empty():
        now = next_visit_q.get()
        now_color = isColored[now]
        next_color = 3 - now_color
        for next_node in connected_list[now]:
            if not isColored[next_node]:
                isColored[next_node] = next_color
                next_visit_q.put(next_node)
            elif isColored[next_node] == now_color:
                result = 'NO'


for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())

    connected_list = list([] for _ in range(V + 1))

    for __ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        connected_list[u].append(v)
        connected_list[v].append(u)

    isColored = [0 for _ in range(V + 1)]
    result = 'YES'

    for i in range(1, V + 1):
        if not isColored[i]:
            bfs(i, 1)

    print(result)





