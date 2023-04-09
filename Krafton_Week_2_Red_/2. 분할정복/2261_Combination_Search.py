import sys, math
from bisect import bisect_left

n = int(sys.stdin.readline())
pl = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# x축 기준 정렬
pl.sort()
res = 1600000000
min_dist = 40000
axis = list([] for _ in range(20003))

for i in range(n - 1):
    if pl[i][0] == pl[i + 1][0] and \
            pl[i][1] == pl[i + 1][1]:
        print(0)
        exit()

for i in range(n):
    px = pl[i][0]
    py = pl[i][1]
    axis[px].append(py)


def dist_sq_idx(idx_a, idx_b):
    dx = pl[idx_a][0] - pl[idx_b][0]
    dy = pl[idx_a][1] - pl[idx_b][1]
    return dx*dx + dy*dy


def dist_sq_pnt(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return dx*dx + dy*dy


for i in range(n-1):
    tmp = dist_sq_idx(i, i+1)
    res = min(res, tmp)


for i in range(-10000, 10001):
    # (i, axis[i]) 점마다
    for j in range(len(axis[i])):
        for k in range(i+1, 10001):
            if (k - i)*(k - i) >= res:
                break
            l = bisect_left(axis[k], axis[i][j])
            if l < len(axis[k]):
                tmp = dist_sq_pnt(i, axis[i][j], k, axis[k][l])
                res = min(tmp, res)
            if l >= 1:
                tmp = dist_sq_pnt(i, axis[i][j], k, axis[k][l-1])
                res = min(tmp, res)

print(res)
