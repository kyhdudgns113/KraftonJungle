import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

connected_list = list([] for _ in range(n + 1))

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    connected_list[a].append(b)
    connected_list[b].append(a)


hasParent = list(0 for _ in range(n + 1))
hasParent[1] = 1


def dfs(now):
    global hasParent

    for son in connected_list[now]:
        if hasParent[son] == 0:
            hasParent[son] = now
            dfs(son)


dfs(1)

for i in range(2, n + 1):
    print(hasParent[i])



