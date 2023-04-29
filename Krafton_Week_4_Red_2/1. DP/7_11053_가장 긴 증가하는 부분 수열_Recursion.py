import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

result_length = list(0 for _ in range(n))


def solve(idx_now):
    if idx_now == 0:
        result_length[0] = 1
        return 1
    if result_length[idx_now]:
        return result_length[idx_now]

    result = 1

    for idx_prev in range(idx_now - 1, -1, -1):
        result_prev = solve(idx_prev)
        if a[idx_now] > a[idx_prev]:
            result = max(result, result_prev + 1)

    result_length[idx_now] = result
    return result


solve(n - 1)

print(max(result_length))



