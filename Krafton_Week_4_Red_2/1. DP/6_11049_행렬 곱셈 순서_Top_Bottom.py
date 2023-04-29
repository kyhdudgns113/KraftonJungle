import sys

n = int(sys.stdin.readline())
rcs = list([] for _ in range(n))

for _ in range(n):
    r, c = map(int, sys.stdin.readline().split())
    rcs[_] = [r, c]


minimum_mul_count = list(list(0 for _ in range(n)) for _ in range(n))


def func_dp(idx_start, idx_end):
    global rcs, minimum_mul_count, n

    if minimum_mul_count[idx_start][idx_end] or idx_start == idx_end:
        return minimum_mul_count[idx_start][idx_end]

    ret = 0x7fffffff

    for i in range(idx_start, idx_end):
        ret = min(ret, func_dp(idx_start, i) + func_dp(i + 1, idx_end) +
                  rcs[idx_start][0]*rcs[i][1]*rcs[idx_end][1])

    minimum_mul_count[idx_start][idx_end] = ret

    return ret


print(func_dp(0, n - 1))



