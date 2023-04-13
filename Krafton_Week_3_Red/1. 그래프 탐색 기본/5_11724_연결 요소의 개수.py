import sys

n, m = map(int, sys.stdin.readline().split())

isConnected = list(list(0 for _ in range(n + 1)) for _ in range(n + 1))

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    isConnected[u][v] = 1
    isConnected[v][u] = 1

isVisited = list(0 for _ in range(n + 1))


def dfs(now):
    global isVisited, isConnected
    isVisited[now] = 1

    for next_v in range(n + 1):
        if isVisited[next_v] == 0 and isConnected[now][next_v] == 1:
            dfs(next_v)


connectedComponents = 0

for i in range(1, n + 1):
    if isVisited[i] == 0:
        connectedComponents += 1
        dfs(i)

print(connectedComponents)

