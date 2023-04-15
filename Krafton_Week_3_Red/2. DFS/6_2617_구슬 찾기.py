import sys

sys.setrecursionlimit(10 ** 5)

n, m = map(int, sys.stdin.readline().split())

connection_list = list([] for _ in range(n + 1))
bigger_count = list(0 for _ in range(n + 1))
lower_count = list(0 for _ in range(n + 1))

for _ in range(m):
    g1, g2 = map(int, sys.stdin.readline().split())
    connection_list[g1].append(g2)


def dfs(now_bead):
    global connection_list, bigger_count, lower_count, is_visit
    is_visit[now_bead] = True
    return_lower_count = 1
    for next_bead in connection_list[now_bead]:
        if not is_visit[next_bead]:
            bigger_count[next_bead] += 1
            return_lower_count += dfs(next_bead)

    return return_lower_count


for bead in range(1, n + 1):
    is_visit = list(False for _ in range(n + 1))
    lower_count[bead] = dfs(bead) - 1


impossible_counter = 0
for bead in range(1, n + 1):
    impossible_counter += 1 if lower_count[bead] > n // 2 or bigger_count[bead] > n // 2 else 0
print(impossible_counter)

