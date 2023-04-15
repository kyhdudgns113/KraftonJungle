import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

ops = list(map(int, sys.stdin.readline().split()))

res_max = -0x7fffffff
res_min = 0x7fffffff


def dfs(now_a_idx, result_idx):
    global n, a, ops, res_max, res_min

    if now_a_idx == n - 1:
        res_max = max(res_max, result_idx)
        res_min = min(res_min, result_idx)
        return

    next_a_idx = now_a_idx + 1

    for i in range(4):
        if ops[i]:
            ops[i] -= 1
            match i:
                case 0:
                    dfs(next_a_idx, result_idx + a[next_a_idx])
                case 1:
                    dfs(next_a_idx, result_idx - a[next_a_idx])
                case 2:
                    dfs(next_a_idx, result_idx * a[next_a_idx])
                case 3:
                    dfs(next_a_idx, (result_idx // a[next_a_idx])
                        if result_idx > 0 or result_idx % a[next_a_idx] == 0
                        else (result_idx // a[next_a_idx] + 1))
            ops[i] += 1


dfs(0, a[0])

print(res_max)
print(res_min)

