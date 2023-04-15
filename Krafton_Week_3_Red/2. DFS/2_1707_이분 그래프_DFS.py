import sys

sys.setrecursionlimit(10**6)

K = int(sys.stdin.readline())


def dfs(now, now_color):
    global isColored, result, connected_list
    isColored[now] = now_color

    for next_node in connected_list[now]:
        if isColored[next_node] == 0:
            dfs(next_node, 3 - now_color)
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
            dfs(i, 1)

    print(result)





