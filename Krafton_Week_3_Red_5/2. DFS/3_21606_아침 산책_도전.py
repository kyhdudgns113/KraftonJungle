import sys

sys.setrecursionlimit(200001)


n = int(sys.stdin.readline())
a = int(sys.stdin.readline().strip(), 2)

connected_list = list([] for _ in range(n + 1))
is_finished = list(0 for _ in range(n + 1))

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    connected_list[u].append(v)
    connected_list[v].append(u)

result = 0
unions = [0 for _ in range(n + 1)]
stack_size = 0


def dfs(now, isVisited, now_union_idx):
    global connected_list, a, unions, n, stack_size, is_finished
    is_finished[now] = 1

    for next_node in connected_list[now]:
        if not isVisited & (1 << (n - next_node)):
            if a & (1 << (n - now)):
                stack_size += 1
                next_union_idx = stack_size - 1
                unions[next_union_idx] += 1
                if a & (1 << (n - next_node)):
                    unions[next_union_idx] += 1
            elif a & (1 << (n - next_node)):
                next_union_idx = now_union_idx
                unions[next_union_idx] += 1
            else:
                next_union_idx = now_union_idx

            dfs(next_node, isVisited | (1 << (n - next_node)), next_union_idx)


for i in range(1, n + 1):
    if a & (1 << (n - i)) and is_finished[i] == 0:
        dfs(i, 1 << (n - i), -1)

result = 0
for i in range(stack_size):
    ll = unions[i]
    result += ll * (ll - 1)

print(result)


