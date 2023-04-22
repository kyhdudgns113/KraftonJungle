import sys

sys.setrecursionlimit(10**6)


n = int(sys.stdin.readline())
a = list(sys.stdin.readline().strip())
a.insert(0, '2')

connected_list = list([] for _ in range(n + 1))

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    connected_list[u].append(v)
    connected_list[v].append(u)

result = 0
unions = list(0 for _ in range(n))
unions_size = 0


def dfs(now, isVisited, now_union_idx):
    global connected_list, a, unions, n, unions_size

    for next_node in connected_list[now]:
        if not isVisited & (1 << (n - next_node)):
            if a[now] == '1':
                unions_size += 1
                next_union_idx = unions_size - 1
                unions[next_union_idx] += 1
                if a[next_node] == '1':
                    unions[next_union_idx] += 1
            else:
                next_union_idx = now_union_idx
                if a[next_node] == '1':
                    unions[next_union_idx] += 1

            dfs(next_node, isVisited | (1 << (n - next_node)), next_union_idx)


for i in range(1, n + 1):
    if a[i] == '1':
        isVisited = 1 << (n - i)
        dfs(i, isVisited, -1)
        break

result = 0
for union in unions:
    ll = union
    result += ll * (ll - 1)

print(result)


