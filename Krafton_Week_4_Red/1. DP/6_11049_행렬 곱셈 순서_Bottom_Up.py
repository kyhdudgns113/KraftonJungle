import sys

n = int(sys.stdin.readline())
rcs = list([] for _ in range(n))

for _ in range(n):
    r, c = map(int, sys.stdin.readline().split())
    rcs[_] = [r, c]

minimum_cost = list(list(0 for _ in range(n)) for _ in range(n))

for length in range(2, n + 1):
    for start in range(n - length + 1):
        temp_res = 0x7fffffff
        for mid in range(start, start + length - 1):
            temp_res = min(temp_res,
                           minimum_cost[start][mid] + minimum_cost[mid + 1][start + length - 1] +
                           rcs[start][0]*rcs[start + length - 1][1]*rcs[mid][1])
        minimum_cost[start][start + length - 1] = temp_res

sys.stdout.write(f'{minimum_cost[0][n - 1]}')
