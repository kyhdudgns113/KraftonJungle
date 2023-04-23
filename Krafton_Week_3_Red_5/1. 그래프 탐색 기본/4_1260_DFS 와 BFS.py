from queue import Queue
import sys

n, m, v = map(int, sys.stdin.readline().split())

isConnected = list(list(0 for _ in range(n + 1)) for __ in range(n + 1))

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    isConnected[s][e] = 1
    isConnected[e][s] = 1


isVisitedDFS = list(0 for _ in range(n + 1))
isVisitedBFS = list(0 for _ in range(n + 1))


def dfs(v):
    global isVisitedDFS, isConnected
    isVisitedDFS[v] = 1
    sys.stdout.write(f'{v} ')
    for next_v in range(n + 1):
        if isConnected[v][next_v] == 1 and isVisitedDFS[next_v] == 0:
            dfs(next_v)


def bfs(v):
    global isVisitedBFS, isConnected
    next_visit_q = Queue()
    next_visit_q.put(v)
    while not next_visit_q.empty():
        now = next_visit_q.get()
        if isVisitedBFS[now] == 0:
            isVisitedBFS[now] = 1
            sys.stdout.write(f'{now} ')
            for next in range(n + 1):
                if isVisitedBFS[next] == 0 and isConnected[now][next] == 1:
                    next_visit_q.put(next)


dfs(v)
print()
bfs(v)











