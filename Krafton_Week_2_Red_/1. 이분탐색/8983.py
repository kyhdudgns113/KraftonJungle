from bisect import bisect_left

import sys

m, n, l = map(int, sys.stdin.readline().split())

sadae_list = list(map(int, sys.stdin.readline().split()))
sadae_list.sort()


def find_idx_sadae(x, left, right):

    global sadae_list, l

    if left == right:
        return left

    mid = (left + right) // 2
    if x < sadae_list[mid]:
        return find_idx_sadae(x, left, mid)
    elif abs(x - sadae_list[mid]) <= abs(x - sadae_list[mid + 1]):
        return mid
    else:
        return find_idx_sadae(x, mid + 1, right)


count = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    idx_sadae = find_idx_sadae(x, 0, m - 1)

    if abs(sadae_list[idx_sadae] - x) + y <= l:
        count += 1
print(count)
